# Generated by Django 5.1.2 on 2024-10-19 21:54

import django.db.models.deletion
import quiz.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Candidate",
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
                ("name", models.CharField(max_length=16, verbose_name="naam")),
            ],
            options={
                "verbose_name": "candidate",
                "verbose_name_plural": "candidates",
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                ("question", models.CharField(max_length=256, verbose_name="question")),
                ("number", models.PositiveSmallIntegerField(verbose_name="number")),
                ("enabled", models.BooleanField(default=True, verbose_name="enabled")),
            ],
            options={
                "verbose_name": "question",
                "verbose_name_plural": "questions",
            },
        ),
        migrations.CreateModel(
            name="Quiz",
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
                ("name", models.CharField(max_length=64, verbose_name="naam")),
            ],
            options={
                "verbose_name": "quiz",
                "verbose_name_plural": "quizzes",
            },
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("text", models.CharField(max_length=64, verbose_name="text")),
                (
                    "is_right_answer",
                    models.BooleanField(verbose_name="is right answer"),
                ),
                (
                    "candidates",
                    models.ManyToManyField(
                        to="quiz.candidate", verbose_name="candidates"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="quiz.question",
                        verbose_name="question",
                    ),
                ),
            ],
            options={
                "verbose_name": "answer",
                "verbose_name_plural": "answers",
            },
        ),
        migrations.AddField(
            model_name="question",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="quiz.quiz",
                verbose_name="quiz",
            ),
        ),
        migrations.CreateModel(
            name="QuizTime",
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
                ("seconds", models.PositiveIntegerField(verbose_name="seconds")),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quiz.candidate",
                        verbose_name="candidate",
                    ),
                ),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quiz.quiz",
                        verbose_name="quiz",
                    ),
                ),
            ],
            options={
                "verbose_name": "quiz time",
                "verbose_name_plural": "quiz times",
            },
        ),
        migrations.CreateModel(
            name="Season",
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
                ("name", models.CharField(max_length=64, verbose_name="naam")),
                (
                    "season_code",
                    models.CharField(
                        default=quiz.helpers.generate_season_code,
                        max_length=5,
                        verbose_name="season code",
                    ),
                ),
                (
                    "active_quiz",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="quiz.quiz",
                        verbose_name="active quiz",
                    ),
                ),
            ],
            options={
                "verbose_name": "season",
                "verbose_name_plural": "seasons",
            },
        ),
        migrations.AddField(
            model_name="quiz",
            name="season",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quizzes",
                to="quiz.season",
                verbose_name="season",
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="season",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="candidates",
                to="quiz.season",
                verbose_name="season",
            ),
        ),
        migrations.CreateModel(
            name="GivenAnswer",
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
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quiz.answer",
                        verbose_name="answer",
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="quiz.candidate",
                        verbose_name="candidate",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="given_answers",
                        to="quiz.question",
                        verbose_name="question",
                    ),
                ),
            ],
            options={
                "verbose_name": "given answer",
                "verbose_name_plural": "given answers",
                "unique_together": {("candidate", "question")},
            },
        ),
        migrations.AlterUniqueTogether(
            name="question",
            unique_together={("quiz", "number")},
        ),
        migrations.CreateModel(
            name="Correction",
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
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="corrections_used",
                        to="quiz.candidate",
                        verbose_name="candidate",
                    ),
                ),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="corrections_used",
                        to="quiz.quiz",
                        verbose_name="quiz",
                    ),
                ),
            ],
            options={
                "verbose_name": "correction",
                "verbose_name_plural": "corrections",
                "unique_together": {("candidate", "quiz")},
            },
        ),
        migrations.AddIndex(
            model_name="candidate",
            index=models.Index(
                fields=["season", "name"], name="quiz_candid_season__d83118_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="candidate",
            unique_together={("season", "name")},
        ),
    ]