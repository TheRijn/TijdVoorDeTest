from django.contrib import messages
from django.core.exceptions import BadRequest
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View

from ..models import Candidate, Answer, GivenAnswer
from ..models.question import NoActiveTestForSeason


class QuestionView(View):
    template_name = "quiz/question.html"

    def get(
        self, request: HttpRequest, candidate: Candidate, *args, **kwargs
    ) -> HttpResponse:
        try:
            question = candidate.get_next_question(candidate)
        except NoActiveTestForSeason:
            messages.error(request, _("No active Quiz for season"))
            raise Http404("No active Quiz for seaon")

        return render(
            request,
            "quiz/question.html",
            {"candidate": candidate, "question": question},
        )

    def post(self, request: HttpRequest, candidate: Candidate, *args, **kwargs):
        answer_id = request.POST.get("answer")
        if answer_id == None:
            raise BadRequest

        try:
            answer = Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            raise BadRequest

        GivenAnswer.objects.create(
            candidate=candidate, question=answer.question, answer=answer
        )

        return self.get(request, candidate, args, kwargs)
