from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ContactMessageViewSet, SocialLinksViewSet, UserEmailViewSet, SiteInfoViewSet, BigSliderViewSet, SmallSliderViewSet, CategoriesViewSet, CommentViewSet

app_name = 'core'

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'contact-messages', ContactMessageViewSet)
router.register(r'social-links', SocialLinksViewSet)
router.register(r'user-emails', UserEmailViewSet)
router.register(r'site-info', SiteInfoViewSet)
router.register(r'big-sliders', BigSliderViewSet)
router.register(r'small-sliders', SmallSliderViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path
# from .views import (home_view, shopdetail_view, contact_view,
#                     footer_email_view, discount_offers, search_view,
#                     product_list)

#
# urlpatterns = [
#     path('', home_view, name='home'),
#     path('shop', product_list, name='shop'),
#     path('detail', shopdetail_view, name='detail'),
#     path('contact', contact_view, name='contact'),
#     path('footer-email/', footer_email_view, name='footer_email'),
#     path('discount-offers/', discount_offers, name='discount_offers'),
#     path('search/', search_view, name='search')
# ]


