# Generated by Django 5.0.6 on 2024-08-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='food_items',
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='dashboard.orderitem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
