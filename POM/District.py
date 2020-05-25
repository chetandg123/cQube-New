import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd

dri = pwd()
class Districts(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report()

    def test_click_on_districtnames(self):
        time.sleep(5)
        driver = cqube(self.driver)
        driver.dots_dist()
        driver.Click_HomeButton()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
