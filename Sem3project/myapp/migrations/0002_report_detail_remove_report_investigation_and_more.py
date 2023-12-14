# Generated by Django 4.2.7 on 2023-12-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investigation', models.CharField(max_length=50)),
                ('results', models.CharField(max_length=50)),
                ('reference_value', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='investigation',
        ),
        migrations.RemoveField(
            model_name='report',
            name='reference_value',
        ),
        migrations.RemoveField(
            model_name='report',
            name='results',
        ),
        migrations.RemoveField(
            model_name='report',
            name='unit',
        ),
    ]
