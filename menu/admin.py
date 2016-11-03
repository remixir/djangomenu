from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Tiles, PDF, CategoryPDF

from forms import AdminMenuForm


class MenuAdmin(DjangoMpttAdmin):
    form = AdminMenuForm

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

admin.site.register(Tiles, MenuAdmin)
admin.site.register(PDF)
admin.site.register(CategoryPDF)