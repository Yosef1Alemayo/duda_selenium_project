import allure
from Pages.register_page import Register_Page
from Locators.register_locators import Register_Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from allure_commons.types import AttachmentType

class Utils:
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def validation(self, expected, actual):
        driver = self.driver
        try:
            assert expected == actual
        except AssertionError:
            allure.attach(driver.save_screenshot('..//Reports/ScreenShot.png'), attachment_type=AttachmentType.PNG)
            raise AssertionError

    @allure.step
    def register_incorrectly_all_combinations(self, values: list):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.register_fields(values)
        WebDriverWait(driver, 20).until_not(EC.element_to_be_clickable((By.XPATH, Register_Locators.SIGNUP_BUTTON)))