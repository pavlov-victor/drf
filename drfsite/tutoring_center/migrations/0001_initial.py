# Generated by Django 5.0.3 on 2024-03-18 09:21

import tutoring_center.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('user_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('student_id', models.UUIDField()),
                ('tutor_id', models.UUIDField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('theme', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('small_preview', models.ImageField(upload_to='')),
                ('preview', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='', verbose_name=tutoring_center.models.File)),
            ],
        ),
        migrations.CreateModel(
            name='Registragtion_for_service',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('tutor_id', models.UUIDField()),
                ('student_id', models.UUIDField()),
                ('service_id', models.UUIDField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('theme_of_lesson', models.CharField(max_length=30)),
                ('additional_info', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('free', 'free'), ('busy', 'busy'), ('confirmed', 'confirmed'), ('completed', 'completed')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('tutor_id', models.UUIDField()),
                ('subject', models.CharField(max_length=30)),
                ('info_about_service', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('level', models.CharField(choices=[('preschooler', 'preschooler'), ('schooler', 'schooler'), ('student', 'student'), ('other', 'other')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('user_id', models.UUIDField()),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('email', models.CharField(max_length=30)),
                ('grade', models.CharField(max_length=100)),
                ('parents_fio', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('user_id', models.UUIDField()),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('education', models.CharField(max_length=100)),
                ('services', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
