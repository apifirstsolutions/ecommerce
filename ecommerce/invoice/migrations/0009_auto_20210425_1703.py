# Generated by Django 2.2.20 on 2021-04-25 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_auto_20191115_2151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'get_latest_by': 'modified'},
        ),
    ]
