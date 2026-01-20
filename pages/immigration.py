from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.helpers import *
import time

class Immigration:
    def __init__(self, driver):
        self.driver = driver
    
    def click_myinfo(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href*='/web/index.php/pim/viewMyDetails']").click()

    def click_immigration_tab(self):
        return self.driver.find_element(By.XPATH, "//a[contains(text(), 'Immigration')]").click()
    
    def delete_existing_immigration_record(self):
        try:
            delete_buttons = self.driver.find_elements(By.CSS_SELECTOR, "i.oxd-icon.bi-trash")
            delete_buttons[0].click()  # Click the first Delete button for Immigration record
            confirm_delete_button = self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button.oxd-button--label-danger")
            confirm_delete_button.click()
        except Exception as e:
            print(f"No immigration record found: {e}")

    def delete_existing_immigration_attachment(self):
        try:
            delete_buttons = self.driver.find_elements(By.CSS_SELECTOR, "i.oxd-icon.bi-trash")
            delete_buttons[1].click()  # Click the second Delete button for Immigration attachment
            confirm_delete_button = self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button.oxd-button--label-danger")
            confirm_delete_button.click()
        except Exception as e:
            print(f"No immigration attachment found: {e}")

    def click_add_immigration_record_button(self):
        add_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.oxd-button--medium")
        add_buttons[0].click()  # Click the first Add button

    def click_add_immigration_attachment_button(self):
        add_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.oxd-button--medium")
        add_buttons[1].click()  # Click the second Add button

    def fill_number(self, number):
        number_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Number')]/../../div[2]/input")))
        fill_input(self.driver, number_element, number)
        time.sleep(1)

    def fill_issue_date(self, issue_date):
        issue_date_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Issued Date')]/../../div[2]//input")))
        fill_input(self.driver, issue_date_element, issue_date)
        time.sleep(1)

    def fill_expiry_date(self, expiry_date):
        expiry_date_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Expiry Date')]/../../div[2]//input")))
        fill_input(self.driver, expiry_date_element, expiry_date)
        time.sleep(1)

    def click_issued_by_dropdown(self):
        return self.driver.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").click()
    
    def click_afghanistan_option(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[role='listbox'] [role='option']:nth-child(2)").click()
    
    def immigration_record_table(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.oxd-table-body")

    def upload_attachment_file(self, file_path):
        try:
            file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            file_input.send_keys(file_path)
            time.sleep(1)
            print(f"Successfully uploaded file: {file_path}")
        except Exception as e:
            print(f"File upload failed: {e}")

    def download_attachment_file(self):
        return self.driver.find_element(By.XPATH, "//button//i[contains(@class, 'download')]").click()