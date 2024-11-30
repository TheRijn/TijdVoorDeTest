from django.views.generic import TemplateView


class EliminationHomeView(TemplateView):
    template_name = "elimination/home.html"
