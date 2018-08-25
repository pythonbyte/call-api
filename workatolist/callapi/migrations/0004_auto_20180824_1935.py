# Generated by Django 2.1 on 2018-08-24 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('callapi', '0003_callrecord_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonebill',
            name='records',
        ),
        migrations.AddField(
            model_name='callrecord',
            name='bill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='callapi.PhoneBill'),
        ),
    ]
