# Generated by Django 2.1.5 on 2020-08-10 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherStu', '0027_auto_20200802_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq_post',
            name='subject',
            field=models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Mathematics', 'Mathematics'), ('Rhymes', 'Rhymes'), ('English Literature Book1', 'English Literature Book1'), ('English Literature Book2', 'English Literature Book2'), ('English Grammar', 'English Grammar'), ('Hindi Literature', 'Hindi Literature'), ('Hindi Grammar', 'Hindi Grammar'), ('Science', 'Science'), ('Computer', 'Computer'), ('Social Studies', 'Social Studies'), ('History', 'History'), ('Civics', 'Civics'), ('Geography', 'Geography'), ('Political Science', 'Political Science'), ('Economics', 'Economics'), ('Physical Education', 'Physical Education'), ('Computer Science', 'Computer Science'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Accountancy', 'Accountancy'), ('Business Studies', 'Business Studies'), ('Psychology', 'Psychology'), ('Hindi-Exam', 'Hindi-Exam'), ('Psychology-Exam', 'Psychology-Exam'), ('Computer Science-Exam', 'Computer Science-Exam'), ('Physical Education-Exam', 'Physical Education-Exam')], max_length=255),
        ),
    ]
