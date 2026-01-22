"""
Validation script for test_immigration_document.txt
Confirms the file exists with expected content, creates it if missing.
"""
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def validate_test_file() -> str:
    """
    Validate test_immigration_document.txt exists with expected content.
    Creates it if missing.
    Returns: "ok" | "created" | "invalid"
    """
    # Path to test file (in project root)
    project_root = Path(__file__).resolve().parents[1]
    test_file = project_root / "test_immigration_document.txt"
    expected_content = "Test immigration document"

    # Check if file exists
    if test_file.exists():
        # Verify content
        try:
            actual_content = test_file.read_text(encoding="utf-8")
            if actual_content == expected_content:
                logger.info(f"✓ File exists with correct content: {test_file}")
                return "ok"
            else:
                logger.error(
                    f"✗ File exists but content mismatch. Expected: '{expected_content}', "
                    f"Got: '{actual_content}'"
                )
                return "invalid"
        except Exception as e:
            logger.error(f"✗ Error reading file: {e}")
            return "invalid"
    else:
        # Create file with expected content
        try:
            test_file.write_text(expected_content, encoding="utf-8")
            logger.info(f"✓ Created test file: {test_file}")
            return "created"
        except Exception as e:
            logger.error(f"✗ Error creating file: {e}")
            return "invalid"


if __name__ == "__main__":
    status = validate_test_file()
    logger.info(f"Status: {status}")
    exit(0 if status != "invalid" else 1)
