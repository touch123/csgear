from unittest import TestCase

from LogSpider import Finder
from LogSpider import Configuration


class TestFinder(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Finder(self):
        Configuration.load("./LogSpider/debug.yml")
        Finder.finder({'logType': 'mis_clt', 'FileDate': '20190116', 'TraceNo': '540002'})

