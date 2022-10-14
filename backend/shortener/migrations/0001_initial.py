# Generated by Django 4.1.2 on 2022-10-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('long_url', models.URLField()),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'shortened_urls',
            },
        ),
    ]
