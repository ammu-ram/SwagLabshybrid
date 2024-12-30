import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.customLogger import logGeneration
from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfiguration

class Testlogin():
    baseUrl = ReadConfiguration.url()
    username = ReadConfiguration.username()
    password = ReadConfiguration.password()
    logger = logGeneration.logGeneration()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_validLogin(self,setup):
        self.logger.info("Session started")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        ts1 = Login(self.driver)
        ts1.enter_username(self.username)
        time.sleep(2)
        ts1.enter_password(self.password)
        time.sleep(2)
        ts1.clickLogin()
        title = self.driver.title
        if title =="Swag Labs":
            assert True
        else:
            self.driver.save_screenshot('screenshots/test_validlogin.png')
            assert False

    @pytest.mark.sanity
    def test_validUserField(self,setup):
        self.driver =setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        username_field = self.driver.find_element(By.ID,"user-name")
        if username_field.is_enabled():
            assert True
        else:
            self.driver.save_screenshot('screenshots/test_validUserField.png')
            assert False

    @pytest.mark.sanity
    def test_validPasswordField(self,setup):
        self.driver =setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        password_field = self.driver.find_element(By.ID,"password")
        if password_field.is_enabled():
            assert True
        else:
            self.driver.save_screenshot('screenshots/test_validPasswordField.png')
            assert False

