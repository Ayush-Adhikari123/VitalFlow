# Generated by Django 4.2.7 on 2023-12-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=32)),
                ('Password', models.CharField(max_length=16)),
            ],
        ),
    ]
