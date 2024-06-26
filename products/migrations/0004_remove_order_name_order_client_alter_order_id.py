# Generated by Django 5.0.4 on 2024-05-05 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_client_remove_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='products.client'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
