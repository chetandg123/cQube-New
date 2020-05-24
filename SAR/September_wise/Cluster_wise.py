import re
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube


class Schools_validation(unittest.TestCase):
    @classmethod
    def setUp(self):
        dri = Data()
        # self.driver = webdriver.Chrome(dri.get_driver_path())
        self.driver = webdriver.Chrome(Data.path)
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report_S()

    def test_validate_schoolrecords(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.SARD1).click()
        self.driver.find_element_by_xpath(Data.SARB3).click()
        self.driver.find_element_by_xpath(Data.SARC3).click()
        time.sleep(5)
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)-1
        self.assertNotEqual(0,count,msg="Failed")
        no_schools = self.driver.find_element_by_xpath(Data.No_schools).text
        str = no_schools
        res = re.sub("\D", "", str)
        self.assertEqual(count,int(res),msg="mis matching found!")


    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()