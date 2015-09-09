from django.db import models


class ArchiveManager(models.Manager):
    def get_queryset(self):
        return super(ArchiveManager, self).get_queryset().filter(
            deleted_at__isnull=True)

    def deleted(self):
        return super(ArchiveManager, self).get_queryset()
