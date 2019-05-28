# Generated by Django 2.1.5 on 2019-05-28 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20190527_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='references',
            name='permissions',
        ),
        migrations.AddField(
            model_name='requestpermissions',
            name='reference',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.References'),
            preserve_default=False,
        ),
    ]