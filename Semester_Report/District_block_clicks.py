import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Districts(unittest.TestCase):
    @classmethod
    def setUp(self):
          dri = pwd()
          self.driver = webdriver.Chrome(dri.get_driver_path())
          driver = cqube(self.driver)
          driver.open_cqube_appln()
          driver.login_cqube()
          driver.navigate_to_semester_report()
    def test_click_on_districtnames(self):
        time.sleep(5)

        distnames = self.driver.find_elements_by_xpath(Data.Dnames)
        details = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(distnames)):
            distnames[i].click()
            time.sleep(6)
            dots=self.driver.find_elements_by_class_name(Data.dots)
            count =len(dots)-1
            school =self.driver.find_element_by_xpath(Data.schoolcount).text
            students=self.driver.find_element_by_xpath(Data.students).text
            print(distnames[i].text, "dots : ", count," ",school," ",students )
            time.sleep(4)
            self.assertNotEqual(0,count,msg="mis match found")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
