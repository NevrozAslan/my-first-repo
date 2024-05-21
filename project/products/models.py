from django.db import models

class Category(models.Model):
    # Kategori adı için maksimum 100 karakterlik bir karakter alanı
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    # Ürün başlığı için maksimum 200 karakterlik bir karakter alanı
    title = models.CharField(max_length=200)
    # Ürün açıklaması için metin alanı
    description = models.TextField()
    # Kategori ile ilişkilendirilmiş bir dış anahtar
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    # Stok miktarı için pozitif bir tamsayı alanı
    stock = models.PositiveIntegerField()
    # Ürünün yayında olup olmadığını belirten bir boolean alanı, varsayılan olarak False
    is_live = models.BooleanField(default=False)

    # Modelin kaydedilmesi işlemi
    def save(self, *args, **kwargs):
        # Eğer ürün bir kategoriye sahipse ve stok miktarı 0'dan büyükse, ürünü yayında olarak işaretle
        if self.category and self.stock > 0:
            self.is_live = True
        else:
            self.is_live = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
