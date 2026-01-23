import logging
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class Dependents(BasePage):
    LOCATORS = {
        "dependents_tab": (By.CSS_SELECTOR, "a[href*='/web/index.php/pim/viewDependents/empNumber/7']"),
        "delete_button": (By.CSS_SELECTOR, "i.oxd-icon.bi-trash"),
        "confirm_delete_button": (By.CSS_SELECTOR, "button.oxd-button.oxd-button--label-danger"),
        "add_button": (By.CSS_SELECTOR, "button.oxd-button"),
        "relationship_dropdown": (By.CSS_SELECTOR, "i.oxd-icon.bi-caret-down-fill.oxd-select-text--arrow"),
        "child_option": (By.CSS_SELECTOR, "[role='listbox'] [role='option']:nth-child(2)"),
        "other_option": (By.CSS_SELECTOR, "[role='listbox'] [role='option']:nth-child(3)"),
        "work_phone_field": (By.XPATH, "//label[contains(text(),'Work')]/../../div[2]/input"),
        "name_field": (By.XPATH, "//label[contains(text(),'Name')]/../../div[2]/input"),
        "dob_field": (By.XPATH, "//label[contains(text(),'Date of Birth')]/../../div[2]//input"),
        "relationship_field": (By.XPATH, "//label[contains(text(),'Please Specify')]/../../div[2]//input"),
        "dependents_records": (By.CSS_SELECTOR, ".orangehrm-horizontal-padding span"),
        "dependents_table": (By.CSS_SELECTOR, "div.oxd-table-body"),
    }

    def __init__(self, driver):
        super().__init__(driver)
    
    def click_dependents_tab(self):
        return self.driver.find_element(*self.LOCATORS["dependents_tab"]).click()
    
    def delete_existing_dependents(self):
        # Click each Delete button for existing dependents
        try:
            delete_buttons_num = len(self.driver.find_elements(*self.LOCATORS["delete_button"]))
            for i in range(delete_buttons_num):
                delete_button = self.driver.find_element(*self.LOCATORS["delete_button"])
                delete_button.click()
                confirm_delete_button = self.driver.find_element(*self.LOCATORS["confirm_delete_button"])
                confirm_delete_button.click()
                self.wait_for_loader_to_disappear()
                time.sleep(3)
        except Exception as exc:
            logger.warning("No existing dependents found: %s", exc)
    
    def click_add_dependent(self):
        return self.driver.find_element(*self.LOCATORS["add_button"]).click()
    
    def click_relationship_dropdown(self):
        return self.driver.find_element(*self.LOCATORS["relationship_dropdown"]).click()
    
    def click_child_relationship_option(self):
        return self.driver.find_element(*self.LOCATORS["child_option"]).click()
    
    def click_other_relationship_option(self):
        return self.driver.find_element(*self.LOCATORS["other_option"]).click()
    
    def work_phone(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["work_phone_field"]))
    
    def fill_name(self, name: str):
        name_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["name_field"]))
        self.fill_input(name_element, name)

    def fill_dob(self, dob: str):
        dob_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["dob_field"]))
        self.fill_input(dob_element, dob)

    def fill_relationship(self, relationship: str):
        relationship_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["relationship_field"]))
        self.fill_input(relationship_element, relationship)

    def dependents_records(self):
        return self.driver.find_element(*self.LOCATORS["dependents_records"])
    
    def dependents_table(self):
        return self.driver.find_element(*self.LOCATORS["dependents_table"])