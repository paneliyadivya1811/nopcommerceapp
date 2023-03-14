import time

from PageObjects.LoginPage import LoginPage
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XlUtils

class Test_002_DDT_Login:
    driver = None
    base_url = ReadConfig.get_base_url()
    path = './/TestData/LoginData.xlsx'
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*******Test_login-ddt started********")
        self.logger.info("***********Verifying Home Page Title***********")
        self.driver = setup
        print(self.base_url)
        self.driver.get(str(self.base_url))
        self.lp = LoginPage(self.driver)
        self.rows = XlUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a Excel:", self.rows)
        lst_status = []  # Empty List variable

        for r in range(2, self.rows+1):
            self.user = XlUtils.Readdata(self.path, "Sheet1", r, 1)
            self.password = XlUtils.Readdata(self.path, "Sheet1", r, 2)
            self.exp = XlUtils.Readdata(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("Test is passed")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "fail":
                    self.logger.info("Test is failed")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("test is Failed")
                    lst_status.append("Failed")
                elif self.exp == "fail":
                    self.logger.info("Test is Passed")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("Login DDT test Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test Failed")
            self.driver.close()
            assert False
        self.logger.info("End of Login DDT Test");
        self.logger.info("Complete TC_LoginDDT_002")


