# Generated by Django 4.1.4 on 2023-02-01 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0006_brand_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='type_brand',
            field=models.CharField(choices=[('Mercado', 'Mercado'), ('Restaurante', 'Restaurante'), ('Emprendimiento', 'Emprendimiento')], max_length=50),
        ),
    ]
