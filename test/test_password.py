import string

from src.utilities import Password


class TestPassword:
    def test_generate_default(self):
        actual = Password.generate()
        assert len(actual) == 12
        assert actual.isascii()

    def test_generate_optional_column_22(self):
        actual = Password.generate(size=22)
        assert len(actual) == 22
        assert actual.isascii()

    def test_generate_optional_characters(self):
        actual = Password.generate(characters=string.ascii_letters)
        assert len(actual) == 12
        assert actual.isalpha()
