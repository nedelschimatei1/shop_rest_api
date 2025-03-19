# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.views import APIView
# from rest_framework.serializers import BaseSerializer
# from rest_framework.pagination import PageNumberPagination
from collections.abc import Sequence
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework import status
from .filters import ProductFilter
from .models import Product, Collection, OrderItem, Review, Cart, \
    CartItem, Customer, Order, ProductImage
from .serializers import ProductSerializer, CollectionSerializer, \
    ReviewSerializer, CartSerialzier, CartItemSerializer, \
    AddCartItemSerializer, UpdateCartItemSerializer, CustomerSerializer, \
    OrderSerializer, CreateOrderSerializer, UpdateOrderSerializer, \
    ProductImageSerializer
from .permissions import IsAdminOrReadOnly, ViewDjangoModelPermissions, \
    ViewCustomerHistoryPermission


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('images').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    # generic filtering
    filter_backend = [DjangoFilterBackend,
                      SearchFilter, OrderingFilter]  # type: ignore
    filterset_class = ProductFilter
    # search
    search_fields = ['title', 'description']
    # order
    ordering_fields = ['unit_price', 'last_update']

    # filtering
    # def get_queryset(self) -> QuerySet:
    #     queryset = Product.objects.all()
    #     collection_id = self.request.query_params.get('collection_id')
    #     if collection_id:
    #         queryset = Product.objects.filter(collection_id=collection_id)
    #     return queryset

    def get_serializer_context(self) -> dict[str, Any]:
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs) -> Response:
        # type: ignore
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response(
                {'error': 'Product cannot be deleted because it is associated with an order item.'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Collection.objects\
        .annotate(products_count=Count('products'))\
        .all()
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs) -> Response:
        collection = self.get_object()
        if collection.products.count() > 0:  # type: ignore
            return Response(
                {'error': 'Collection cannot be deleted (items > 0)'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self) -> QuerySet:
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self) -> dict[str, Any]:
        return {'product_id': self.kwargs['product_pk']}


class CartViewSet(CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerialzier


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        elif self.request.method == "PATCH":
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self) -> dict[str, Any]:
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects\
            .filter(cart_id=self.kwargs['cart_pk'])\
            .select_related('product')


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # DjangoModelPermissions or my custom class
    permission_classes = [IsAdminUser]

    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    def history(self, request, pk):
        return Response("nice history")

    # type: ignore
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request) -> Response | None:
        customer = Customer.objects.get(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class OrderViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data, context={
                                           'user_id': self.request.user.id})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()

        customer_id = Customer.objects.only('id')\
            .get(user_id=user.id)
        return Order.objects.filter(customer_id=customer_id)


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_serializer_context(self) -> dict[str, Any]:
        return {'product_id': self.kwargs['product_pk']}

    def get_queryset(self) -> QuerySet:
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])
