# Generated by Django 3.0.8 on 2020-07-27 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200726_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='order_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.OrderStatus'),
        ),
    ]
