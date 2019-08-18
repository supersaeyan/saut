from unittest import TestCase

# from models import lookup
from models import clookup as lookup


class TestLookup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def test_environ(self):
        matches = lookup('environ')
        self.assertEqual(matches.sort(),
                         ["environ", "environm", "environs", "environme", "environet", "environics", "environews",
                          "environmen", "environment", "environement", "environments", "environmental", "environnement",
                          "dbenvironment", "newenvironment", "environmetrics", "environmentally", "microenvironment",
                          "environmentalism", "environmentalist", "geoenvironmental", "bioenvironmental",
                          "environnementale", "environnementaux", "environmentalists"].sort())

    def test_cosmo(self):
        matches = lookup('cosmo')
        self.assertEqual(matches.sort(),
                         ["cosmo", "cosmos", "cosmote", "cosmocom", "cosmogony", "cosmochim", "cosmogirl", "cosmonaut",
                          "cosmonazi", "cosmology", "cosmopolis", "cosmodrome", "cosmogenic", "cosmograph",
                          "cosmonauts", "cosmologies", "microcosmos", "cosmosworks", "cosmologist", "cosmological",
                          "cosmochimica", "cosmologists", "cosmopolitan", "cosmopolitans", "cosmopolitanism"].sort())

    def test_the(self):
        matches = lookup('the')
        self.assertEqual(matches.sort(),
                         ["the", "thew", "nthe", "they", "thee", "thep", "thea", "thel", "ithe", "theg", "ethe", "fthe",
                          "thef", "rthe", "thed", "them", "thec", "thex", "then", "sthe", "cthe", "ythe", "gthe",
                          "uthe", "mthe"].sort())

    @classmethod
    def tearDownClass(cls) -> None:
        pass
