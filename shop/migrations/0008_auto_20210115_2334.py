# Generated by Django 3.1.2 on 2021-01-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='products',
            new_name='product',
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(default='Failed', max_length=200),
        ),
    ]