import pytest
import config.config_data as config_data
from pages.personal_details import PersonalDetails


@pytest.mark.dependency(depends=["login_success"], name="personal_details", scope="session")
@pytest.mark.run(order=3)
def test_add_personal_details(logged_in_browser):
    """Test adding first name and last name to Personal Details in My Info page"""
    try:
        personal_details_page = PersonalDetails(logged_in_browser)
        personal_details_page.click_myinfo()
    except Exception as exc:
        raise Exception(f"Personal Details page failed to load: {exc}") from exc
    personal_details_page.wait_for_loader_to_disappear()
    personal_details_page.fill_firstname(config_data.FIRST_NAME)
    personal_details_page.fill_lastname(config_data.LAST_NAME)
    personal_details_page.click_save_button_and_verify()
    actual_first_name = personal_details_page.firstname().get_attribute("value")
    actual_last_name = personal_details_page.lastname().get_attribute("value")
    assert actual_first_name == config_data.FIRST_NAME, f"Expected firstName to be '{config_data.FIRST_NAME}', but got '{actual_first_name}'"
    assert actual_last_name == config_data.LAST_NAME, f"Expected lastName to be '{config_data.LAST_NAME}', but got '{actual_last_name}'"
