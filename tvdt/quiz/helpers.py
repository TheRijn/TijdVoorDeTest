import random
import string


def generate_season_code(length: int = 5) -> str:
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )
