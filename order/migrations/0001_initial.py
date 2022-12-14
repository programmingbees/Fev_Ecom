# Generated by Django 4.1.3 on 2022-12-14 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0010_productimages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quanftity of Product')),
                ('purchased', models.BooleanField(verbose_name='Purchased or Not')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Adding Time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False, verbose_name='Ordered')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('paymentId', models.CharField(blank=True, max_length=300, null=True, verbose_name='Payment Id')),
                ('orderdId', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ordered Id')),
                ('orderitems', models.ManyToManyField(to='order.cart', verbose_name='Ordered Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
    ]
