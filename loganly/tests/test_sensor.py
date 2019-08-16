# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase

from LogSpider import Sensor
from LogSpider import Configuration


class TestFinder(TestCase):
    """
        test_n  开头为正常测试
        test_e 开头为异常测试
        test_p 开头为性能测试

    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_n_sensor(self):
        Configuration.load("./LogSpider/debug.yml")
        Sensor.sensor()

    @unittest.skip("在全量测试时不成功,因Configuration有值.")
    def test_e_sensor(self):
        Configuration.load("")
	print(Configuration.db_path)
        self.assertFalse(Sensor.sensor())

    def test_n_file_names(self):
        Configuration.load("./LogSpider/debug.yml")
	result = Sensor.file_names(user_dir='/home/vagrant/shop/log')
	self.assertIsInstance(result,list,"返回值是否为列表")

    def test_e_file_names(self):
	result = Sensor.file_names(user_dir=None)
	self.assertIsInstance(result,list,"返回值是否为列表")
	

