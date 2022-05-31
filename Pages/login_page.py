from Locators.login_locators import Locators_Login
from selenium.webdriver.common.by import By
class Login_Page:
    def __init__(self, driver):
        self.driver = driver
        self.userNameField = Locators_Login.USERNAME_FIELD
        self.passwordField = Locators_Login.PASSWORD_FIELD
        self.signInButton = Locators_Login.SIGNIN_BUTTON
        self.rememberMeBox = Locators_Login.REMEMBER_ME_BOX
        self.registerLink = Locators_Login.REGISTER_LINK
        self.cypressLink = Locators_Login.CYPRESS_LINK

    def login_page(self):
        self.driver.get('http://localhost:3000/signin')

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.userNameField).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.userNameField).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.passwordField).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.passwordField).send_keys(password)

    def click_signin_button(self):
        self.driver.find_element(By.TAG_NAME, self.signInButton).click()
