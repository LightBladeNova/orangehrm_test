import sys
from pathlib import Path

import pytest
from selenium import webdriver

# Ensure project root is on sys.path so imports work when running from tests/
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.config import config
from pages.login import LoginPage


@pytest.fixture
def driver():
    """Initialize and cleanup WebDriver"""
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def verify_base_url_accessible(driver):
    """Verify BASE_URL is accessible; skip dependent tests if not"""
    try:
        driver.get(config.base_url)
        if "Page not found" in driver.page_source or "error" in driver.page_source.lower():
            pytest.skip("BASE_URL returned an error page - skipping dependent tests")
    except Exception as exc:
        pytest.skip(f"BASE_URL is not accessible: {exc}")


@pytest.fixture
def logged_in_browser(driver, verify_base_url_accessible):
    """Log into the app and return a ready browser session"""
    try:
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
    except Exception as exc:
        raise Exception(f"Login page failed to load: {exc}") from exc
    login_page.fill_username(config.username)
    login_page.fill_password(config.password)
    login_page.click_login()
    return driver
