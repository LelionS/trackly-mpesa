# Generated by Django 5.1.1 on 2024-09-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210404_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=55),
        ),
    ]
