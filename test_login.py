import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pageObject.LoginPage import LoginPage1
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration

class Test_001_Logins:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    # logger=LogGeneration.loggen()

    def test_homePageTitle(self,setup):
        self.logger=LogGeneration.loggen()
        self.logger.info("********* Test_001_Logins *********")
        self.logger.info("********* Verifying Home Page Title  *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)

        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* Home Page Title test is passed  *********")
        else:
            # self.driver.logging(".\\Logs\\automation.log")
            # Capture Screenshot on failures
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********* Home Page Title test is failed  *********")
            assert False

    def test_login12(self,setup):
        self.logger = LogGeneration.loggen()
        self.logger.info("********* Verifying Login test  *********")

        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        self.lp = LoginPage1(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        time.sleep(5)

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********* Login test is passed  *********")
            self.driver.close()
        else:
            # self.driver.logging(".\\Logs\\automation.log")
            # Capture Screenshot on failures
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login12.png")
            self.driver.close()
            self.logger.error("********* Login test is failed  *********")
            assert False



