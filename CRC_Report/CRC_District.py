import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube


class Sundalpur_cluster(unittest.TestCase):
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_crc_report()

    def test_crcclick(self):
        time.sleep(25)
        dist = self.driver.find_element_by_xpath(Data.CRD3).click()
        disttxt = self.driver.find_element_by_xpath(Data.CRD3).text
        print(disttxt)
        self.assertEqual(Data.value2,disttxt,"is not selected ")
        time.sleep(5)
        blk = self.driver.find_element_by_xpath(Data.CRB7).click()
        self.driver.find_element_by_xpath(Data.CRC5).click()
        self.driver.find_element_by_xpath(Data.Download).click()

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()