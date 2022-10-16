from tabnanny import verbose
from django.db import models
from django.urls import reverse


class  Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category, 
                                related_name='products', 
                                on_delete=models.CASCADE)
    
    name = models.CharField(max_length=150, db_index=True, verbose_name='Найменування')
    slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Ссилка')
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True, verbose_name='Опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    available = models.BooleanField(default=True, verbose_name='Наявність')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлений')
    uploaded = models.DateTimeField(auto_now=True, verbose_name='Зміненний')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])