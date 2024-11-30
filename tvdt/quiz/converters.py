import base64
import binascii

from .models import Candidate, Season


class CandidateConverter:
    regex = r"[A-Za-z\d]{5}\/[\w\-=]+"

    def to_python(self, value: str) -> Candidate:
        season_code, base64_name = value.split("/")

        try:
            name = base64.urlsafe_b64decode(base64_name).decode()
        except binascii.Error:
            raise ValueError

        try:
            season = Season.objects.aget(season_code=season_code)

            candidate = Candidate.objects.get(name=name, season=season)
            return candidate
        except [Season.DoesNotExist, Candidate.DoesNotExist]:
            raise ValueError

    def to_url(self, candidate: Candidate) -> str:
        base64_candidate = base64.urlsafe_b64encode(candidate.name.encode()).decode()
        return f"{candidate.season.season_code}/{base64_candidate}"
