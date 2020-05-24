import os
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.parameters import Data


class cqube():

    def __init__(self, driver):
        self.driver = driver

    def open_cqube_appln(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(Data.url)

    def login_cqube(self):
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()

    def navigate_to_student_report(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SAR).click()
        self.driver.find_element_by_xpath(Data.year).click()
        self.driver.find_element_by_xpath(Data.august).click()
    def navigate_to_student_report_S(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SAR).click()
        self.driver.find_element_by_xpath(Data.year).click()
        self.driver.find_element_by_xpath(Data.Sept).click()
    def navigate_to_student_report_O(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SAR).click()
        self.driver.find_element_by_xpath(Data.year).click()
        self.driver.find_element_by_xpath(Data.Oct).click()




    def navigate_to_semester_report(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SR).click()

    def navigate_to_crc_report(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.crc).click()

    def Details_text(self):
        Details = self.driver.find_elements_by_xpath(Data.details)
        time.sleep(5)
        for i in range(len(Details)):
           print(Details[i].text)

    def ClickOn_HomeButton(self):
            self.driver.find_element_by_id(Data.Home_icon).click()
            print(self.driver.current_url)

    def CRC_footers(self):
        footer = self.driver.find_elements_by_xpath(Data.footer)
        for i in range(len(footer)):
            print(footer[i].text)
            time.sleep(5)

    def test_Distnames(self):
        dnames = self.driver.find_elements_by_xpath(Data.Dnames)
        for i in range(len(dnames)):
            print(dnames[i].text)
            time.sleep(2)

    def dots_dist(self):
        distnames = self.driver.find_elements_by_xpath(Data.Dnames)
        for i in range(len(distnames)):
            print(distnames[i].click())
            time.sleep(3)
            lists = self.driver.find_elements_by_class_name(Data.dots)
            time.sleep(2)
            count = len(lists) - 1
            print(distnames[i].text, ":", count)

    def X_Yaxis(self):
        x_axis = self.driver.find_elements_by_xpath(Data.xaxis)
        time.sleep(2)
        print("X axis menu list...")
        for i in range(len(x_axis)):
            print(x_axis[i].text)
        print("Y axis menu list...")
        time.sleep(2)
        y_axis = self.driver.find_elements_by_xpath(Data.yaxis)
        for i in range(len(y_axis)):
            print(y_axis[i].text)

    def crcDist_click(self):
        clu = self.driver.find_elements_by_xpath(Data.clusterlist)
        for i in range(len(clu)):
            clu[i].click()
            time.sleep(6)

    def clusters_text(self):
        cluster = self.driver.find_elements_by_xpath(Data.clusterlist)
        for i in range(len(cluster)):
            cluster[i].click()
            print(cluster[i].text)
            time.sleep(5)

    def X_axis(self):
        xvalues = self.driver.find_elements_by_xpath(Data.xaxis)
        for i in range(len(xvalues)):
            xvalues[i].click()
            time.sleep(3)

    def get_driver_path(self):
        os.chdir('../')
        executable_path = os.path.join(os.getcwd(), 'Driver/chromedriver1')
        return executable_path


    #SAR
    def blocks_names(self):
        self.driver.find_element_by_xpath(Data.Blocks).click()
        time.sleep(15)
        print("Block details..")
        infob = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infob)):
            print(infob[i].text)

    def clusters_names(self):
        self.driver.find_element_by_xpath(Data.Clusters).click()
        time.sleep(15)
        print("Cluster details..")
        infoc = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infoc)):
            print(infoc[i].text)

    def schools_test(self):
        self.driver.find_element_by_xpath(Data.Schools).click()
        print("for schools details...")
        time.sleep(15)
        infos = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infos)):
            print(infos[i].text)


