from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Menu, Tiles

from forms import AdminMenuForm


class MenuAdmin(DjangoMpttAdmin):
    form = AdminMenuForm
    # change_form_template = 'change_form.html'
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(Menu, MenuAdmin)
admin.site.register(Tiles, MenuAdmin)
