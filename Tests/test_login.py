import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base import Base
from Pages.login_page import Login_Page
import pytest

@pytest.mark.usefixtures('set_up')
class Test_Login(Base):
    @allure.description('User Registered Correctly')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_correctly(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.enter_username('RM12')
        login.enter_password('147852963')
        login.click_signin_button()
        WebDriverWait(driver, 20).until(EC.url_to_be('http://localhost:3000/'))