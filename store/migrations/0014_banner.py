# Generated by Django 4.1.3 on 2023-01-11 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_variationvalue_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Banner Title')),
                ('short_desc', models.TextField(blank=True, max_length=250, null=True, verbose_name='Short Description')),
                ('image', models.ImageField(upload_to='banner', verbose_name='Banner Image')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='banner')),
            ],
        ),
    ]
