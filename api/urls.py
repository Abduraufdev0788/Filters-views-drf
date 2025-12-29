from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    # path("products/", ProductListCreateView.as_view(), name="products" ),
    # path("products/<inst:pk>/", ProductRetrieveUpdateDestroyView.as_view(), name="products" ),
]
