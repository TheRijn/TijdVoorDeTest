from django.db import models
from django.db.models import F, OuterRef, Subquery
from django.db.models.aggregates import Count, Max, Min
from django.db.models.functions import Coalesce
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta

from quiz.models import Candidate, Correction


class Quiz(models.Model):
    name = models.CharField(max_length=64, verbose_name=_("name"))
    season = models.ForeignKey(
        "Season",
        on_delete=models.CASCADE,
        related_name="quizzes",
        verbose_name=_("season"),
    )

    dropouts = models.PositiveSmallIntegerField(
        verbose_name=_("dropouts"),
        default=1,
    )

    def is_valid_quiz(self) -> bool:
        return True
        # Check > 0 active questions
        # Check every question 1 right answer

    def get_score(self):
        time_query = (
            Candidate.objects.filter(id=OuterRef("id"), answers__quiz=self)
            .annotate(time=Max("answers__created") - Min("answers__created"))
            .values("time")
        )
        corrections = Correction.objects.filter(
            quiz=self, candidate=OuterRef("id")
        ).values("amount")

        scores = (
            Candidate.objects.filter(
                answers__answer__is_right_answer=True,
                answers__quiz=self,
            )
            .values("id", "name")
            .annotate(
                correct=Count("answers"),
                corrections=Coalesce(Subquery(corrections), 0.0),
                score=F("correct") + F("corrections"),
                time=Subquery(time_query),
            )
            .order_by("-score", "time")
        )
        return scores

    def __str__(self) -> str:
        return f"{self.season.name} - {self.name}"

    class Meta(TypedModelMeta):
        verbose_name = _("quiz")
        verbose_name_plural = _("quizzes")
