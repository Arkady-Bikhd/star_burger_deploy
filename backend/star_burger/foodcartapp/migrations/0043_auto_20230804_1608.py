# Generated by Django 3.2.15 on 2023-08-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0042_update_order_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_new_order',
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Ne', 'Новый заказ'), ('Pr', 'Обработанный'), ('Fi', 'Завершенный')], default='Ne', max_length=2),
        ),
    ]
