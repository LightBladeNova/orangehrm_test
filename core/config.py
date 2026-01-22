import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

# Load .env located next to this config file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"), override=False)


@dataclass
class AppConfig:
    """Application configuration with environment variable support and validation"""
    
    # Base URL
    base_url: str = os.getenv("BASE_URL")
    
    # Credentials
    username: str = os.getenv("USERNAME")
    password: str = os.getenv("PASSWORD")
    invalid_username: str = os.getenv("INVALID_USERNAME")
    invalid_password: str = os.getenv("INVALID_PASSWORD")
    
    # Personal Details
    first_name: str = os.getenv("FIRST_NAME")
    last_name: str = os.getenv("LAST_NAME")
    
    # Contact Details
    street_1: str = os.getenv("STREET_1")
    city: str = os.getenv("CITY")
    state: str = os.getenv("STATE")
    zip: str = os.getenv("ZIP")
    work_phone: str = os.getenv("WORK_PHONE")
    
    # Dependent Details
    child_dependent_name: str = os.getenv("CHILD_DEPENDENT_NAME")
    child_dependent_dob: str = os.getenv("CHILD_DEPENDENT_DOB")
    other_dependent_name: str = os.getenv("OTHER_DEPENDENT_NAME")
    other_dependent_dob: str = os.getenv("OTHER_DEPENDENT_DOB")
    other_dependent_relationship: str = os.getenv("OTHER_DEPENDENT_RELATIONSHIP")
    
    # Immigration Record Details
    immigration_number: str = os.getenv("IMMIGRATION_NUMBER")
    immigration_issue_date: str = os.getenv("IMMIGRATION_ISSUE_DATE")
    immigration_expiry_date: str = os.getenv("IMMIGRATION_EXPIRY_DATE")
    immigration_issued_by: str = os.getenv("IMMIGRATION_ISSUED_BY")
    
    # Immigration Attachment Details
    immigration_test_file_name: str = os.getenv("IMMIGRATION_TEST_FILE_NAME")
    immigration_test_file_path: str = field(default_factory=lambda: os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "test_immigration_document.txt"
    ))
    immigration_attachment_content: str = os.getenv("IMMIGRATION_ATTACHMENT_CONTENT")
    
    def __post_init__(self):
        """Validate required configuration fields"""
        required_fields = {
            'base_url': self.base_url,
            'username': self.username,
            'password': self.password,
        }
        
        missing_fields = [field_name for field_name, value in required_fields.items() if not value]
        
        if missing_fields:
            raise ValueError(
                f"Missing required configuration fields: {', '.join(missing_fields)}. "
                f"Please set them via environment variables or provide defaults."
            )

# Create a singleton instance
config = AppConfig()
