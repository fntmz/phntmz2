# Generated by Django 4.0 on 2022-06-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
