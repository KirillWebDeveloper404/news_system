# Generated by Django 4.0.6 on 2022-08-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='animals',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='kids',
            field=models.BooleanField(null=True),
        ),
    ]
