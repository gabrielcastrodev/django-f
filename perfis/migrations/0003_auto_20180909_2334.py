# Generated by Django 2.1.1 on 2018-09-10 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_auto_20180909_2332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='nome',
            new_name='usuario',
        ),
    ]