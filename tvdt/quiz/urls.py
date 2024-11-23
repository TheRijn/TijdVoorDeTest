from django.urls import path, register_converter

from .converters import CandidateConverter, SeasonCodeConverter
from .views import SelectSeasonView
from .views.questionview import QuestionView
from .views.enternameview import EnterNameView

register_converter(SeasonCodeConverter, "season")
register_converter(CandidateConverter, "candidate")
urlpatterns = [
    path("", SelectSeasonView.as_view(), name="home"),
    path("<season:season>/", EnterNameView.as_view(), name="quiz"),
    path("<candidate:candidate>/", QuestionView.as_view(), name="question"),
]
