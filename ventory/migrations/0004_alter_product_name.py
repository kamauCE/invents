# Generated by Django 4.2.7 on 2023-11-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventory', '0003_remove_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(choices=[('book', 'book'), ('water', 'water'), ('plates', 'plates'), ('Concealer', 'Concealer'), ('Foundation', 'Foundation'), ('Eye shadow', 'Eye shadow'), ('Eye liner', 'Eye liner'), ('Bronzer', 'Bronzer'), ('Powder', 'Powder'), ('Mosturizer', 'Mosturizer'), ('Cream', 'Cream'), ('Shampoo', 'Shampoo')], max_length=255),
        ),
    ]
