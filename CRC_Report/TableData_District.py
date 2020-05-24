import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube


class Crc_Reports(unittest.TestCase):
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_crc_report()

    def test_crcclick(self):
        time.sleep(30)
        headers = self.driver.find_elements_by_xpath(Data.headers)
        for i in range(len(headers)):
            print(headers[i].text)
            time.sleep(3)
        rows = self.driver.find_elements_by_xpath(Data.distrows)
        for j in range(len(rows)):
            print(rows[j].text)
            time.sleep(3)
    def tearDown(self):
            footer = self.driver.find_elements_by_xpath(Data.footer)
            for i in range(len(footer)):
                print(footer[i].text)
            time.sleep(5)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()