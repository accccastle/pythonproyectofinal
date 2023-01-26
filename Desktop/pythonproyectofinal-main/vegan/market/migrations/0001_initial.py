# Generated by Django 4.1.4 on 2023-01-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationame', models.CharField(max_length=100)),
                ('type_shop', models.CharField(max_length=100)),
                ('name_shop', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_market', models.CharField(max_length=100)),
                ('name_product', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('food_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Restaurants',
                'verbose_name_plural': 'Restaurants',
            },
        ),
    ]