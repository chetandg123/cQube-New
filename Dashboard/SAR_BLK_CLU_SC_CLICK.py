import time
import unittest


from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class SAROption(unittest.TestCase):

    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()

    def test_SAR(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SAR).click()
        self.driver.find_element_by_xpath(Data.SAR_Blocks_btn).click()
        time.sleep(15)
        driver = cqube(self.driver)
        driver.Details_text()
        self.driver.find_element_by_xpath(Data.SAR_Clusters_btn).click()
        time.sleep(15)
        driver.Details_text()
        self.driver.find_element_by_xpath(Data.SAR_Schools_btn).click()
        time.sleep(30)
        driver.Details_text()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()