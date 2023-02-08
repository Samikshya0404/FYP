# Generated by Django 3.1 on 2023-02-04 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='style',
            name='thumbnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='style',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]