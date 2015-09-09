from django.contrib import admin

from pastryio.admin.mixins import ArchiveAdminMixin
from profiles.models import BaseProfile


class BaseProfileAdmin(ArchiveAdminMixin):
    model = BaseProfile


admin.site.register(BaseProfile, BaseProfileAdmin)
