import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class SAR(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()

    def test_click_schools(self):
        driver = cqube(self.driver)
        driver.navigate_to_student_report()
        self.driver.find_element_by_xpath(Data.Schools).click()
        time.sleep(30)
        list = self.driver.find_elements_by_class_name(Data.dots)
        self.assertNotEqual(0, int(len(list) - 1), msg='Failed')

    def tearDown(self):
        self.driver.close()
