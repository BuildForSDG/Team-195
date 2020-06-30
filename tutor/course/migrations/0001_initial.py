<<<<<<< HEAD
# Generated by Django 3.0.5 on 2020-06-13 19:40
=======
# Generated by Django 3.0.5 on 2020-06-23 22:18
>>>>>>> d704842c96df6235167466558355fc31c5c3ba93

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(max_length=15, unique=True)),
=======
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=50)),
                ('content', models.FileField(blank=True, upload_to='')),
>>>>>>> d704842c96df6235167466558355fc31c5c3ba93
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
<<<<<<< HEAD
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Grade')),
                ('student', models.ManyToManyField(to='student.Students')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tutors')),
=======
>>>>>>> d704842c96df6235167466558355fc31c5c3ba93
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=50)),
                ('content', models.FileField(blank=True, upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
    ]
