import logging
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class Immigration(BasePage):
    LOCATORS = {
        "immigration_tab": (By.XPATH, "//a[contains(text(), 'Immigration')]"),
        "delete_button": (By.CSS_SELECTOR, "i.oxd-icon.bi-trash"),
        "confirm_delete_button": (By.CSS_SELECTOR, "button.oxd-button.oxd-button--label-danger"),
        "add_button": (By.CSS_SELECTOR, "button.oxd-button--medium"),
        "number_field": (By.XPATH, "//label[contains(text(),'Number')]/../../div[2]/input"),
        "issue_date_field": (By.XPATH, "//label[contains(text(),'Issued Date')]/../../div[2]//input"),
        "expiry_date_field": (By.XPATH, "//label[contains(text(),'Expiry Date')]/../../div[2]//input"),
        "issued_by_dropdown": (By.CSS_SELECTOR, "i.oxd-icon.bi-caret-down-fill.oxd-select-text--arrow"),
        "afghanistan_option": (By.CSS_SELECTOR, "[role='listbox'] [role='option']:nth-child(2)"),
        "immigration_table": (By.CSS_SELECTOR, "div.oxd-table-body"),
        "file_input": (By.CSS_SELECTOR, "input[type='file']"),
        "download_button": (By.XPATH, "//button//i[contains(@class, 'download')]"),
    }

    def __init__(self, driver):
        super().__init__(driver)

    def click_immigration_tab(self):
        return self.driver.find_element(*self.LOCATORS["immigration_tab"]).click()
    
    def delete_existing_immigration_record(self):
        try:
            delete_buttons = self.driver.find_elements(*self.LOCATORS["delete_button"])
            delete_buttons[0].click()  # Click the first Delete button for Immigration record
            confirm_delete_button = self.driver.find_element(*self.LOCATORS["confirm_delete_button"])
            confirm_delete_button.click()
        except Exception as exc:
            logger.warning("No immigration record found: %s", exc)

    def delete_existing_immigration_attachment(self):
        try:
            delete_buttons = self.driver.find_elements(*self.LOCATORS["delete_button"])
            delete_buttons[1].click()  # Click the second Delete button for Immigration attachment
            confirm_delete_button = self.driver.find_element(*self.LOCATORS["confirm_delete_button"])
            confirm_delete_button.click()
        except Exception as exc:
            logger.warning("No immigration attachment found: %s", exc)

    def click_add_immigration_record_button(self):
        add_buttons = self.driver.find_elements(*self.LOCATORS["add_button"])
        add_buttons[0].click()  # Click the first Add button

    def click_add_immigration_attachment_button(self):
        add_buttons = self.driver.find_elements(*self.LOCATORS["add_button"])
        add_buttons[1].click()  # Click the second Add button

    def fill_number(self, number: str):
        number_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["number_field"]))
        self.fill_input(number_element, number)

    def fill_issue_date(self, issue_date: str):
        issue_date_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["issue_date_field"]))
        self.fill_input(issue_date_element, issue_date)

    def fill_expiry_date(self, expiry_date: str):
        expiry_date_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["expiry_date_field"]))
        self.fill_input(expiry_date_element, expiry_date)

    def click_issued_by_dropdown(self):
        return self.driver.find_element(*self.LOCATORS["issued_by_dropdown"]).click()
    
    def click_afghanistan_option(self):
        return self.driver.find_element(*self.LOCATORS["afghanistan_option"]).click()
    
    def immigration_record_table(self):
        return self.driver.find_element(*self.LOCATORS["immigration_table"])

    def upload_attachment_file(self, file_path: str):
        try:
            file_input = self.driver.find_element(*self.LOCATORS["file_input"])
            file_input.send_keys(file_path)
            time.sleep(1)
            logger.info("Successfully uploaded file: %s", file_path)
        except Exception as e:
            logger.warning("File upload failed: %s", e)

    def download_attachment_file(self):
        return self.driver.find_element(*self.LOCATORS["download_button"]).click()