import time
import unittest

from  selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Crc_Reports(unittest.TestCase):
    def setUp(self):
        path_exe = pwd()
        self.driver = webdriver.Chrome(path_exe.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_crc_report()

    def test_crcclick(self):
        time.sleep(35)
        self.driver.find_element_by_xpath(Data.CRD13).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.CRB5).click()
        time.sleep(10)

        headers = self.driver.find_elements_by_xpath(Data.headers)
        for i in range(len(headers)):
            print(headers[i].text)
            time.sleep(3)

        rows = self.driver.find_elements_by_xpath(Data.distrows)
        for j in range(len(rows)):
            print(rows[i].text)
            time.sleep(5)
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.crc).click()
        time.sleep(30)

    def tearDown(self):
            time.sleep(5)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()