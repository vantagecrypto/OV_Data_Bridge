# Generated by Django 3.1.7 on 2021-07-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbluser',
            options={},
        ),
        migrations.AddField(
            model_name='tbluser',
            name='permission',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='tbluser',
            table='TBLUSER',
        ),
    ]
