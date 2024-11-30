from django.urls import path, register_converter

from tvdt.converters import SeasonCodeConverter

from .views import EliminationHomeView

register_converter(SeasonCodeConverter, "season")
urlpatterns = [
    path("", EliminationHomeView.as_view()),
    path("<season:season>", EliminationHomeView.as_view()),
]
