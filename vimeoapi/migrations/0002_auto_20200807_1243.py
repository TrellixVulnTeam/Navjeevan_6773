# Generated by Django 2.0 on 2020-08-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vimeoapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vimeo',
            name='college',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vimeo',
            name='sub',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vimeo',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
