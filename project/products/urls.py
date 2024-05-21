from django.urls import path
from .views import ProductListCreate, ProductDetail, CategoryListCreate, CategoryDetail



from . import views




urlpatterns = [
    # Ürünlerin listelendiği ve yeni ürünlerin oluşturulabildiği URL
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    # Tek bir ürünün detaylarının görüntülendiği, güncellendiği veya silindiği URL
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    # Kategorilerin listelendiği ve yeni kategorilerin oluşturulabildiği URL
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    # Tek bir kategorinin detaylarının görüntülendiği, güncellendiği veya silindiği URL
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),



     path('', views.home, name='home'),


     
]
