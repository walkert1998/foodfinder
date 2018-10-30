from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from foodapp.views import restaurant_list, restaurant_detail

@apphook_pool.register
class RestaurantApphook(CMSApp):
    app_name = "restaurant"
    name = _("Restaurant Application")

    def get_urls(self, page=none, language=None, **kwargs):
        return [
            url(r'^$', restaurant_list.as_view()),
            url(r'^(?P<slug>[\w-]+)/?$', restaurant_detail.as_view()),
        ]
