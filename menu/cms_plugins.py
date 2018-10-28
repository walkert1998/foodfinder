from menu.models import MenuItem
from menu.models import Menu
from menu.admin import MenuItemInline
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

@plugin_pool.register_plugin
class MenuPlugin(CMSPluginBase):
    model = Menu
    module = _("Menu")
    name = _("Menu Plugin")
    render_template = "menu.html"
    cache = False
    inlines = [MenuItemInline,]

    def render(self, context, instance, placeholder):
        context = super(
            MenuPlugin, self).render(
                context,
                instance,
                placeholder
                )
        context.update({
            'items': MenuItem.objects.all()
        })
        return context
