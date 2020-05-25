import sys
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from TS.arg import arg
from TS.reuse_func import cqube
from TestNG.cqube import MyTestSuite
from  get_dir import pwd
#pwd = Data()
p = pwd()
sys.path.append(p.get_system_path())


class TestCases():
    #dri = Data()
    dri = pwd()
    driver = webdriver.Chrome(dri.get_driver_path())
    driver1 = cqube(driver)
    driver1.open_cqube_appln()
    driver1.login_cqube()
    driver1.navigate_to_student_report()
    time.sleep(3)
    select_year = Select(driver.find_element_by_name(Data.select_year))
    select_month = Select(driver.find_element_by_name(Data.select_month))
    time.sleep(3)

    year = []
    month = []

    for x in select_year.options:
        year.append(x.text)
    for y in select_month.options:
        month.append(y.text)

    for x in range(1, len(year)):
        for y in range(1,len(month)):
            a = arg()
            a.list.append(year[x])
            a.list.append(month[y])
            cal = MyTestSuite()
            cal.test_Issue(month[y])
            a.list.clear()

    driver.close()









