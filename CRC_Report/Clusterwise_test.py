import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube


class Gothva_cluster(unittest.TestCase):
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()

    def test_crcclick(self):
        time.sleep(25)
        dist = self.driver.find_element_by_xpath(Data.CRD18).click()

        blk = self.driver.find_element_by_xpath(Data.CRB2).click()

        clu = self.driver.find_element_by_xpath(Data.CRC2).click()

        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Download).click()
        time.sleep(5)
        count = self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[2]/span").text
        self.assertNotEqual(0,count,"mis match found")



    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()