import pytest
from core.config import config
from pages.dependents import Dependents


@pytest.mark.dependency(depends=["personal_details", "contact_details"], name="dependents", scope="session")
@pytest.mark.run(order=5)
def test_add_dependents(logged_in_browser):
    try:
        dependents_page = Dependents(logged_in_browser)
        dependents_page.click_myinfo()
        dependents_page.click_dependents_tab()
    except Exception as exc:
        raise Exception(f"Dependents page failed to load: {exc}") from exc

    dependents_page.wait_for_loader_to_disappear()
    dependents_page.delete_existing_dependents()

    dependents_page.click_add_dependent()
    dependents_page.click_save_button_input_error()
    dependents_page.click_relationship_dropdown()
    dependents_page.click_child_relationship_option()
    dependents_page.fill_name(config.child_dependent_name)
    dependents_page.fill_dob(config.child_dependent_dob)
    dependents_page.click_save_button_and_verify()
    dependents_page.wait_for_loader_to_disappear()

    dependents_page.click_add_dependent()
    dependents_page.click_relationship_dropdown()
    dependents_page.click_other_relationship_option()
    dependents_page.fill_name(config.other_dependent_name)
    dependents_page.fill_relationship(config.other_dependent_relationship)
    dependents_page.fill_dob(config.other_dependent_dob)
    dependents_page.click_save_button_and_verify()
    dependents_page.wait_for_loader_to_disappear()

    dependent_records = dependents_page.dependents_records()
    assert "(2) Records Found" in dependent_records.text, "Expected 2 dependents, but record count mismatch"
    dependents_table = dependents_page.dependents_table()
    assert config.child_dependent_name in dependents_table.text, "Dependent 'Kevin' not found in dependents list"
    assert config.other_dependent_name in dependents_table.text, "Dependent 'Samantha' not found in dependents list"
