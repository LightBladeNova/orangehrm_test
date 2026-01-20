# Credentials and URL for OrangeHRM tests
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
INVALID_USERNAME = "InvalidUser"
INVALID_PASSWORD = "InvalidPass"
USERNAME = "Admin"
PASSWORD = "admin123"

# Personal Details
FIRST_NAME = "John"
LAST_NAME = "Doe"

# Contact Details
STREET_1 = "2600 Great America Way"
CITY = "Santa Clara"
STATE = "California"
ZIP = "95054"
WORK_PHONE = "4087330480"

# Dependent Details
CHILD_DEPENDENT_NAME = "Kevin"
CHILD_DEPENDENT_DOB = "2015-01-01"
OTHER_DEPENDENT_NAME = "Samantha"
OTHER_DEPENDENT_DOB = "1980-01-01"
OTHER_DEPENDENT_RELATIONSHIP = "Mother"

# Immigration Record Details
IMMIGRATION_NUMBER = "777"
IMMIGRATION_ISSUE_DATE = "2020-01-01"
IMMIGRATION_EXPIRY_DATE = "2030-01-01"
IMMIGRATION_ISSUED_BY = "Afghanistan"

# Immigration Attachment Details
import os
IMMIGRATION_TEST_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "test_immigration_document.txt")
IMMIGRATION_ATTACHMENT_CONTENT = "Test immigration document"