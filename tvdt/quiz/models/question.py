from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta


class NoActiveTestForSeason(Exception):
    pass


class QuizAlreadyFinished(Exception):
    pass


class Question(models.Model):
    question = models.CharField(max_length=256, verbose_name=_("question"))
    quiz = models.ForeignKey(
        "Quiz",
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name=_("quiz"),
    )
    enabled = models.BooleanField(default=True, verbose_name=_("enabled"))

    def __str__(self) -> str:
        return f"{self._order + 1}. {self.question} ({self.quiz}) ({self.answers.count()} answers, {self.answers.filter(is_right_answer=True).count()} correct)"

    class Meta(TypedModelMeta):
        verbose_name = _("question")
        verbose_name_plural = _("questions")

        order_with_respect_to = "quiz"
