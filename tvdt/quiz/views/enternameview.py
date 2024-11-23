from crispy_forms.helper import FormHelper
from django import forms
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from ..models import Season, Candidate


class EnterNameForm(forms.Form):
    name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class EnterNameView(View):
    template_name = "quiz/enter_name.html"
    forms_class = EnterNameForm

    def get(self, request, season: Season, *args, **kwargs):
        if season.active_quiz == None:
            raise Http404("No quiz active")

        return render(
            request,
            self.template_name,
            {"form": self.forms_class(), "season": season},
        )

    def post(self, request, season: Season, *args, **kwargs):
        name = request.POST.get("name")

        if season.preregister_candidates:
            try:
                candidate = Candidate.objects.get(season=season, name=name)
            except Candidate.DoesNotExist:
                raise Http404("Candidate not found")
        else:
            candidate, created = Candidate.objects.get_or_create(
                season=season, name=name
            )

        return redirect(
            reverse(
                "question",
                kwargs={"candidate": candidate},
            )
        )
