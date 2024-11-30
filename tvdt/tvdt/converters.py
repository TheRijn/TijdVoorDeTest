from quiz.models import Season


class SeasonCodeConverter:
    regex = r"[A-Za-z\d]{5}"

    def to_python(self, value: str) -> Season:
        try:
            return Season.objects.get(season_code=value.upper())
        except Season.DoesNotExist:
            raise ValueError

    def to_url(self, value: Season) -> str:
        return value.season_code
