import datetime
from django.db import models
from pastryio.models import managers
from pastryio.utils import int_to_b64


class ArchiveMixin(models.Model):
    """
    A model that is only marked as deleted when the .delete() method is
    called, instead of actually deleted.

    Calling .delete() on this object will only mark it as deleted, and it will
    not show up in the default queryset.  If you want to see all objects,
    including the ones marked as deleted, use:

    ArchiveModel.objects.all_objects.all()

    If you want to just see the ones marked as deleted, use:

    ArchiveModel.objects.deleted.all()
    """
    b64id = models.CharField(max_length=2047, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = managers.ArchiveManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(ArchiveMixin, self).save(*args, **kwargs)
        self.b64id = int_to_b64(self.pk)
        super(ArchiveMixin, self).save(*args, **kwargs)

    def delete(self, using=None):
        from django.db import router
        from django.db.models import signals
        using = using or router.db_for_write(self.__class__, instance=self)

        assert self._get_pk_val() is not None, \
            "{} object can't be deleted because its {} attribute " \
            "is set to None.".format(self._meta.object_name, self._meta.pk.attname)

        if not self.deleted_at:
            signals.pre_delete.send(
                sender=self.__class__,
                instance=self, using=using)

            self.deleted_at = datetime.datetime.now()
            self.save(using=using)

            signals.post_delete.send(
                sender=self.__class__,
                instance=self, using=using)

    def really_delete(self, using=None):
        """
        Actually deletes the instance.
        """
        super(ArchiveMixin, self).delete(using=using)
