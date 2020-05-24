import re
import time
import unittest
#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.parameters import Data
from TS.reuse_func import cqube


class Blocks_button(unittest.TestCase):
    @classmethod
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report()

    def test_click_on_blocksbtn(self):
        self.driver.find_element_by_xpath(Data.Blocks).click()
        time.sleep(5)
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)
        self.assertNotEqual(0,count,msg="Failed")
        time.sleep(15)
        print(self.driver.find_element_by_xpath(Data.students).text)
        print(self.driver.find_element_by_xpath(Data.schoolcount).text)
        print(self.driver.find_element_by_xpath(Data.DateRange).text)

    def tearDown(self):
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
