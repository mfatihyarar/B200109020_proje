# Generated by Django 4.1.4 on 2022-12-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_settings_setting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='contact',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=models.TextField(blank=True),
        ),
    ]
