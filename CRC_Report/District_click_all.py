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
        distnames = self.driver.find_elements_by_xpath(Data.crcdistrict)
        for i in range(len(distnames)):
            distnames[i].click()
            time.sleep(5)
            print(distnames[i].text)
    def tearDown(self):
            time.sleep(5)


    if __name__ == "__main__":
        unittest.main()