# Generated by Django 3.0.2 on 2020-09-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_order_orderitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='acceptorder',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='declineorder',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
