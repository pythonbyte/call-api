# Generated by Django 2.1 on 2018-08-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callapi', '0004_auto_20180824_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonebill',
            name='period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phonebill',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
