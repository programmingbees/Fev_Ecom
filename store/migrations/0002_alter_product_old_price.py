# Generated by Django 4.1.3 on 2022-11-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Product Old Price'),
        ),
    ]
