# Generated by Django 3.0.5 on 2020-05-27 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
