# Generated by Django 3.1 on 2023-02-04 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_dec',
            new_name='decription',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_address',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_name',
            new_name='venue',
        ),
    ]