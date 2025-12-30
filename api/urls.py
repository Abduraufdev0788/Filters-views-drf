from django.urls import path
# from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

from .views import ProductViewSet

urlpatterns = [
    # path("products/", ProductListCreateView.as_view(), name="products" ),
    path("products/<int:pk>/", ProductViewSet.as_view({'get':'retieve', 'put':'update', 'delete':'destroy'})),
    path("products/", ProductViewSet.as_view({'get':'list', 'post':'create'})),

]
