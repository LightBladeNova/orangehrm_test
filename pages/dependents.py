from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Dependents(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_myinfo(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href*='/web/index.php/pim/viewMyDetails']").click()

    def click_dependents_tab(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href*='/web/index.php/pim/viewDependents/empNumber/7']").click()
    
    def delete_existing_dependents(self):
        # Click each Delete button for existing dependents
        try:
            delete_buttons_num = len(self.driver.find_elements(By.CSS_SELECTOR, "i.oxd-icon.bi-trash"))
            for i in range(delete_buttons_num):
                delete_button = self.driver.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-trash")
                delete_button.click()
                confirm_delete_button = self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button.oxd-button--label-danger")
                confirm_delete_button.click()
                self.wait_for_loader_to_disappear()
                time.sleep(3)
        except Exception as exc:
            print(f"No existing dependents found: {exc}")
    
    def click_add_dependent(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button").click()
    
    def click_relationship_dropdown(self):
        return self.driver.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").click()
    
    def click_child_relationship_option(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[role='listbox'] [role='option']:nth-child(2)").click()
    
    def click_other_relationship_option(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[role='listbox'] [role='option']:nth-child(3)").click()
    
    def work_phone(self):
        return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Work')]/../../div[2]/input")))
    
    def fill_name(self, name):
        name_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Name')]/../../div[2]/input")))
        self.fill_input(name_element, name)
        time.sleep(1)

    def fill_dob(self, dob):
        dob_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Date of Birth')]/../../div[2]//input")))
        self.fill_input(dob_element, dob)
        time.sleep(1)

    def fill_relationship(self, relationship):
        relationship_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Please Specify')]/../../div[2]//input")))
        self.fill_input(relationship_element, relationship)
        time.sleep(1)

    def dependents_records(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-horizontal-padding span")
    
    def dependents_table(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.oxd-table-body")