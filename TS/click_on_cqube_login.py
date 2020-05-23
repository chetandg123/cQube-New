import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Data.parameters import Data
from TS.reuse_func import cqube


class CqubeLogin(unittest.TestCase):
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()

    def test_search(self):
        driver = cqube(self.driver)
        driver.login_cqube()

    def tearDown(self):
        self.driver.close()
