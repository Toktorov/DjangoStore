from django.db import models
from django.db.models.signals import pre_save
from utils.slug_generator import unique_slug_generators
from apps.categories.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='products_user'
    )
    slug = models.SlugField(blank=True, unique=True)
    price = models.PositiveIntegerField(verbose_name='Цена:')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество:')
    is_stock = models.BooleanField(default=True, db_index=True)
    category = models.ForeignKey(
        Category,
        related_name='product_category',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'ПРОДУКТ'
        verbose_name_plural = 'ПРОДУКТЫ'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.title} -- {self.is_stock}"


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='product',
        verbose_name='Картинки',
        blank=True, null=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_image'
    )

    def __str__(self):
        return f"{self.product.title} -- {self.product.id}"


def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Product)
