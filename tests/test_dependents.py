import pytest
import config.config_data as config_data
from pages.dependents import Dependents


@pytest.mark.dependency(depends=["personal_details", "contact_details"], name="dependents", scope="session")
@pytest.mark.run(order=5)
def test_add_dependents(logged_in_browser):
    """Test adding dependents in My Info page"""
    try:
        dependents_page = Dependents(logged_in_browser)
        dependents_page.click_myinfo()
        dependents_page.click_dependents_tab()
    except Exception as exc:
        raise Exception(f"Dependents page failed to load: {exc}") from exc

    dependents_page.delete_existing_dependents()

    dependents_page.click_add_dependent()
    dependents_page.click_save_button_input_error()
    dependents_page.click_relationship_dropdown()
    dependents_page.click_child_relationship_option()
    dependents_page.fill_name(config_data.CHILD_DEPENDENT_NAME)
    dependents_page.fill_dob(config_data.CHILD_DEPENDENT_DOB)
    dependents_page.click_save_button_and_verify()
    dependents_page.wait_for_loader_to_disappear()

    dependents_page.click_add_dependent()
    dependents_page.click_relationship_dropdown()
    dependents_page.click_other_relationship_option()
    dependents_page.fill_name(config_data.OTHER_DEPENDENT_NAME)
    dependents_page.fill_relationship(config_data.OTHER_DEPENDENT_RELATIONSHIP)
    dependents_page.fill_dob(config_data.OTHER_DEPENDENT_DOB)
    dependents_page.click_save_button_and_verify()
    dependents_page.wait_for_loader_to_disappear()

    dependent_records = dependents_page.dependents_records()
    assert "(2) Records Found" in dependent_records.text, "Expected 2 dependents, but record count mismatch"
    dependents_table = dependents_page.dependents_table()
    assert config_data.CHILD_DEPENDENT_NAME in dependents_table.text, "Dependent 'Kevin' not found in dependents list"
    assert config_data.OTHER_DEPENDENT_NAME in dependents_table.text, "Dependent 'Samantha' not found in dependents list"
