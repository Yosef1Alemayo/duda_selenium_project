import pytest
from Utils.utils import Utils
from Base.base import Base
from selenium.webdriver.common.by import By
from Pages.register_page import Register_Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.register_locators import Register_Locators

@pytest.mark.usefixtures('set_up')
class Test_Register(Base):
    def test_register_correctly(self):
        driver = self.driver
        validation = Utils(driver)
        register = Register_Page(driver)
        register.register_page()
        register.register_fields(['Avi', 'Yakov', 'AviYakov12', '147852963', '147852963'])
        register.click_sign_up()
        WebDriverWait(driver, 20).until(EC.url_to_be('http://localhost:3000/signin'))
        validation.validation(driver.current_url, 'http://localhost:3000/signin')

    def test_register_incorrectly_without_first_name(self):
        driver = self.driver
        register = Register_Page(driver)
        validation = Utils(driver)
        validation.register_incorrectly_all_combinations(['', 'Yakov', 'AVI_YAKOV', '123456789', '123456789'])
        validation.validation(register.first_name_message(), 'First Name is required')

    def test_register_incorrectly_without_last_name(self):
        driver = self.driver
        validation = Utils(driver)
        register = Register_Page(driver)
        register.register_page()
        register.register_fields(['Avi', '', 'AVI_YAKOV', '123456789', '123456789'])
        WebDriverWait(driver, 20).until_not(EC.element_to_be_clickable((By.XPATH, Register_Locators.SIGNUP_BUTTON)))
        validation.validation(register.last_name_message(), "Last Name is required")

    def test_register_incorrectly_without_username(self):
        driver = self.driver
        register = Register_Page(driver)
        validation = Utils(driver)
        validation.register_incorrectly_all_combinations(['Avi', 'Yakov', '', '123456789', '123456789'])
        validation.validation(register.user_name_message(), 'Username is required')

    def test_register_incorrectly_without_password(self):
        driver = self.driver
        register = Register_Page(driver)
        validation = Utils(driver)
        validation.register_incorrectly_all_combinations(['Avi', 'Yakov', 'AviYAKOV', '', ''])
        validation.validation(register.password_message(), 'Enter your password')

    def test_register_when_all_the_fields_null(self):
        driver = self.driver
        register = Register_Page(driver)
        validation = Utils(driver)
        validation.register_incorrectly_all_combinations(['', '', '', '', ''])
        validation.validation(register.first_name_message(), 'First Name is required')
        validation.validation(register.last_name_message(), "Last Name is required")
        validation.validation(register.user_name_message(), 'Username is required')
        validation.validation(register.password_message(), 'Enter your password')

    def test_navigate_to_login_link(self):
        driver = self.driver
        register = Register_Page(driver)
        register.register_page()
        register.click_login_link()
        register.click_login_link()
        WebDriverWait(driver, 20).until(EC.url_to_be('http://localhost:3000/signin'))

