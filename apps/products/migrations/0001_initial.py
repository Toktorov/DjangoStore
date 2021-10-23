# Generated by Django 3.2.7 on 2021-10-23 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('price', models.PositiveIntegerField(verbose_name='Цена:')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество:')),
                ('is_stock', models.BooleanField(db_index=True, default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='categories.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ПРОДУКТ',
                'verbose_name_plural': 'ПРОДУКТЫ',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Картинки')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.product')),
            ],
        ),
    ]
