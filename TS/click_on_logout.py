import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class CqubeLogin(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()

    def test_logout(self):
        self.driver.find_element_by_xpath(Data.Log_out).click()

    def tearDown(self):
        self.driver.close()
