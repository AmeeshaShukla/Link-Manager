# Generated by Django 3.2 on 2021-08-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amazon', models.URLField()),
                ('airbnb', models.URLField()),
                ('blog', models.URLField()),
                ('book', models.URLField()),
                ('cloud', models.URLField()),
                ('codepen', models.URLField()),
                ('database', models.URLField()),
                ('email', models.URLField()),
                ('facebook', models.URLField()),
                ('github', models.URLField()),
                ('google_drive', models.URLField()),
                ('google_play', models.URLField()),
                ('hackerRank', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
                ('qr_code', models.URLField()),
                ('quora', models.URLField()),
                ('reddit', models.URLField()),
                ('slideshare', models.URLField()),
                ('snapchat', models.URLField()),
                ('telegram', models.URLField()),
                ('twitch', models.URLField()),
                ('twitter', models.URLField()),
                ('website', models.URLField()),
                ('youtube', models.URLField()),
            ],
        ),
    ]
