from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from django.utils.text import slugify


class Category(MPTTModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, unique=True, blank=True)  # blank=True qo'shildi

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    class MPTTMeta:
        order_insertion_by = ['title',]


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    price = models.DecimalField(max_digits=100, null=True, decimal_places=2, verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color, null=True, verbose_name='Colors')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='Slug')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # If slug is not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Option(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options', verbose_name='Product')
    key = models.CharField(max_length=200, verbose_name='key')
    value = models.CharField(max_length=200, verbose_name='value')

    def __str__(self):
        return self.key


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='galleries', verbose_name='Product')
    image = models.ImageField(upload_to='gallery/', verbose_name='Image')

    def __str__(self):
        return self.product.title

    