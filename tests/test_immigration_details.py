import time
import pytest
from core.config import config
from pages.immigration import Immigration


@pytest.mark.dependency(depends=["personal_details", "contact_details"], name="immigration_details", scope="session")
@pytest.mark.run(order=6)
def test_add_immigration_details(logged_in_browser):
    """Test adding immigration record in My Info page"""
    try:
        immigration_page = Immigration(logged_in_browser)
        immigration_page.click_myinfo()
        immigration_page.click_immigration_tab()
    except Exception as exc:
        raise Exception(f"Immigration page failed to load: {exc}") from exc

    immigration_page.wait_for_loader_to_disappear()
    immigration_page.delete_existing_immigration_record()
    immigration_page.wait_for_loader_to_disappear()
    time.sleep(3)

    immigration_page.click_add_immigration_record_button()
    immigration_page.click_save_button_input_error()
    immigration_page.fill_number(config.immigration_number)
    immigration_page.fill_issue_date(config.immigration_issue_date)
    immigration_page.fill_expiry_date(config.immigration_expiry_date)
    immigration_page.click_issued_by_dropdown()
    immigration_page.click_afghanistan_option()
    immigration_page.click_save_button_and_verify()
    immigration_page.wait_for_loader_to_disappear()
    time.sleep(3)

    immigration_record_table = immigration_page.immigration_record_table()
    assert config.immigration_number in immigration_record_table.text, "Immigration record '777' not found in immigration list"
    assert config.immigration_issued_by in immigration_record_table.text, "Immigration record 'Afghanistan' not found in immigration list"
    assert config.immigration_issue_date in immigration_record_table.text or "01-01-2020" in immigration_record_table.text, "Immigration record '2020-01-01' not found in immigration list"
    assert config.immigration_expiry_date in immigration_record_table.text or "01-01-2030" in immigration_record_table.text, "Immigration record '2030-01-01' not found in immigration list"
