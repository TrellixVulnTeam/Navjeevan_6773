# Generated by Django 2.1.5 on 2020-08-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherStu', '0026_auto_20200730_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq_post',
            name='subject',
            field=models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Mathematics', 'Mathematics'), ('Rhymes', 'Rhymes'), ('English Literature Book1', 'English Literature Book1'), ('English Literature Book2', 'English Literature Book2'), ('English Grammar', 'English Grammar'), ('Hindi Literature', 'Hindi Literature'), ('Hindi Grammar', 'Hindi Grammar'), ('Science', 'Science'), ('Computer', 'Computer'), ('Social Studies', 'Social Studies'), ('History', 'History'), ('Civics', 'Civics'), ('Geography', 'Geography'), ('Political Science', 'Political Science'), ('Economics', 'Economics'), ('Physical Education', 'Physical Education'), ('Computer Science', 'Computer Science'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Accountancy', 'Accountancy'), ('Business Studies', 'Business Studies'), ('Political Science', 'Political Science'), ('Psychology', 'Psychology')], max_length=255),
        ),
        migrations.AlterField(
            model_name='stu_task',
            name='subject',
            field=models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Mathematics', 'Mathematics'), ('Rhymes', 'Rhymes'), ('English Literature Book1 ', 'English Literature Book1'), ('English Literature Book2', 'English Literature Book2'), ('English Grammar', 'English Grammar'), ('Hindi Literature', 'Hindi Literature'), ('Hindi Grammar', 'Hindi Grammar'), ('Science', 'Science'), ('Computer', 'Computer'), ('Social Studies', 'Social Studies'), ('Civics', 'Civics'), ('History', 'History'), ('Geography', 'Geography'), ('Political Science', 'Political Science'), ('Economics', 'Economics'), ('Physical Education', 'Physical Education'), ('Computer Science', 'Computer Science'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Accountancy', 'Accountancy'), ('Business Studies', 'Business Studies'), ('Political Science', 'Political Science'), ('Psychology', 'Psychology')], max_length=255),
        ),
    ]
