

import re
import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from  TS.reuse_func import cqube
from get_dir import pwd


class Dist_validation(unittest.TestCase):
    @classmethod
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report_O()


    def test_validate_District(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.SARD10).click()

        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Download).click()
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)
        print("no of dots:",count)
        time.sleep(20)
        with open("/home/chetan/Documents/Data_files/Block_per_district_report (4).csv", 'r') as file:
            reader = csv.reader(file)
            lines = len(list(reader))
            print("no of records in file:",lines)
        self.assertEqual(count,lines,"unmatching count found")
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()