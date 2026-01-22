import time
import pytest
import config.config_data as config_data
from pages.login import LoginPage

@pytest.mark.run(order=1)
def test_login_fail(driver):
    """Test login invalid credentials for OrangeHRM"""
    try:
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
    except Exception as exc:
        raise Exception(f"Login page failed to load: {exc}") from exc
    login_page.fill_username(config_data.INVALID_USERNAME)
    login_page.fill_password(config_data.INVALID_PASSWORD)
    login_page.click_login()
    time.sleep(3)
    alert_element = login_page.get_invalid_credentials_error()
    assert "Invalid credentials" in alert_element.text, "Expected 'Invalid credentials' alert not found"
    current_url = driver.current_url
    assert "dashboard" not in current_url, "Login should have failed but dashboard found in URL"


@pytest.mark.dependency(name="login_success", scope="session")
@pytest.mark.run(order=2)
def test_login_success(logged_in_browser):
    """Test login functionality for OrangeHRM"""
    time.sleep(3)
    current_url = logged_in_browser.current_url
    assert "dashboard" in current_url, "Login failed: dashboard not found in URL"
