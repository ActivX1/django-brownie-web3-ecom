# Generated by Django 2.2.14 on 2022-07-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_vendorpayable_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorpayable',
            name='payment_tx',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
