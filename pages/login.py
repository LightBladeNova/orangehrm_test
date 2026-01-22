from core.config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login_page(self):
        self.driver.get(config.base_url)
    
    def fill_username(self, username):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "username")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(username)

    def fill_password(self, password):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def get_invalid_credentials_error(self):
        return self.driver.find_element(By.CSS_SELECTOR, "p.oxd-alert-content-text")