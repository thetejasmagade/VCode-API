# Generated by Django 3.2.7 on 2021-10-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='codedescription',
            field=models.CharField(blank=True, max_length=555),
        ),
    ]
