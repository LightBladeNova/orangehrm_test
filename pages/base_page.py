from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class BasePage:
    """Base page object with common helper methods"""
    MYINFO_LINK = (By.CSS_SELECTOR, "a[href*='/web/index.php/pim/viewMyDetails']")
    
    def __init__(self, driver):
        self.driver = driver

    def click_myinfo(self):
        """Navigate to the My Info page via the sidebar link"""
        return self.driver.find_element(*self.MYINFO_LINK).click()
    
    def wait_for_loader_to_disappear(self, timeout=15):
        """Wait for any loader overlays to disappear"""
        loader_locator = (By.CSS_SELECTOR, "div.oxd-form-loader")
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(loader_locator)
        )

    def click_save_button_input_error(self, timeout=6):
        """Click save and verify input error is displayed"""
        save_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        save_button.click()
        time.sleep(2)
        input_required_error = self.driver.find_element(By.CSS_SELECTOR, "span.oxd-input-field-error-message")
        assert input_required_error.text == "Required", "Input required error message not displayed"

    def click_save_button_and_verify(self, timeout=5):
        """Click save and verify success message"""
        save_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        save_button.click()
        time.sleep(2)
        # Verify the changes were saved by checking for success message
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast--success')]"))
            )
            success = True
        except Exception:
            success = False
        assert success, "Failed to save details - success message not found"

    def fill_input(self, webelement, value, timeout=10, attempts=3):
        """Clears the field robustly (Ctrl+A+Delete, JS fallback) then sends value.
        Returns True on success, False on failure after retries.
        """
        for attempt in range(attempts):
            try:
                # Try multiple ways to clear the field reliably
                try:
                    # send Ctrl+A then Delete
                    webelement.send_keys(Keys.CONTROL + "a")
                    webelement.send_keys(Keys.DELETE)
                except Exception:
                    pass
                # Fallback: clear via JavaScript then send value
                try:
                    self.driver.execute_script("arguments[0].value = '';", webelement)
                except Exception:
                    pass
                webelement.send_keys(value)
                time.sleep(1)
                return True
            except Exception:
                # small pause before retrying on other transient issues
                time.sleep(1)
        return False
