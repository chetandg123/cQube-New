import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube


class Patan_cluster(unittest.TestCase):
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_crc_report()

    def test_crcclick(self):
        time.sleep(25)
        dist = self.driver.find_element_by_xpath(Data.CRD24).click()

        blk = self.driver.find_element_by_xpath(Data.CRB8).click()

        self.driver.find_element_by_xpath(Data.CRC3).click()

        self.driver.find_element_by_xpath(Data.Download).click()
        time.sleep(5)
        tabledata = self.driver.find_elements_by_xpath(Data.distrows)
        for i in range(len(tabledata)):
            print(tabledata[i].text)
        footer = self.driver.find_elements_by_xpath(Data.footer)
        for i in range(len(footer)):
            print(footer[i].text)
            time.sleep(5)


    def tearDown(self):

            self.driver.close()

    if __name__ == "__main__":
        unittest.main()