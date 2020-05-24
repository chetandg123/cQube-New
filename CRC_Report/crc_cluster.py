import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube


class cluster_test(unittest.TestCase):
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_crc_report()

    def test_crcclick(self):
        time.sleep(30)
        dist = self.driver.find_element_by_xpath(Data.CRD17).click()
        disttxt = self.driver.find_element_by_xpath(Data.CRD17).text
        time.sleep(5)
        blk = self.driver.find_element_by_xpath().click()
        block = self.driver.find_element_by_xpath(Data.CRB7).text
        time.sleep(5)

        self.driver.find_element_by_xpath(Data.CRC2).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Download).click()
        time.sleep(5)
        count = self.driver.find_element_by_xpath(Data.no_schools).text

        self.assertNotEqual(0,count, "unmatching count found")


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()