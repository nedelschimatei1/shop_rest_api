from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router = DefaultRouter()  # type: ignore
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')  # (lookup = product_pk)
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')
product_router.register('images', views.ProductImageViewSet,
                        basename='product-images')

cart_router = routers.NestedDefaultRouter(
    router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet,
                     basename='cart-items')

urlpatterns = router.urls + product_router.urls + cart_router.urls
