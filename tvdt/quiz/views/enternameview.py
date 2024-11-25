from crispy_forms.helper import FormHelper
from django import forms
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from ..models import Candidate, Season


class EnterNameForm(forms.Form):
    name = forms.CharField(label=_("Name"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class EnterNameView(View, TemplateResponseMixin):
    template_name = "quiz/enter_name.html"
    forms_class = EnterNameForm

    def get(self, request, season: Season, *args, **kwargs):
        if season.active_quiz == None:
            messages.info(request, _("This season has no active quiz."))
            return redirect("home")

        return self.render_to_response({"form": self.forms_class()})

    def post(self, request, season: Season, *args, **kwargs):
        name = request.POST.get("name")

        try:
            candidate = Candidate.objects.get(season=season, name__iexact=name)
        except Candidate.DoesNotExist:
            if season.preregister_candidates:
                messages.warning(request, _("Candidate does not exist"))

                return redirect(reverse("quiz", kwargs={"season": season}))

            candidate = Candidate.objects.create(season=season, name=name)

        return redirect(
            reverse(
                "question",
                kwargs={"candidate": candidate},
            )
        )
