# Generated by Django 5.0.6 on 2024-10-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_favoritemovie_delete_news_delete_newsarticle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='posters/'),
        ),
    ]
