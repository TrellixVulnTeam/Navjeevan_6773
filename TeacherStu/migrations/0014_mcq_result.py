# Generated by Django 2.1.5 on 2020-07-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherStu', '0013_auto_20200716_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQ_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=255)),
                ('clas', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('result', models.IntegerField()),
                ('total', models.IntegerField()),
                ('correct', models.IntegerField()),
                ('wrong', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
