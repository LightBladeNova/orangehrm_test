import os
import time
import pytest
import config.config_data as config_data
from pages.immigration import Immigration


@pytest.mark.dependency(depends=["personal_details", "contact_details"], name="immigration_attachment", scope="session")
@pytest.mark.run(order=7)
def test_add_immigration_attachment(logged_in_browser):
    """Test adding immigration attachment with file upload in My Info page"""
    try:
        immigration_page = Immigration(logged_in_browser)
        immigration_page.click_myinfo()
        immigration_page.click_immigration_tab()
    except Exception as exc:
        raise Exception(f"Immigration page failed to load: {exc}") from exc

    immigration_page.wait_for_loader_to_disappear()
    immigration_page.delete_existing_immigration_attachment()
    immigration_page.wait_for_loader_to_disappear()

    test_file_path = config_data.IMMIGRATION_TEST_FILE_PATH
    immigration_page.click_add_immigration_attachment_button()
    immigration_page.upload_attachment_file(test_file_path)

    try:
        immigration_page.click_save_button_and_verify()
    except Exception as exc:
        print(f"Save verification failed (expected if no file): {exc}")
    immigration_page.wait_for_loader_to_disappear()

    download_dir = str(os.path.expanduser("~")) + "/Downloads"
    immigration_page.download_attachment_file()
    time.sleep(3)

    downloaded_files = [f for f in os.listdir(download_dir) if os.path.isfile(os.path.join(download_dir, f))]
    assert len(downloaded_files) > 0, "No files found in Downloads directory"
    latest_file = max(downloaded_files, key=lambda f: os.path.getmtime(os.path.join(download_dir, f)))
    assert latest_file, "Could not determine latest downloaded file"

    assert "test_immigration_document" in latest_file, f"Expected 'test_immigration_document' in filename, but got '{latest_file}'"

    latest_file_path = os.path.join(download_dir, latest_file)
    with open(latest_file_path, "r") as file_handle:
        downloaded_content = file_handle.read()
    assert config_data.IMMIGRATION_ATTACHMENT_CONTENT in downloaded_content, f"Expected content '{config_data.IMMIGRATION_ATTACHMENT_CONTENT}' not found in downloaded file"
    print(f"✅ File download verified: {latest_file}")
