import csv
import re
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class schools_test(unittest.TestCase):
    @classmethod
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report_S()


    def test_validate_schoolrecords(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.SARD1).click()
        self.driver.find_element_by_xpath(Data.SARB1).click()
        self.driver.find_element_by_xpath(Data.SARC3).click()
        time.sleep(10)
        # self.driver.find_element_by_xpath(Data.Download).click()
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)-1
        schools = self.driver.find_element_by_xpath(Data.no_schools).text
        str =schools
        res = re.sub("\D", "", str)
        self.assertEqual(count,int(res),"unmatching count found")

    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()