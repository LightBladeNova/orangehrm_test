from core.config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOCATORS = {
        "username_field": (By.NAME, "username"),
        "password_field": (By.NAME, "password"),
        "login_button": (By.XPATH, "//button[@type='submit']"),
        "error_message": (By.CSS_SELECTOR, "p.oxd-alert-content-text"),
    }

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login_page(self):
        self.driver.get(config.base_url)
    
    def fill_username(self, username: str):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["username_field"]))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(username)

    def fill_password(self, password: str):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["password_field"]))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOCATORS["login_button"]).click()

    def get_invalid_credentials_error(self):
        return self.driver.find_element(*self.LOCATORS["error_message"])