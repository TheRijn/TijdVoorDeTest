from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta

from quiz.models import Answer


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

    @property
    def order(self):
        return self._order

    @property
    def right_answer(self) -> QuerySet[Answer]:
        return self.answers.filter(is_right_answer=True)

    @property
    def has_right_answer(self) -> bool:
        return self.answers.filter(is_right_answer=True).count() > 0

    @property
    def errors(self) -> str | None:
        if self.answers.count() == 0:
            return _("Error: Question has no answers")

        n_correct_answers = self.answers.filter(is_right_answer=True).count()

        if n_correct_answers == 0:
            return _("Error: This question has no right answer!")

        if n_correct_answers > 1:
            return _("Warning: This question has multiple correct answers")

        return None

    def __str__(self) -> str:
        return f"{self._order + 1}. {self.question} ({self.quiz}) ({self.answers.count()} answers, {self.answers.filter(is_right_answer=True).count()} correct)"

    class Meta(TypedModelMeta):
        verbose_name = _("question")
        verbose_name_plural = _("questions")

        order_with_respect_to = "quiz"
