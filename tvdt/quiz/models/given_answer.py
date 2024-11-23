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
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        null=True,
        related_name="given_answers",
        verbose_name=_("question"),
    )
    answer = models.ForeignKey(
        "Answer", on_delete=models.CASCADE, verbose_name=_("answer")
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta(TypedModelMeta):
        unique_together = ["candidate", "question"]

        verbose_name = _("given answer")
        verbose_name_plural = _("given answers")
