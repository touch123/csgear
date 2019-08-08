from unittest import TestCase

from LogSpider import Configuration
from LogSpider import Spider


class TestSpider(TestCase):
    def test_LogSpider(self):
        Configuration.init()
        Spider(logType=Configuration.logType)
