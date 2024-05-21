from rest_framework import generics, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductListCreate(generics.ListCreateAPIView):
    # Tüm ürünleri listeleyen ve yeni ürün oluşturan API view'i
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Arama ve sıralama filtreleri ekleyen view sınıfı
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # Arama yapılacak alanlar
    search_fields = ['title', 'description', 'category__name']
    # Sıralama yapılacak alanlar
    ordering_fields = ['stock']

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    # Tek bir ürünü görüntüleyen, güncelleyen veya silen API view'i
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    # Tüm kategorileri listeleyen ve yeni kategori oluşturan API view'i
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # Tek bir kategoriyi görüntüleyen, güncelleyen veya silen API view'i
    queryset = Category.objects.all()
    serializer_class = CategorySerializer






from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
