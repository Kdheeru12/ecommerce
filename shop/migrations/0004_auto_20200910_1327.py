# Generated by Django 3.0.2 on 2020-09-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200910_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderitems',
            field=models.TextField(blank=True, null=True),
        ),
    ]