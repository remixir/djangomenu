from django.db import models
from mptt.models import TreeForeignKey, MPTTModel, raise_if_unsaved


class Menu(MPTTModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(verbose_name='content')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    '''
    TreeForeignKey basic ForeignKey, but uses mptt's
    I used this to generat a ModelForm with correct widget
    '''

    def __str__(self):
        return self.name

    def has_parent(self):
        return self.parent != None

    @raise_if_unsaved
    def get_family(self):
        """
        Returns a ``QuerySet`` containing the ancestors, the model itself
        and the descendants, in tree order.
        """
        opts = self._mptt_meta

        left = getattr(self, opts.left_attr)
        right = getattr(self, opts.right_attr)

        ancestors = Q(**{
            "%s__lte" % opts.left_attr: left,
            "%s__gte" % opts.right_attr: right,
            opts.tree_id_attr: self._mpttfield('tree_id'),
        })

        descendants = Q(**{
            "%s__gte" % opts.left_attr: left,
            "%s__lte" % opts.left_attr: right,
            opts.tree_id_attr: self._mpttfield('tree_id'),
        })

        return self._tree_manager.filter(ancestors | descendants)
