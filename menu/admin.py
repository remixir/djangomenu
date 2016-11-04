from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Menu, Tiles, PDF

from forms import AdminMenuForm

class PDFFileInlineAdmin(admin.TabularInline):
    model = PDF

class MenuAdmin(DjangoMpttAdmin):
    form = AdminMenuForm
    inlines = [PDFFileInlineAdmin,]

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser




admin.site.register(Tiles, MenuAdmin)
admin.site.register(PDF)