from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta

from ..helpers import generate_season_code

User = get_user_model()


class Season(models.Model):
    name = models.CharField(max_length=64, verbose_name=_("name"))
    active_quiz = models.ForeignKey(
        "Quiz",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        verbose_name=_("active quiz"),
        related_name="+",
    )
    season_code = models.CharField(
        max_length=5, default=generate_season_code, verbose_name=_("season code")
    )
    preregister_candidates = models.BooleanField(
        default=True, verbose_name=_("preregister candidates")
    )
    owner = models.ManyToManyField(
        User,
        verbose_name=_("owners"),
        related_name="seasons",
    )

    def renew_season_code(self) -> str:
        self.season_code = generate_season_code()
        self.save()
        return self.season_code

    def __str__(self) -> str:
        return self.name

    class Meta(TypedModelMeta):
        verbose_name = _("season")
        verbose_name_plural = _("seasons")
