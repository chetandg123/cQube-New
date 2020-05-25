import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class SemesterReport(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report()

    def test_cluster(self):
        time.sleep(5)
        select_district = Select(self.driver.find_element_by_name(Data.select_district))
        select_block = Select(self.driver.find_element_by_name(Data.select_blocks))
        select_cluster = Select(self.driver.find_element_by_name(Data.select_clusters))
        time.sleep(5)

        def test_select_district_block_cluster(self):
            time.sleep(5)
            select_district = Select(self.driver.find_element_by_name(Data.select_district))
            select_block = Select(self.driver.find_element_by_name(Data.select_blocks))
            select_cluster = Select(self.driver.find_element_by_name(Data.select_clusters))
            time.sleep(5)
            for x in range(1, len(select_district.options)):
                select_district.select_by_index(x)
                time.sleep(2)
                for y in range(1, len(select_block.options)):
                    select_block.select_by_index(y)
                    time.sleep(2)
                    for z in range(1, len(select_cluster.options)):
                        select_cluster.select_by_index(z)
                        time.sleep(2)
                        list = self.driver.find_elements_by_class_name(Data.dots)
                        elem = self.driver.find_element_by_xpath(Data.No_schools).text
                        res = re.sub("\D", "", elem)
                        if int(len(list) - 1) != int(res):
                            self.assertEqual(int(len(list) - 1), int(res), "no of dots is not equal to no of schools")

    def tearDown(self):
        self.driver.close()