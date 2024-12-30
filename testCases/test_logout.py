import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utilities.readProperties import ReadConfiguration
from pageObjects.logoutPage import Logout
from pageObjects.loginPage import Login


class TestLogout():
    baseUrl = ReadConfiguration.url()
    username =ReadConfiguration.username()
    password = ReadConfiguration.password()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_logout(self,setup):
        self.driver =setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        ts1 = Logout(self.driver)
        ts1.enter_username(self.username)
        ts1.enter_password(self.password)
        ts1.clickLogin()
        title=self.driver.title
        time.sleep(2)
        ts1.menuforlogout()
        time.sleep(2)
        ts1.clickLogout()
        if title=="Swag Labs":
            assert True
        else:
            self.driver.save_screenshot('/screenshots/test_logout.png')

        self.driver.close()
        self.driver.quit()

    @pytest.mark.sanity
    def test_validField(self,setup):
        self.driver =setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        ts2 = Login(self.driver)
        ts2.enter_username(self.username)
        ts2.enter_password(self.password)
        ts2.clickLogin()
        element=self.driver.find_element(By.XPATH,'//span[.="Products"]')
        if element.is_displayed():
            assert True
        else:
            self.driver.save_screenshot("/screenshots/test_validField.png")