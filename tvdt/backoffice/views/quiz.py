from django.http import HttpRequest
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from quiz.models import Quiz


class QuizView(View, TemplateResponseMixin):
    template_name = "backoffice/quiz.html"

    def get(self, request: HttpRequest, quiz: Quiz, *args, **kwargs):

        return self.render_to_response({"quiz": quiz})
