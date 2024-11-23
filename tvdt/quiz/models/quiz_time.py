from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta


class QuizTime(models.Model):
    candidate = models.ForeignKey(
        "Candidate", on_delete=models.CASCADE, verbose_name=_("candidate")
    )
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, verbose_name=_("quiz"))
    seconds = models.PositiveIntegerField(verbose_name=_("seconds"))

    class Meta(TypedModelMeta):
        verbose_name = _("quiz time")
        verbose_name_plural = _("quiz times")
