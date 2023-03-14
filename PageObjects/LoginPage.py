from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class LoginPage:
    textbox_username_xpath = '//*[@id="Email"]'
    textbox_password_xpath = '//*[@id="Password"]'
    button_login_xpath = '//*[@type="submit"]'
    link_logout_xpath = '//*[@id="navbarText"]/ul/li[3]/a'

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator)))
        return element

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def send_keys(self, locator, value):
        element = self.wait_for_element(locator)
        element.send_keys(value)

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def AcceptAlertWindow(self):
        self.driver.switch_to.alert.accept()

    def DismissAlertWindow(self):
        self.driver.switch_to.alert.dismiss()
