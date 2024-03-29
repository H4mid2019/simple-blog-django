# Generated by Django 2.2.5 on 2019-10-03 15:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_brief_thumb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('subtitle', models.CharField(blank=True, max_length=40, null=True)),
                ('tags', models.CharField(blank=True, max_length=40, null=True)),
                ('slug', models.SlugField(allow_unicode=True, null=True, unique=True)),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('brief', models.TextField(max_length=185)),
                ('article', models.TextField(blank=True, max_length=9000000, null=True)),
                ('imag', models.ImageField(blank=True, null=True, upload_to='blog_image/')),
                ('date_added', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Brief',
        ),
    ]
