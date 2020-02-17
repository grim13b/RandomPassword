import secrets
import string


class Password:

    @staticmethod
    def generate(size=12, characters=string.ascii_letters+string.digits+string.punctuation):
        return ''.join(secrets.choice(characters) for _ in range(size))
