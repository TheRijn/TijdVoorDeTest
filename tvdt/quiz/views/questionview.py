from django.contrib import messages
from django.core.exceptions import BadRequest
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from ..models import Answer, Candidate, GivenAnswer
from ..models.question import NoActiveTestForSeason, QuizAlreadyFinished


class QuestionView(View, TemplateResponseMixin):
    template_name = "quiz/question.html"

    def get(
        self, request: HttpRequest, candidate: Candidate, *args, **kwargs
    ) -> HttpResponse:
        try:
            question = candidate.get_next_question(candidate)
        except NoActiveTestForSeason:
            messages.error(request, _("No active quiz for season"))
            return redirect("home")
        except QuizAlreadyFinished:
            if not kwargs.get("from_post"):
                messages.error(request, _("Quiz done"))

            return redirect(reverse("enter_name", kwargs={"season": candidate.season}))

        # TODO: On first question -> record time
        if (
            GivenAnswer.objects.filter(
                candidate=candidate, quiz=candidate.season.active_quiz
            ).count()
            == 0
        ):
            GivenAnswer.objects.create(
                candidate=candidate, quiz=question.quiz, answer=None
            )

        return self.render_to_response({"candidate": candidate, "question": question})

    def post(self, request: HttpRequest, candidate: Candidate, *args, **kwargs):
        answer_id = request.POST.get("answer")
        if answer_id == None:
            raise BadRequest

        try:
            answer = Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            raise BadRequest

        GivenAnswer.objects.create(
            candidate=candidate,
            quiz=answer.question.quiz,
            answer=answer,
        )
        return self.get(request, candidate, from_post=True)
