# Generated by Django 2.1.5 on 2019-05-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_iddata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iddata',
            old_name='last_name',
            new_name='surname',
        ),
        migrations.AddField(
            model_name='iddata',
            name='second_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
