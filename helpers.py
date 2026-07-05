import random
import string


def generate_random_string(length: int = 200) -> str:
    """Generate a random string of the given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
