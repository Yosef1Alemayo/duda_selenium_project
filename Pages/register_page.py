from Locators.register_locators import Register_Locators
from selenium.webdriver.common.by import By
class Register_Page:
    def __init__(self, driver):
        self.driver = driver
        self.registerField = Register_Locators.REGISTER_FIELDS  # All The Fields In The Page
        self.signUpButton = Register_Locators.SIGNUP_BUTTON  # The Signup Button

        # Messages:
        self.userNameError = Register_Locators.USER_NAME_ERROR  # Error Message - Required Field

    def register_page(self):
        self.driver.get('http://localhost:3000/signup')

    def register_fields(self, values: list):
        fields = self.driver.find_elements(By.XPATH, self.registerField)
        for row in range(len(fields)):
            fields[row].clear()
            fields[row].send_keys(values[row])

    def click_sign_up(self):
        self.driver.find_element(By.XPATH, self.signUpButton).click()

    def user_name_message(self):
        return self.driver.find_element(By.ID, self.userNameError).get_attribute('innerText')
