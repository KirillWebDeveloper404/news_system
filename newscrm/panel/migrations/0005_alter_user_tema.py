# Generated by Django 3.2.8 on 2022-09-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_auto_20220905_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tema',
            field=models.ManyToManyField(null=True, related_name='panel_user_panel_tema_through', to='panel.Tema', verbose_name='Тематика(выбор)'),
        ),
    ]