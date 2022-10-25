# Generated by Django 4.1.2 on 2022-10-25 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products_in_warehouse', to='inventory.warehouse'),
        ),
    ]
