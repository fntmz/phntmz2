# Generated by Django 4.0 on 2022-08-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author_id', models.CharField(max_length=16)),
                ('detail', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
