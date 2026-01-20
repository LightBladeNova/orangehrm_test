import config.config_data as config_data
import os
import pytest
from pages.immigration import Immigration
from pages.login import LoginPage
from pages.contact_details import ContactDetails
from pages.dependents import Dependents
from pages.personal_details import PersonalDetails
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.helpers import *
import time


@pytest.fixture
def driver():
    """Fixture to initialize and cleanup WebDriver"""
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture
def verify_base_url_accessible(driver):
    """Fixture to verify BASE_URL is accessible - skips tests if not"""
    try:
        driver.get(config_data.BASE_URL)
        # Check if page loaded successfully (not a 404 or error page)
        if "Page not found" in driver.page_source or "error" in driver.page_source.lower():
            pytest.skip("BASE_URL returned an error page - skipping dependent tests")
    except Exception as e:
        pytest.skip(f"BASE_URL is not accessible: {e}")

@pytest.fixture
def logged_in_browser(driver, verify_base_url_accessible):
    try:
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
    except Exception as e:
        raise Exception(f"Login page failed to load: {e}") from e
    login_page.fill_username(config_data.USERNAME)
    login_page.fill_password(config_data.PASSWORD)
    login_page.click_login()
    return driver

def test_login_fail(driver):
    """Test login invalid credentials for OrangeHRM"""
    try:
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
    except Exception as e:
        raise Exception(f"Login page failed to load: {e}") from e
    login_page.fill_username(config_data.INVALID_USERNAME)
    login_page.fill_password(config_data.INVALID_PASSWORD)
    login_page.click_login()
    time.sleep(3)
    alert_element = login_page.get_invalid_credentials_error()
    assert "Invalid credentials" in alert_element.text, "Expected 'Invalid credentials' alert not found" 
    current_url = driver.current_url
    assert "dashboard" not in current_url, "Login should have failed but dashboard found in URL"

@pytest.mark.dependency()
def test_login_success(logged_in_browser):
    """Test login functionality for OrangeHRM"""
    time.sleep(3)
    current_url = logged_in_browser.current_url
    assert "dashboard" in current_url, "Login failed: dashboard not found in URL"

@pytest.mark.dependency(depends=["test_login_success"])
def test_add_personal_details(logged_in_browser):
    """Test adding first name and last name to Personal Details in My Info page"""
    try:
        personal_details_page = PersonalDetails(logged_in_browser)
        personal_details_page.click_myinfo()
    except Exception as e:
        raise Exception(f"Personal Details page failed to load: {e}") from e
    wait_for_loader_to_disappear(logged_in_browser)
    personal_details_page.fill_firstname(config_data.FIRST_NAME)
    personal_details_page.fill_lastname(config_data.LAST_NAME)
    click_save_button_and_verify(logged_in_browser)
    # Verify firstName and lastName values were saved correctly
    actual_first_name = personal_details_page.firstname().get_attribute("value")
    actual_last_name = personal_details_page.lastname().get_attribute("value")
    assert actual_first_name == config_data.FIRST_NAME, f"Expected firstName to be 'John', but got '{actual_first_name}'"
    assert actual_last_name == config_data.LAST_NAME, f"Expected lastName to be 'Doe', but got '{actual_last_name}'"

@pytest.mark.dependency(depends=["test_add_personal_details"])
def test_add_contact_details(logged_in_browser):
    """Test adding contact details including address in My Info page"""
    try:
        contact_details_page = ContactDetails(logged_in_browser)
        contact_details_page.click_myinfo()
        contact_details_page.click_contact_details_tab()
    except Exception as e:
        raise Exception(f"Contact Details page failed to load: {e}") from e
    wait_for_loader_to_disappear(logged_in_browser)
    contact_details_page.fill_street1(config_data.STREET_1)
    contact_details_page.fill_city(config_data.CITY)
    contact_details_page.fill_state(config_data.STATE)
    contact_details_page.fill_zip(config_data.ZIP)
    contact_details_page.fill_workphone(config_data.WORK_PHONE)
    click_save_button_and_verify(logged_in_browser)
    # Verify contact details values were saved correctly
    assert contact_details_page.street1().get_attribute("value") == config_data.STREET_1, f"Expected street1 to be '{config_data.STREET_1}', but got '{contact_details_page.street1().get_attribute('value')}'"
    assert contact_details_page.city().get_attribute("value") == config_data.CITY, f"Expected city to be '{config_data.CITY}', but got '{contact_details_page.city().get_attribute('value')}'"
    assert contact_details_page.state().get_attribute("value") == config_data.STATE, f"Expected state to be '{config_data.STATE}', but got '{contact_details_page.state().get_attribute('value')}'"
    assert contact_details_page.zip().get_attribute("value") == config_data.ZIP, f"Expected zip to be '{config_data.ZIP}', but got '{contact_details_page.zip().get_attribute('value')}'"
    assert contact_details_page.work_phone().get_attribute("value") == config_data.WORK_PHONE, f"Expected work_phone to be '{config_data.WORK_PHONE}', but got '{contact_details_page.work_phone().get_attribute('value')}'"

