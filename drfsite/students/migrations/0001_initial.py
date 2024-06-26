# Generated by Django 5.0.3 on 2024-05-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(default="", max_length=20, verbose_name="Имя"),
                ),
                (
                    "last_name",
                    models.CharField(default="", max_length=20, verbose_name="Фамилия"),
                ),
                (
                    "middle_name",
                    models.CharField(
                        default="", max_length=20, verbose_name="Отчество"
                    ),
                ),
                (
                    "birthday",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        default="", max_length=30, verbose_name="Электронная почта"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        default="", max_length=15, verbose_name="Номер телефона"
                    ),
                ),
                (
                    "grade",
                    models.CharField(
                        choices=[
                            ("PRESCHOOLER", "Дошкольники"),
                            ("SCHOLAR", "Школьники"),
                            ("STUDENT", "Студенты"),
                            ("OTHER", "Другие"),
                        ],
                        default="OTHER",
                        max_length=15,
                        verbose_name="Уровень образования",
                    ),
                ),
                (
                    "parent_fio",
                    models.CharField(
                        default="", max_length=100, verbose_name="ФИО родителя"
                    ),
                ),
                (
                    "parent_phone",
                    models.CharField(
                        default="",
                        max_length=15,
                        verbose_name="Номер телефона родителя",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ученик",
                "verbose_name_plural": "Ученики",
            },
        ),
    ]
