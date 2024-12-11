from django.urls import path, register_converter

from tvdt.converters import SeasonCodeConverter

from .converters import CandidateConverter
from .views import SelectSeasonView
from .views.enternameview import EnterNameView
from .views.questionview import QuestionView

register_converter(SeasonCodeConverter, "season")
register_converter(CandidateConverter, "candidate")
urlpatterns = [
    path("", SelectSeasonView.as_view(), name="index"),
    path("<season:season>/", EnterNameView.as_view(), name="enter_name"),
    path("<candidate:candidate>/", QuestionView.as_view(), name="question"),
    # path("<>")
]
