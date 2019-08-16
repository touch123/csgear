# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase

from LogSpider import Configuration
from LogSpider import Spider
import datetime


class TestSpider(TestCase):
    def test_n_spider(self):
        Configuration.load("./LogSpider/debug.yml")
        self.assertTrue(Spider.spider(file_date="20170221",log_type=["postran"]))

    @unittest.skip("在全量测试时不成功,因Configuration有值.")
    def test_e_spider(self):
        self.assertFalse(Spider.spider(file_date="20170221",log_type=["xxx"]))

    def test_n_getdate(self):
        self.assertIsInstance(Spider.getdate(1),str)

    def test_e_getdate(self):
        self.assertIsInstance(Spider.getdate(),str)
        self.assertIsInstance(Spider.getdate(None),str)
        self.assertIsInstance(Spider.getdate(""),str)

