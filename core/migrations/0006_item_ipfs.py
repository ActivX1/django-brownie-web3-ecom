# Generated by Django 2.2.14 on 2022-07-23 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220723_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ipfs',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
