from unittest import TestCase
# Create your tests here.
from .models import lookup


class TestLookup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def test_environ(self):
        matches = lookup('environ')
        assert matches

    @classmethod
    def tearDownClass(cls) -> None:
        pass
