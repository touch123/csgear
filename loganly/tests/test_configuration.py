from unittest import TestCase

from LogSpider import Configuration


class TestFinder(TestCase):
    def setUp(self):
        Configuration.load("./LogSpider/debug.yml")

    def tearDown(self):
        pass

    def test_n_load(self):
        Configuration.load("./LogSpider/debug.yml")

    def test_e_load(self):
        self.assertFalse(Configuration.load())
        self.assertFalse(Configuration.load(""))
        self.assertFalse(Configuration.load(None))

    def test_n_get_re(self):
        self.assertIsInstance(Configuration.get_re("postran"),dict)

    def test_e_get_re(self):
        self.assertIsInstance(Configuration.get_re("xxxxx"),dict)

    def test_n_self_check(self):
        self.assertTrue(Configuration.self_check())

    def test_e_self_check(self):
        Configuration.load("")
        self.assertTrue(Configuration.self_check())

