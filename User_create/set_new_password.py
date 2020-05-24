import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube


class Click_ChangePassword(unittest.TestCase):
    def setUp(self):
        dri = Data()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()

    def test_set_newpwd(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/mat-list-item/div/button/span/mat-icon").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/div/a[2]/div/span").click()
        pwd =self.driver.find_element_by_xpath("//h2").text
        self.assertEqual(pwd,"Change Password","Change password is not found!..")
        # self.driver.find_element_by_xpath("//input[@name='newPasswd']").send_keys("1234")
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//input[@name='cnfpass']").send_keys("1234")
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()