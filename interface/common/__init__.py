import unittest
import requests
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import BaseConfig
from db_fixture import test_data


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.host = BaseConfig.host

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        """
        post请求
        """
        r = requests.post(url, data, json, **kwargs)
        return r

    @staticmethod
    def get(url, params=None, **kwargs):
        """
        get请求
        """
        r = requests.get(url, params, **kwargs)
        return r


def run() -> None:
    """初始化数据，运行测试"""
    test_data.init_data()
    unittest.main()
