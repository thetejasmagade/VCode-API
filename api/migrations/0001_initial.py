# Generated by Django 3.2.7 on 2021-09-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('codetitle', models.CharField(max_length=255)),
                ('htmlcode', models.TextField(blank=True)),
                ('jscode', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
    ]
