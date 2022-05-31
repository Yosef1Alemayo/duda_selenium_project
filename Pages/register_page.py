from Locators.register_locators import Register_Locators
from selenium.webdriver.common.by import By
import allure

class Register_Page:
    def __init__(self, driver):
        self.driver = driver
        self.registerField = Register_Locators.REGISTER_FIELDS  # All The Fields In The Page
        self.signUpButton = Register_Locators.SIGNUP_BUTTON  # The Signup Button
        self.logInLink = Register_Locators.LOG_IN_LINK  # LogIn Link
        self.cypressLink = Register_Locators.CYPRESS_LINK  # Cypress Link
        # Messages:
        self.firstNameError = Register_Locators.FIRST_NAME_ERROR  # Error Message - Required Field
        self.lastNameError = Register_Locators.LAST_NAME_ERROR  # Error Message - Required Field
        self.userNameError = Register_Locators.USER_NAME_ERROR  # Error Message - Required Field
        self.passwordError = Register_Locators.PASSWORD_ERROR  # Error Message - Required Field
        self.confirmPasswordError = Register_Locators.CONFIRM_PASSWORD  # Error Message - Required Field

    @allure.description('This is The Pre Condition')
    def register_page(self):
        self.driver.get('http://localhost:3000/signup')

    @allure.step
    def register_fields(self, values: list):
        fields = self.driver.find_elements(By.XPATH, self.registerField)
        for row in range(len(fields)):
            fields[row].clear()
            fields[row].send_keys(values[row])

    @allure.step
    def click_sign_up(self):
        self.driver.find_element(By.XPATH, self.signUpButton).click()

    # Not Clickable:
    # ---------------------------------------
    @allure.step
    def click_login_link(self):
        self.driver.find_element(By.LINK_TEXT, self.logInLink).click()

    @allure.step
    def click_cypress_link(self):
        self.driver.find_element(By.XPATH, self.cypressLink).click()
    # ---------------------------------------

    # Messages:
    @allure.step
    def first_name_message(self):
        return self.driver.find_element(By.ID, self.firstNameError).get_attribute('innerText')

    @allure.step
    def last_name_message(self):
        return self.driver.find_element(By.ID, self.lastNameError).get_attribute('innerText')

    @allure.step
    def user_name_message(self):
        return self.driver.find_element(By.ID, self.userNameError).get_attribute('innerText')

    @allure.step
    def password_message(self):
        return self.driver.find_element(By.ID, self.passwordError).get_attribute('innerText')

    @allure.step
    def confirm_password_message(self):
        return self.driver.find_element(By.ID, self.confirmPasswordError).get_attribute('innerText')
