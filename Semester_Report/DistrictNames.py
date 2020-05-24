import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.parameters import Data
from TS.reuse_func import cqube


class Semester_Home(unittest.TestCase):
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_semester_report()

    def test_Distnames(self):
        time.sleep(5)
        self.driver.find_elements_by_xpath(Data.SRD32).click()
        driver =cqube(self.driver)
        driver.dots_dist()

    def tearDown(self):
        time.sleep()
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()