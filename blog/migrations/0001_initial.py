# Generated by Django 4.0.3 on 2022-03-31 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('category', models.SlugField(max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
