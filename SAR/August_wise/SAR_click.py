import time
import unittest

from selenium import webdriver
from Data.parameters import Data
from TS.reuse_func import cqube
class SAROption(unittest.TestCase):

    @classmethod
    def setUp(self):
        dri = Data()
        # self.driver = webdriver.Chrome(dri.get_driver_path())
        self.driver = webdriver.Chrome(Data.path)
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report()


    def test_SAR(self):
        driver = cqube(self.driver)
        driver.blocks_names()
        time.sleep(5)
        driver.clusters_names()
        time.sleep(5)
        driver.schools_test()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()