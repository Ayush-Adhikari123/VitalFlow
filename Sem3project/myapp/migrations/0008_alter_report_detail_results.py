# Generated by Django 4.2.7 on 2023-12-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_report_detail_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_detail',
            name='results',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
