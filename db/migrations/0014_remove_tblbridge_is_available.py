# Generated by Django 3.1.7 on 2021-07-22 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0013_tblbridge_is_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblbridge',
            name='is_available',
        ),
    ]
