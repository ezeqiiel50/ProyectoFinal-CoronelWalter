# Generated by Django 4.1.7 on 2023-04-19 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppShortStories', '0013_alter_mensaje_motivo_alter_mensaje_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='motivo',
            field=models.IntegerField(choices=[(1, 'Consulta sobre la App'), (2, 'Problemas en la Registracion'), (3, 'Problemas al Loguearse'), (4, 'Problemas en la App'), (5, 'Otros')], default=1),
        ),
    ]