# Generated by Django 3.1.7 on 2021-07-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0012_auto_20210722_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblbridge',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
