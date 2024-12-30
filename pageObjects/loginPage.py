from selenium.webdriver.common.by import By

class Login():
    textfield_id_username = "user-name"
    textfield_id_password = "password"
    buttonfield_id_submit = "login-button"

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(By.ID,self.textfield_id_username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textfield_id_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID,self.buttonfield_id_submit).click()



