import time
import unittest

from selenium import webdriver

from Data.Paramters import Data

from TS.reuse_func import cqube


class Semester_click(unittest.TestCase):
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_semester_report()

    def test_semester(self):
        driver =cqube(self.driver)
        driver.Details_text()
        time.sleep(5)
        driver.ClickOn_HomeButton()

    def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()