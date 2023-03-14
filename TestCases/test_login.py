from PageObjects.LoginPage import LoginPage
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    driver = None
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*******Test_00f1_Login started********")
        self.logger.info("***********Verifying Home Page Title***********")
        self.driver = setup
        self.driver.get(self.base_url)
        act_Title = self.driver.title
        if act_Title == "Your store. Login":
            assert True
            self.logger.info("*******Home Page Title test is passed********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error("*******Home Page Title test is failed********")
            self.driver.close()


    # def test_login(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     self.driver.maximize_window()
    #     # self.lp.AcceptAlertWindow()
    #     # self.lp.DismissAlertWindow()
    #
    #     act_title = self.driver.title
    #     self.lp.clickLogout()
    #
    #     if act_title == "administration":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
    #         self.driver.close()
    #         assert False
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*******Test_login started********")
        self.logger.info("***********Verifying Home Page Title***********")
        self.driver = setup
        print(self.base_url)
        self.driver.get(str(self.base_url))
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        act_title = self.driver.title
        self.lp.clickLogout()

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******Home Page Title test is passed********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.driver.close()
            self.logger.error("*******Home Page Title test is failed********")








