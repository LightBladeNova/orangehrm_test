from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PersonalDetails(BasePage):
    LOCATORS = {
        "first_name_field": (By.NAME, "firstName"),
        "last_name_field": (By.NAME, "lastName"),
    }

    def __init__(self, driver):
        super().__init__(driver)
    
    def firstname(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["first_name_field"]))
    
    def lastname(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["last_name_field"]))

    def fill_firstname(self, firstname: str):
        self.fill_input(self.firstname(), firstname)
        time.sleep(1)
    
    def fill_lastname(self, lastname: str):
        self.fill_input(self.lastname(), lastname)
        time.sleep(1)
    