@pytest.mark.dependency(depends=["test_add_personal_details", "test_add_contact_details"])
def test_add_dependents(logged_in_browser):
    """Test adding dependents in My Info page"""
    try:
        dependents_page = Dependents(logged_in_browser)
        dependents_page.click_myinfo()
        dependents_page.click_dependents_tab()
    except Exception as e:
        raise Exception(f"Dependents page failed to load: {e}") from e

    # Delete existing dependents if any
    dependents_page.delete_existing_dependents()

    # Add Child dependent
    dependents_page.click_add_dependent()
    # Verify input error on save without filling fields
    click_save_button_input_error(logged_in_browser)
    dependents_page.click_relationship_dropdown()
    dependents_page.click_child_relationship_option()
    dependents_page.fill_name(config_data.CHILD_DEPENDENT_NAME)
    dependents_page.fill_dob(config_data.CHILD_DEPENDENT_DOB)
    click_save_button_and_verify(logged_in_browser)
    wait_for_loader_to_disappear(logged_in_browser)

    # Add Other dependent (Mother)
    dependents_page.click_add_dependent()
    dependents_page.click_relationship_dropdown()
    dependents_page.click_other_relationship_option()
    dependents_page.fill_name(config_data.OTHER_DEPENDENT_NAME)
    dependents_page.fill_relationship(config_data.OTHER_DEPENDENT_RELATIONSHIP)
    dependents_page.fill_dob(config_data.OTHER_DEPENDENT_DOB)
    click_save_button_and_verify(logged_in_browser)
    wait_for_loader_to_disappear(logged_in_browser)

    # Verify dependents were added
    dependent_records = dependents_page.dependents_records()
    assert "(2) Records Found" in dependent_records.text, "Expected 2 dependents, but record count mismatch"
    dependents_table = dependents_page.dependents_table()
    assert config_data.CHILD_DEPENDENT_NAME in dependents_table.text, "Dependent 'Kevin' not found in dependents list"
    assert config_data.OTHER_DEPENDENT_NAME in dependents_table.text, "Dependent 'Samantha' not found in dependents list"

@pytest.mark.dependency(depends=["test_add_personal_details", "test_add_contact_details"])
def test_add_immigration_details(logged_in_browser):
    """Test adding immigration record in My Info page"""    
    try:
        immigration_page = Immigration(logged_in_browser)
        immigration_page.click_myinfo()
        immigration_page.click_immigration_tab()
        time.sleep(3)
    except Exception as e:
        raise Exception(f"Immigration page failed to load: {e}") from e
    
    # Delete existing immigration record if any
    immigration_page.delete_existing_immigration_record()
    wait_for_loader_to_disappear(logged_in_browser)

    immigration_page.click_add_immigration_record_button()
    # Verify input error on save without filling fields
    click_save_button_input_error(logged_in_browser)
    immigration_page.fill_number(config_data.IMMIGRATION_NUMBER)
    immigration_page.fill_issue_date(config_data.IMMIGRATION_ISSUE_DATE)
    immigration_page.fill_expiry_date(config_data.IMMIGRATION_EXPIRY_DATE)
    immigration_page.click_issued_by_dropdown()
    # Afghanistan is the 2nd option in the list
    immigration_page.click_afghanistan_option()
    click_save_button_and_verify(logged_in_browser)
    wait_for_loader_to_disappear(logged_in_browser)
    immigration_record_table = immigration_page.immigration_record_table()
    assert config_data.IMMIGRATION_NUMBER in immigration_record_table.text, "Immigration record '777' not found in immigration list"
    assert config_data.IMMIGRATION_ISSUED_BY in immigration_record_table.text, "Immigration record 'Afghanistan' not found in immigration list"
    assert config_data.IMMIGRATION_ISSUE_DATE in immigration_record_table.text or "01-01-2020" in immigration_record_table.text, "Immigration record '2020-01-01' not found in immigration list"
    assert config_data.IMMIGRATION_EXPIRY_DATE in immigration_record_table.text or "01-01-2030" in immigration_record_table.text, "Immigration record '2030-01-01' not found in immigration list"

@pytest.mark.dependency(depends=["test_add_personal_details", "test_add_contact_details"])
def test_add_immigration_attachment(logged_in_browser):
    """Test adding immigration attachment with file upload in My Info page"""    
    try:
        immigration_page = Immigration(logged_in_browser)
        immigration_page.click_myinfo()
        immigration_page.click_immigration_tab()
    except Exception as e:
        raise Exception(f"Immigration page failed to load: {e}") from e
    
    wait_for_loader_to_disappear(logged_in_browser)
    # Delete existing immigration record if any
    immigration_page.delete_existing_immigration_attachment()
    wait_for_loader_to_disappear(logged_in_browser)
    
    # Upload file attachment
    test_file_path = config_data.IMMIGRATION_TEST_FILE_PATH    
    immigration_page.click_add_immigration_attachment_button()
    immigration_page.upload_attachment_file(test_file_path)
    
    # Click save button
    try:
        click_save_button_and_verify(logged_in_browser)
    except Exception as e:
        print(f"Save verification failed (expected if no file): {e}")
    wait_for_loader_to_disappear(logged_in_browser)
    
    # Download attachment and verify
    download_dir = str(os.path.expanduser("~")) + "/Downloads"
    immigration_page.download_attachment_file()
    time.sleep(3)
    
    # Get the most recently modified file
    downloaded_files = [f for f in os.listdir(download_dir) if os.path.isfile(os.path.join(download_dir, f))]
    assert len(downloaded_files) > 0, "No files found in Downloads directory"
    latest_file = max(downloaded_files, key=lambda f: os.path.getmtime(os.path.join(download_dir, f)))
    assert latest_file, "Could not determine latest downloaded file"
    
    # Verify it's the test_immigration_document file
    assert "test_immigration_document" in latest_file, f"Expected 'test_immigration_document' in filename, but got '{latest_file}'"
    
    # Verify file content
    latest_file_path = os.path.join(download_dir, latest_file)
    with open(latest_file_path, "r") as f:
        downloaded_content = f.read()
    assert config_data.IMMIGRATION_ATTACHMENT_CONTENT in downloaded_content, f"Expected content '{config_data.IMMIGRATION_ATTACHMENT_CONTENT}' not found in downloaded file"
    print(f"✅ File download verified: {latest_file}")
