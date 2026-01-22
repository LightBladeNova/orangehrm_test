import os
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class AppConfig:
    """Application configuration with environment variable support and validation"""
    
    # Base URL
    base_url: str = field(default_factory=lambda: os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"))
    
    # Credentials
    username: str = field(default_factory=lambda: os.getenv("USERNAME", "Admin"))
    password: str = field(default_factory=lambda: os.getenv("PASSWORD", "admin123"))
    invalid_username: str = field(default_factory=lambda: os.getenv("INVALID_USERNAME", "InvalidUser"))
    invalid_password: str = field(default_factory=lambda: os.getenv("INVALID_PASSWORD", "InvalidPass"))
    
    # Personal Details
    first_name: str = field(default_factory=lambda: os.getenv("FIRST_NAME", "John"))
    last_name: str = field(default_factory=lambda: os.getenv("LAST_NAME", "Doe"))
    
    # Contact Details
    street_1: str = field(default_factory=lambda: os.getenv("STREET_1", "2600 Great America Way"))
    city: str = field(default_factory=lambda: os.getenv("CITY", "Santa Clara"))
    state: str = field(default_factory=lambda: os.getenv("STATE", "California"))
    zip: str = field(default_factory=lambda: os.getenv("ZIP", "95054"))
    work_phone: str = field(default_factory=lambda: os.getenv("WORK_PHONE", "4087330480"))
    
    # Dependent Details
    child_dependent_name: str = field(default_factory=lambda: os.getenv("CHILD_DEPENDENT_NAME", "Kevin"))
    child_dependent_dob: str = field(default_factory=lambda: os.getenv("CHILD_DEPENDENT_DOB", "2015-01-01"))
    other_dependent_name: str = field(default_factory=lambda: os.getenv("OTHER_DEPENDENT_NAME", "Samantha"))
    other_dependent_dob: str = field(default_factory=lambda: os.getenv("OTHER_DEPENDENT_DOB", "1980-01-01"))
    other_dependent_relationship: str = field(default_factory=lambda: os.getenv("OTHER_DEPENDENT_RELATIONSHIP", "Mother"))
    
    # Immigration Record Details
    immigration_number: str = field(default_factory=lambda: os.getenv("IMMIGRATION_NUMBER", "777"))
    immigration_issue_date: str = field(default_factory=lambda: os.getenv("IMMIGRATION_ISSUE_DATE", "2020-01-01"))
    immigration_expiry_date: str = field(default_factory=lambda: os.getenv("IMMIGRATION_EXPIRY_DATE", "2030-01-01"))
    immigration_issued_by: str = field(default_factory=lambda: os.getenv("IMMIGRATION_ISSUED_BY", "Afghanistan"))
    
    # Immigration Attachment Details
    immigration_test_file_name: str = field(default_factory=lambda: os.getenv("IMMIGRATION_TEST_FILE_NAME", "test_immigration_document"))
    immigration_test_file_path: str = field(default_factory=lambda: os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "test_immigration_document.txt"
    ))
    immigration_attachment_content: str = field(default_factory=lambda: os.getenv("IMMIGRATION_ATTACHMENT_CONTENT", "Test immigration document"))
    
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
    
    @classmethod
    def from_env(cls):
        """Load configuration from environment variables"""
        return cls()


# Create a singleton instance
config = AppConfig()
