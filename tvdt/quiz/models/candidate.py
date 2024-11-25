from typing import Self

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta

from .given_answer import GivenAnswer
from .question import NoActiveTestForSeason, Question, QuizAlreadyFinished


class Candidate(models.Model):
    season = models.ForeignKey(
        "Season",
        on_delete=models.CASCADE,
        related_name="candidates",
        verbose_name="season",
    )
    name = models.CharField(max_length=16, verbose_name=_("name"))

    def get_next_question(self, candidate: Self) -> "Question":
        quiz = candidate.season.active_quiz
        if quiz is None:
            raise NoActiveTestForSeason()

        question = (
            Question.objects.filter(quiz=quiz, enabled=True)
            .exclude(
                id__in=GivenAnswer.objects.filter(
                    candidate=candidate,
                    quiz=quiz,
                    answer__isnull=False,
                ).values_list("answer__question_id", flat=True)
            )
            .first()
        )

        if question is None:
            raise QuizAlreadyFinished()

        return question

    def __str__(self) -> str:
        return f"{self.name} ({self.season})"

    class Meta(TypedModelMeta):
        unique_together = ["season", "name"]
        indexes = [models.Index(fields=["season", "name"])]

        verbose_name = _("candidate")
        verbose_name_plural = _("candidates")
