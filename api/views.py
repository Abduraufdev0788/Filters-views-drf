from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .filters import  ProductFilter

from .models import Product


from .serializers import ProductSerializer


class ProductListCreateView(ListCreateAPIView):
 queryset = Product.objects.all()
 serializer_class = ProductSerializer
 pagination_class = LimitOffsetPagination
 

 
class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
 queryset = Product.objects.all()
 serializer_class = ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
 queryset = Product.objects.all()
 serializer_class = ProductSerializer
 filter_backends = [DjangoFilterBackend]
 filterset_fields = ['category', 'price']
 filterset_class = ProductFilter

 