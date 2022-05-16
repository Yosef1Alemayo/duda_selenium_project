import pytest
from selenium import webdriver

class Base:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Edge(executable_path='C:/Users/yossi/Desktop/Python-Project/duda_selenium_project'
                                                     '/Drivers/msedgedriver.exe')
        self.driver.implicitly_wait(15)
        self.driver.get('http://localhost:3000/signin')
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()


