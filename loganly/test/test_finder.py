from unittest import TestCase
import Finder


class TestFinder(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Finder(self):
        Finder.Finder({'logType': 'mis_clt', 'FileDate': '20190116', 'TraceNo': '540002'})

