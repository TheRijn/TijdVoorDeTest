from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta


class Quiz(models.Model):
    name = models.CharField(max_length=64, verbose_name=_("name"))
    season = models.ForeignKey(
        "Season",
        on_delete=models.CASCADE,
        related_name="quizzes",
        verbose_name=_("season"),
    )

    def is_valid_quiz(self) -> bool:
        pass
        # Check > 0 active questions
        # Check every question 1 right answer

    def __str__(self) -> str:
        return f"{self.season.name} - {self.name}"

    class Meta(TypedModelMeta):
        verbose_name = _("quiz")
        verbose_name_plural = _("quizzes")
