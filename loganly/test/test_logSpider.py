from unittest import TestCase

import Configuration
from LogSpider import LogSpider


class TestLogSpider(TestCase):
    def test_LogSpider(self):
        Configuration.init()
        LogSpider(logType=Configuration.logType)
