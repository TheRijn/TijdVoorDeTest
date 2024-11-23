from crispy_forms.helper import FormHelper
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django import forms

from ..models import Season


class SelectSeasonForm(forms.Form):
    code = forms.CharField(max_length=5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class SelectSeasonView(FormView):
    form_class = SelectSeasonForm
    template_name = "quiz/select_season.html"

    def form_valid(self, form):
        try:
            season = Season.objects.get(season_code=form.cleaned_data["code"].upper())
        except Season.DoesNotExist:
            raise Http404("Season does not exist")

        return redirect(reverse("quiz", kwargs={"season": season}))
