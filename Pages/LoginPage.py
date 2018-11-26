from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):
    username = (By.NAME,'loginName')
    password = (By.ID,'password')
    loginbutton = (By.CLASS_NAME,'btn-block')
    usernamerror = (By.ID,'namePrompt')
    passworderror = (By.ID,'passwdPrompt')

    def set_username(self,username):
        name = self.driver.find_element(*LoginPage.username)
        name.send_keys(username)

    def set_password(self,password):
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password)

    def click_login(self):
        loginbutton = self.driver.find_element(*LoginPage.loginbutton)
        loginbutton.click()

    def get_title(self):
        return self.driver.title

    def get_nameerrorinfo(self):
        nameerror = self.driver.find_element(*LoginPage.usernamerror)
        return nameerror.text

    def get_pwderrorinfo(self):
        pwderror = self.driver.find_element(*LoginPage.passworderror)
        return pwderror

    def tear_down(self):
        self.driver.close()


    #def getalter(self):
        #alert = self.driver.switch_to_alert
        #return alert.text()
