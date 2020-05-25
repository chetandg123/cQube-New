import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Schools_validation(unittest.TestCase):

    @classmethod
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report_O()

    def test_validate_schoolrecords(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.Schools).click()
        time.sleep(30)
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)-1
        print("no of dots:",count)
        with open('Data_files/School_wise_report_August_2019.csv', 'r') as file:
            reader = csv.reader(file)
            lines = len(list(reader))
            print("no of records in file:",lines)
        self.assertEqual(count,lines,"unmatching count found")
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()