# Generated by Django 4.1.3 on 2022-12-05 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='idno',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='content.category'),
        ),
    ]
