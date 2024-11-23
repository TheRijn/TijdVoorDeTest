from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta


class Answer(models.Model):
    text = models.CharField(max_length=64, verbose_name=_("text"))
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name=_("question"),
    )
    is_right_answer = models.BooleanField(verbose_name=_("is right answer"))
    candidates = models.ManyToManyField(
        "Candidate", verbose_name=_("candidates"), blank=True
    )

    class Meta(TypedModelMeta):
        verbose_name = _("answer")
        verbose_name_plural = _("answers")

        order_with_respect_to = "question"
