# Generated by Django 4.2.7 on 2024-01-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
