from utils.helpers import fill_input
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class PersonalDetails:
    def __init__(self, driver):
        self.driver = driver
    
    def click_myinfo(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href*='/web/index.php/pim/viewMyDetails']").click()

    def firstname(self):
        return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "firstName")))
    
    def lastname(self):
        return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "lastName")))

    def fill_firstname(self, firstname):
        fill_input(self.driver, self.firstname(), firstname)
        time.sleep(1)
    
    def fill_lastname(self, lastname):
        fill_input(self.driver, self.lastname(), lastname)
        time.sleep(1)
    