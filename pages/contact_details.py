from utils.helpers import fill_input
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class ContactDetails:
    def __init__(self, driver):
        self.driver = driver
    
    def click_myinfo(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href*='/web/index.php/pim/viewMyDetails']").click()

    def click_contact_details_tab(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href*='/web/index.php/pim/contactDetails/empNumber/7']").click()
    
    def street1(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Street 1')]/../../div[2]/input")))
    
    def city(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'City')]/../../div[2]/input")))
    
    def state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'State/Province')]/../../div[2]/input")))
    
    def zip(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Zip/Postal Code')]/../../div[2]/input")))
    
    def work_phone(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Work')]/../../div[2]/input")))
    
    def fill_street1(self, street1):
        fill_input(self.driver, self.street1(), street1)
        time.sleep(1)
        
    def fill_city(self, city):
        fill_input(self.driver, self.city(), city)
        time.sleep(1)

    def fill_state(self, state):
        fill_input(self.driver, self.state(), state)
        time.sleep(1)

    def fill_zip(self, zip):
        fill_input(self.driver, self.zip(), zip)
        time.sleep(1)

    def fill_workphone(self, workphone):
        fill_input(self.driver, self.work_phone(), workphone)
        time.sleep(1)
