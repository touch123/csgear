from unittest import TestCase

from LogSpider import Configuration
from LogSpider import Library


class TestLibrary(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_n_ID(self):
        self.assertIsInstance(Library.ID("[32322- (2342)]"),str)

    def test_e_ID(self):
        self.assertIsNone(Library.ID("xxxx"))

    def test_n_message_head(self):
        self.assertIsInstance(Library.message_head("01: "),str)

    def test_e_message_head(self):
        self.assertFalse(Library.message_head("xxxx"))

    def test_n_message_tail(self):
        self.assertIsInstance(Library.message_tail(" [xxx]"),str)

    def test_e_message_tail(self):
        self.assertFalse(Library.message_tail("xxxx"))

    def test_n_get_num(self):
        self.assertIsInstance(Library.get_num("  234 234 234 234 234"),str)

    def test_e_get_num(self):
        self.assertIsNone(Library.get_num("xxxx"))

    def test_n_key_words_marching(self):
        Configuration.load("./LogSpider/debug.yml")
        self.assertTrue(Library.key_words_marching("Rrn"))

    def test_e_key_words_marching(self):
        Configuration.load("./LogSpider/debug.yml")
        self.assertFalse(Library.key_words_marching("xxx"))

    def test_n_DIYSearch(self):
        self.assertTrue(Library.DIYSearch("(.*)","aaa"))

    def test_e_DIYSearch(self):
        self.assertIsNone(Library.DIYSearch(".*","aaa"))
        self.assertIsNone(Library.DIYSearch("\d.*","ccc"))

    def test_n_FileName(self):
        self.assertTrue(Library.FileName("postran.20170101"))

    def test_e_FileName(self):
        self.assertIsNone(Library.FileName("70101223"))

    def test_n_FileDate(self):
        self.assertTrue(Library.FileDate("postran.20170101"))

    def test_e_FileDate(self):
        self.assertIsNone(Library.FileDate("aaaaaa"))
