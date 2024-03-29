# Generated by Django 4.0 on 2022-08-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_posts_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.CharField(max_length=16)),
                ('author_id', models.CharField(max_length=16)),
                ('rating', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
