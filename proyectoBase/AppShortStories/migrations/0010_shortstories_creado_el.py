# Generated by Django 4.1.7 on 2023-04-18 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppShortStories', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortstories',
            name='creado_el',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]