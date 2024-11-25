from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta


class GivenAnswer(models.Model):
    candidate = models.ForeignKey(
        "Candidate",
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name=_("candidate"),
    )

    quiz = models.ForeignKey(
        "Quiz",
        on_delete=models.CASCADE,
        null=False,
        related_name="+",
        verbose_name=_("quiz"),
    )

    answer = models.ForeignKey(
        "Answer",
        on_delete=models.CASCADE,
        verbose_name=_("answer"),
        null=True,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quiz} - {self.candidate.name} {self.answer}"

    class Meta(TypedModelMeta):
        ordering = ("quiz", "candidate")

        verbose_name = _("given answer")
        verbose_name_plural = _("given answers")
