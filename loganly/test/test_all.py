from unittest import TestCase
import Finder
import Spider


class TestAll(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_All(self):
        Finder.Finder({'logType': 'mis_clt', 'FileDate': '20190116', 'TraceNo': '540002'})

