# Generated by Django 4.2.7 on 2024-01-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.CharField(max_length=500)),
                ('show', models.BooleanField(default=True)),
            ],
        ),
    ]