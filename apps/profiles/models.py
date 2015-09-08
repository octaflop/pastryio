from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import (
    User
)

from pastryio.models.mixins import ArchiveMixin


class BaseProfile(ArchiveMixin):
    user = models.OneToOneField(User)
    avatar = models.ImageField(_("avatar"), blank=True)

    def __unicode__(self):
        return self.user.username
