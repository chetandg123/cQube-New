import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from get_dir import pwd


class test_cluster(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        self.driver.implicitly_wait(15)

    def test_url(self):
        self.driver.maximize_window()
        self.driver.get(Data.url)
        self.driver.find_element_by_xpath(Data.email).send_keys("devraj@gmail.com")
        self.driver.find_element_by_xpath(Data.pwd).send_keys("devraj123")
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.submit).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.Clusters).click()
        time.sleep(15)
        dots = self.driver.find_elements_by_xpath(Data.dots)
        count = len(dots)
        self.assertEqual(0,count,msg="Failed ")
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()