from unittest import TestCase

from LogSpider import Configuration
from LogSpider import Spider


class TestSpider(TestCase):
    def test_LogSpider(self):
	
        Configuration.load("./LogSpider/debug.yml")
        #Spider.spider(file_date="20170221",log_type=Configuration.logType)
        Spider.spider(file_date="20170221",log_type=["postran"])
