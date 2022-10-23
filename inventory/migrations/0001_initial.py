# Generated by Django 4.1.1 on 2022-10-17 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('logo', models.ImageField(default=None, upload_to='brands')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sku', models.CharField(blank=True, max_length=20, null=True)),
                ('hsn', models.CharField(blank=True, max_length=6, null=True)),
                ('minimum_quantity', models.IntegerField(default=0)),
                ('lot_number', models.CharField(blank=True, max_length=50, null=True)),
                ('expiry_date', models.DateField()),
                ('desciption', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='products')),
                ('price', models.FloatField()),
                ('profit_margin', models.FloatField()),
                ('barcode_symbology', models.CharField(choices=[('code128', 'Code 128'), ('code39', 'Code 39')], default='code128', max_length=20)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]