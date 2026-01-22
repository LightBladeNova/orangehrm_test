import pytest
from core.config import config
from pages.contact_details import ContactDetails


@pytest.mark.dependency(depends=["personal_details"], name="contact_details", scope="session")
@pytest.mark.run(order=4)
def test_add_contact_details(logged_in_browser):
    try:
        contact_details_page = ContactDetails(logged_in_browser)
        contact_details_page.click_myinfo()
        contact_details_page.click_contact_details_tab()
    except Exception as exc:
        raise Exception(f"Contact Details page failed to load: {exc}") from exc
    contact_details_page.wait_for_loader_to_disappear()
    contact_details_page.fill_street1(config.street_1)
    contact_details_page.fill_city(config.city)
    contact_details_page.fill_state(config.state)
    contact_details_page.fill_zip(config.zip)
    contact_details_page.fill_workphone(config.work_phone)
    contact_details_page.click_save_button_and_verify()
    assert contact_details_page.street1().get_attribute("value") == config.street_1, f"Expected street1 to be '{config.street_1}', but got '{contact_details_page.street1().get_attribute('value')}'"
    assert contact_details_page.city().get_attribute("value") == config.city, f"Expected city to be '{config.city}', but got '{contact_details_page.city().get_attribute('value')}'"
    assert contact_details_page.state().get_attribute("value") == config.state, f"Expected state to be '{config.state}', but got '{contact_details_page.state().get_attribute('value')}'"
    assert contact_details_page.zip().get_attribute("value") == config.zip, f"Expected zip to be '{config.zip}', but got '{contact_details_page.zip().get_attribute('value')}'"
    assert contact_details_page.work_phone().get_attribute("value") == config.work_phone, f"Expected work_phone to be '{config.work_phone}', but got '{contact_details_page.work_phone().get_attribute('value')}'"
