# Generated by Django 2.1.5 on 2019-05-29 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20190529_0736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iddata',
            old_name='certified_id',
            new_name='certified_id_copy',
        ),
    ]
