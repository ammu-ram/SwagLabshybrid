from selenium.webdriver.common.by import By

class Logout():
    textfield_id_username = "user-name"
    textfield_id_password = "password"
    buttonfield_id_submit = "login-button"
    hamburgermenu_xpath ='//button[.="Open Menu"]'

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textfield_id_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textfield_id_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.buttonfield_id_submit).click()

    def menuforlogout(self):
        menu=self.driver.find_element(By.XPATH,self.hamburgermenu_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()",menu)
        menu.click()

    def clickLogout(self):
        logout=self.driver.find_element(By.XPATH,"//a[.='Logout']")
        self.driver.execute_script("arguments[0].scrollIntoView()",logout)
        logout.click()






