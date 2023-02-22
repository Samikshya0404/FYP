# Generated by Django 3.1 on 2023-02-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
