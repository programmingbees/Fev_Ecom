# Generated by Django 4.1.3 on 2022-11-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='my-product', unique=True, verbose_name=''),
            preserve_default=False,
        ),
    ]