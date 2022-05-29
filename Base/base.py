import pytest
from selenium import webdriver

class Base:
    @pytest.fixture(autouse=True)
    def set_up(self):
        print('\nTest Started')
        self.driver = webdriver.Edge(executable_path='..//Drivers/msedgedriver.exe')
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            print('\nTest Finished')
            self.driver.close()
            self.driver.quit()
