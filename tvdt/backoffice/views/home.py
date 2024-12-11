from django.http import HttpRequest
from django.views.generic import TemplateView


class BackofficeIndexView(TemplateView):
    template_name = "backoffice/index.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        seasons = request.user.seasons.all()
        return self.render_to_response({"seasons": seasons})
