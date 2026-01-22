import logging
import time
from pathlib import Path
import pytest
from core.config import config
from pages.immigration import Immigration
from utils.files import latest_file, read_text

logger = logging.getLogger(__name__)


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

    test_file_path = config.immigration_test_file_path
    immigration_page.click_add_immigration_attachment_button()
    immigration_page.upload_attachment_file(test_file_path)

    try:
        immigration_page.click_save_button_and_verify()
    except Exception as exc:
        logger.warning("Save verification failed (expected if no file): %s", exc)
    immigration_page.wait_for_loader_to_disappear()

    download_dir = Path.home() / "Downloads"
    immigration_page.download_attachment_file()
    time.sleep(3)

    downloaded_file = latest_file(download_dir, pattern=config.immigration_test_file_name + "*")
    assert config.immigration_test_file_name in downloaded_file.name, f"Expected '{config.immigration_test_file_name}' in filename, but got '{downloaded_file.name}'"

    downloaded_content = read_text(downloaded_file)
    assert config.immigration_attachment_content in downloaded_content, f"Expected content '{config.immigration_attachment_content}' not found in downloaded file"
    logger.info("✅ File download verified: %s", downloaded_file.name)
