# Generated by Django 4.1.7 on 2023-03-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
