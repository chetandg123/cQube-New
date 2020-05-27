

import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Blocks_Wise_test(unittest.TestCase):
    @classmethod
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report_S()

    def test_validate_District(self):
        time.sleep(5)
        dist = self.driver.find_element_by_xpath(Data.SARD13).click()
        blk = self.driver.find_element_by_xpath(Data.SARB5).click()
        time.sleep(5)
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)
        self.assertNotEqual(0,count,msg="Failed")
        time.sleep(20)
        with open("/home/chetan/Documents/Data_files/Cluster_per_block_report (5).csv", 'r') as file:
            reader = csv.reader(file)
            lines = len(list(reader))
            print("no of records in file:",lines)
        self.assertEqual(count,lines,"unmatching count found")
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()