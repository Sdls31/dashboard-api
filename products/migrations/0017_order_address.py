# Generated by Django 5.0.4 on 2024-05-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_remove_client_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Mexico', max_length=50),
        ),
    ]
