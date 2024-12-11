from quiz.models import Quiz


class QuizConverter:
    regex = r"\d+"

    def to_python(self, value: str) -> Quiz:
        try:
            return Quiz.objects.get(id=value)
        except Quiz.DoesNotExist:
            raise ValueError

    def to_url(self, value: Quiz | int) -> str:
        return str(value.id) if isinstance(value, Quiz) else value
