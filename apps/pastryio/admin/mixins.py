from django.contrib import admin


class ArchiveAdminMixin(admin.ModelAdmin):
    exclude = ('b64id', 'deleted_at',)