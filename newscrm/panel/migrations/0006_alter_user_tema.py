# Generated by Django 3.2.8 on 2022-09-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_alter_user_tema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tema',
            field=models.ManyToManyField(related_name='panel_user_panel_tema_through', to='panel.Tema', verbose_name='Тематика(выбор)'),
        ),
    ]