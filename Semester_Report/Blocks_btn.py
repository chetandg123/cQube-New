
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class School_click(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_semester_report()

    def test_click_on_blocks(self):
        self.driver.find_elements_by_xpath(Data.Blocks).click()
        time.sleep(10)
        driver = cqube(self.driver)
        driver.Details_text()
        time.sleep(10)
        driver.ClickOn_HomeButton()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

