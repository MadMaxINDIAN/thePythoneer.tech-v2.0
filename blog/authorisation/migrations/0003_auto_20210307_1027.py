# Generated by Django 3.1.4 on 2021-03-07 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20210304_2353'),
        ('authorisation', '0002_auto_20210306_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='author',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_app.author'),
        ),
    ]
