from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta


class Correction(models.Model):
    candidate = models.ForeignKey(
        "Candidate",
        on_delete=models.CASCADE,
        related_name="corrections",
        verbose_name=_("candidate"),
    )
    quiz = models.ForeignKey(
        "Quiz",
        on_delete=models.CASCADE,
        related_name="corrections",
        verbose_name=_("quiz"),
    )
    amount = models.FloatField(verbose_name=_("amount"), default=1)

    class Meta(TypedModelMeta):
        unique_together = ("candidate", "quiz")
        verbose_name = _("correction")
        verbose_name_plural = _("corrections")
