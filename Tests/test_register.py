from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Locators.register_locators import Register_Locators
from selenium.webdriver.common.by import By
from Utils.utils import Utils
from Base.base import Base
from Pages.register_page import Register_Page

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

    def test_register_incorrectly_without_username(self):
        driver = self.driver
        validation = Utils(driver)
        register = Register_Page(driver)
        register.register_page()
        register.register_fields(['Avi', 'Yakov', '', '147852963', '147852963'])
        WebDriverWait(driver, 20).until_not(EC.element_to_be_clickable((By.XPATH, Register_Locators.SIGNUP_BUTTON)))
        validation.validation(register.user_name_message(), "Username is required")
