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


class SemesterReport(unittest.TestCase):
    def setUp(self):
        dri = Data()
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
        for x in select_district.options[1:]:
            select_district.select_by_visible_text(x.text)
            time.sleep(1)
            for y in select_block.options[1:]:
                select_block.select_by_visible_text(y.text)
                time.sleep(1)
                for z in select_cluster.options[1:]:
                    select_cluster.select_by_visible_text(z.text)
                    # print(x.text, " ", y.text, " ", z.text)
                    time.sleep(1)
                    list = self.driver.find_elements_by_class_name(Data.dots)
                    elem = self.driver.find_element_by_xpath(Data.No_schools).text
                    res = re.sub("\D", "", elem)
                    if int(len(list)-1) != int(res):
                        self.assertEqual(int(len(list)-1), int(res),x.text+y.text+z.text)

    def tearDown(self):
        self.driver.close()