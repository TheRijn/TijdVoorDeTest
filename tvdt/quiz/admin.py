from django.contrib import admin

from .models import Answer, Candidate, Correction, GivenAnswer, Question, Quiz, Season


class CandidatesAdmin(admin.StackedInline):
    model = Candidate
    extra = 1


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    inlines = [CandidatesAdmin]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question", "quiz__season__name", "quiz__name", "_order"]
    ordering = ["quiz__season", "quiz", "_order"]
    inlines = [AnswerInline]


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(GivenAnswer)
class GivenAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Correction)
class CorrextionAdmin(admin.ModelAdmin):
    pass
