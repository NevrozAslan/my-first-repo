from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    # Kategori modelini seri hale getirmek için kullanılan serializer sınıfı
    class Meta:
        model = Category
        # Tüm alanları (id ve name) içerecek şekilde kategori modelinin tüm alanlarını kullan
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # Ürün modelini seri hale getirmek için kullanılan serializer sınıfı
    class Meta:
        model = Product
        # Tüm alanları (id, title, description, category, stock, is_live) içerecek şekilde ürün modelinin tüm alanlarını kullan
        fields = '__all__'

    # Veriyi doğrulamak için kullanılan özel bir metot
    def validate(self, data):
        # Başlık alanının boş olmamasını doğrula
        if not data['title']:
            raise serializers.ValidationError("Title cannot be empty")
        # Başlık alanının maksimum 200 karakteri geçmemesini doğrula
        if len(data['title']) > 200:
            raise serializers.ValidationError("Title cannot exceed 200 characters")
        # Ürünün bir kategoriye sahip olmasını doğrula
        if not data['category']:
            raise serializers.ValidationError("Product must have a category")
        # Stok miktarının en az 1 olmasını doğrula
        if data['stock'] < 1:
            raise serializers.ValidationError("Stock must be at least 1 to be live")
        return data
