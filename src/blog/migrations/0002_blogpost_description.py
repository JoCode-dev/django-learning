# Generated by Django 3.1.6 on 2024-01-21 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
