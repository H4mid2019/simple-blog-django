# Generated by Django 2.2.4 on 2019-09-17 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_brief_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brief',
            name='brief',
            field=models.TextField(max_length=500),
        ),
    ]
