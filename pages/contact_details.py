from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactDetails(BasePage):
    LOCATORS = {
        "contact_details_tab": (By.CSS_SELECTOR, "a[href*='/web/index.php/pim/contactDetails/empNumber/7']"),
        "street1_field": (By.XPATH, "//label[contains(text(),'Street 1')]/../../div[2]/input"),
        "city_field": (By.XPATH, "//label[contains(text(),'City')]/../../div[2]/input"),
        "state_field": (By.XPATH, "//label[contains(text(),'State/Province')]/../../div[2]/input"),
        "zip_field": (By.XPATH, "//label[contains(text(),'Zip/Postal Code')]/../../div[2]/input"),
        "work_phone_field": (By.XPATH, "//label[contains(text(),'Work')]/../../div[2]/input"),
    }

    def __init__(self, driver):
        super().__init__(driver)
    
    def click_contact_details_tab(self):
        return self.driver.find_element(*self.LOCATORS["contact_details_tab"]).click()
    
    def street1(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["street1_field"]))
    
    def city(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["city_field"]))
    
    def state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["state_field"]))
    
    def zip(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["zip_field"]))
    
    def work_phone(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["work_phone_field"]))
    
    def fill_street1(self, street1: str):
        self.fill_input(self.street1(), street1)
        
    def fill_city(self, city: str):
        self.fill_input(self.city(), city)

    def fill_state(self, state: str):
        self.fill_input(self.state(), state)

    def fill_zip(self, zip: str):
        self.fill_input(self.zip(), zip)

    def fill_workphone(self, workphone: str):
        self.fill_input(self.work_phone(), workphone)
