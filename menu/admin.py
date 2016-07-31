from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Menu


class MenuAdmin(DjangoMpttAdmin):
    list_display = ('name',)
    tree_auto_open = 0
    tree_load_on_demand = False
    '''
    tree_auto_open accept three values True, False,Integer - autopen all nodes, do not autopen and autopen unitl state value
    '''
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(Menu, MenuAdmin)
