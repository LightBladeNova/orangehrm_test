import pytest
import config.config_data as config_data
from pages.contact_details import ContactDetails


@pytest.mark.dependency(depends=["personal_details"], name="contact_details", scope="session")
@pytest.mark.run(order=4)
def test_add_contact_details(logged_in_browser):
    """Test adding contact details including address in My Info page"""
    try:
        contact_details_page = ContactDetails(logged_in_browser)
        contact_details_page.click_myinfo()
        contact_details_page.click_contact_details_tab()
    except Exception as exc:
        raise Exception(f"Contact Details page failed to load: {exc}") from exc
    contact_details_page.wait_for_loader_to_disappear()
    contact_details_page.fill_street1(config_data.STREET_1)
    contact_details_page.fill_city(config_data.CITY)
    contact_details_page.fill_state(config_data.STATE)
    contact_details_page.fill_zip(config_data.ZIP)
    contact_details_page.fill_workphone(config_data.WORK_PHONE)
    contact_details_page.click_save_button_and_verify()
    assert contact_details_page.street1().get_attribute("value") == config_data.STREET_1, f"Expected street1 to be '{config_data.STREET_1}', but got '{contact_details_page.street1().get_attribute('value')}'"
    assert contact_details_page.city().get_attribute("value") == config_data.CITY, f"Expected city to be '{config_data.CITY}', but got '{contact_details_page.city().get_attribute('value')}'"
    assert contact_details_page.state().get_attribute("value") == config_data.STATE, f"Expected state to be '{config_data.STATE}', but got '{contact_details_page.state().get_attribute('value')}'"
    assert contact_details_page.zip().get_attribute("value") == config_data.ZIP, f"Expected zip to be '{config_data.ZIP}', but got '{contact_details_page.zip().get_attribute('value')}'"
    assert contact_details_page.work_phone().get_attribute("value") == config_data.WORK_PHONE, f"Expected work_phone to be '{config_data.WORK_PHONE}', but got '{contact_details_page.work_phone().get_attribute('value')}'"
