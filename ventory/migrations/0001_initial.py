# Generated by Django 4.2.7 on 2023-11-27 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Concealer', 'Concealer'), ('Mascara', 'Mascara'), ('Blush', 'Blush'), ('Foundation', 'Foundation'), ('Eye shadow', 'Eye shadow'), ('Eye liner', 'Eye liner'), ('Primer', 'Primer'), ('Clinique', 'Clinique'), ('Bronzer', 'Bronzer'), ('Highlighter', 'Highlighter'), ('Maybelline', 'Maybelline'), ('Powder', 'Powder'), ('Mosturizer', 'Mosturizer'), ('Cream', 'Cream'), ('Shampoo', 'Shampoo')], max_length=255)),
                ('barcode', models.CharField(max_length=14, unique=True)),
                ('quantity_available', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventory.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventory.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='ventory.CartItem', to='ventory.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
