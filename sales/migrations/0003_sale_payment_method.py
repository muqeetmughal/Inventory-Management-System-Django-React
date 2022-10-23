# Generated by Django 4.1.1 on 2022-10-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_remove_sale_reference_number_remove_sale_sale_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('banktransfer', 'Bank Transfer'), ('cheque', 'Cheque'), ('unpaid', 'Unpaid')], default='unpaid', max_length=20),
        ),
    ]