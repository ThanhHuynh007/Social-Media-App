# Generated by Django 5.0.6 on 2024-07-20 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_trend'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
