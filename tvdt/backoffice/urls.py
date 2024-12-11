from django.contrib.auth.decorators import login_required
from django.urls import path, register_converter

from tvdt.converters import SeasonCodeConverter

from .converters import QuizConverter
from .views import BackofficeIndexView, QuizView, SeasonView

register_converter(SeasonCodeConverter, "season")
register_converter(QuizConverter, "quiz")

app_name = "backoffice"
urlpatterns = [
    path("", login_required(BackofficeIndexView.as_view()), name="index"),
    path(
        "<season:season>/",
        login_required(SeasonView.as_view()),
        name="season",
    ),
    path("<quiz:quiz>/", login_required(QuizView.as_view()), name="quiz"),
]
