import unittest
from unittest import TestCase

from LogSpider import DB


class TestDB(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("I don't want to run this case.")
    def test_init(self):
	print(1)
        DB.init()

    @unittest.skip("I don't want to run this case.")
    def test_skip(self):
        result = DB.skip('postran','20190101')
        self.assertNotEqual(len(result), 0)

    @unittest.skip("I don't want to run this case.")
    def test_sign(self):
	#self.skipTest('Do not run this case')
        DB.sign('20190101','postran')
	DB.delet_old_sign('postran', '20190101')

    @unittest.skip("I don't want to run this case.")
    def test_drop_table(self):
        DB.drop_table()

	
    def test_all(self):
	DB.getTable('T_postran')
