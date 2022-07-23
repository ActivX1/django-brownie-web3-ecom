# Generated by Django 2.2.14 on 2022-07-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('T', 'Trousers'), ('SW', 'Sport wear'), ('OW', 'Outwear'), ('E', 'Ethnic')], max_length=2),
        ),
    ]
