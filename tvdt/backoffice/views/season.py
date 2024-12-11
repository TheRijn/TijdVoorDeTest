from django.http import HttpRequest
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from quiz.models import Season


class SeasonView(View, TemplateResponseMixin):
    template_name = "backoffice/season.html"

    def get(self, request: HttpRequest, season: Season, *args, **kwargs):
        return self.render_to_response({"season": season})
