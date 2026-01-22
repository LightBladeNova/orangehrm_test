# Test Strategy for OrangeHRM Test Automation

## Overview
This document outlines the test automation strategy for OrangeHRM application, focusing on the My Info module with emphasis on personal details, contact details, dependents, and immigration records management.

## Project Structure

```
orangehrm_test/
├── core/
│   ├── config.py           # Configuration management with .env support
│   └── .env                # Environment variables (gitignored)
├── pages/
│   ├── base_page.py        # Base page object with common methods
│   ├── login.py            # Login page object
│   ├── personal_details.py # Personal details page object
│   ├── contact_details.py  # Contact details page object
│   ├── dependents.py       # Dependents page object
│   └── immigration.py      # Immigration details page object
├── tests/
│   ├── conftest.py         # Pytest fixtures and configuration
│   ├── test_login.py       # Login test cases
│   ├── test_personal_details.py    # Personal details test cases
│   ├── test_contact_details.py     # Contact details test cases
│   ├── test_dependents.py          # Dependents test cases
│   └── test_immigration_details.py # Immigration records test cases
├── tools/
│   └── validate_test_file.py       # Validation utility for test files
├── test_immigration_document.txt   # Test file for immigration attachments
├── requirements.txt        # Python dependencies
└── pytest.ini             # Pytest configuration
```

## Technology Stack

- **Python 3.x**: Core programming language
- **Selenium WebDriver**: Browser automation
- **Pytest**: Test framework
- **pytest-ordering**: Test execution order management
- **pytest-html**: HTML test report generation
- **python-dotenv**: Environment variable management
- **Page Object Model**: Design pattern for maintainability

## Configuration Management

### Environment Variables
All sensitive and environment-specific data is managed through `.env` file:

```ini
# Base Configuration
BASE_URL=https://opensource-demo.orangehrmlive.com

# Credentials
USERNAME=Admin
PASSWORD=admin123
INVALID_USERNAME=InvalidUser
INVALID_PASSWORD=InvalidPass123

# Personal Details
FIRST_NAME=John
LAST_NAME=Doe

# Contact Details
STREET_1=123 Main St
CITY=New York
STATE=New York
ZIP=10001
WORK_PHONE=1234567890

# Dependent Details
CHILD_DEPENDENT_NAME=Kevin
CHILD_DEPENDENT_DOB=2020-01-01
OTHER_DEPENDENT_NAME=Samantha
OTHER_DEPENDENT_DOB=2018-05-15
OTHER_DEPENDENT_RELATIONSHIP=Cousin

# Immigration Record Details
IMMIGRATION_NUMBER=777
IMMIGRATION_ISSUE_DATE=2020-01-01
IMMIGRATION_EXPIRY_DATE=2030-01-01
IMMIGRATION_ISSUED_BY=Afghanistan
IMMIGRATION_TEST_FILE_NAME=test_immigration_document.txt
IMMIGRATION_ATTACHMENT_CONTENT=Test immigration document
```

### Configuration Class
- Centralized `AppConfig` dataclass in `core/config.py`
- Automatic validation of required fields
- Type-safe access to configuration values
- Support for default values and computed paths

## Test Design Pattern

### Page Object Model (POM)
Each page/module has a dedicated page object class:

1. **BasePage**: Common functionality for all pages
   - WebDriver initialization
   - Common waits and interactions
   - Element location strategies
   - Loader handling

2. **LoginPage**: Login functionality
   - Valid/invalid login scenarios
   - Credential management
   - Navigation to dashboard

3. **PersonalDetailsPage**: Personal information management
   - First name and last name updates
   - Field validation
   - Save/cancel operations

4. **ContactDetailsPage**: Contact information management
   - Address fields (street, city, state, zip)
   - Phone number management
   - Field validation and updates

5. **DependentsPage**: Dependent management
   - Add/delete dependent records
   - Multiple relationship types (Child, Other)
   - Date of birth handling
   - Custom relationship specification

6. **ImmigrationPage**: Immigration records management
   - Add/delete immigration records
   - Document number and dates
   - Country of issuance
   - File attachment support
   - Record verification

## Test Execution Strategy

### Test Order and Dependencies
Tests are executed in a specific order using `pytest-ordering` and `pytest-dependency`:

1. **test_login.py** (order=1)
   - Validates authentication
   - Sets up session for subsequent tests
   - Provides `logged_in_browser` fixture

2. **test_personal_details.py** (order=2-3)
   - Depends on: login
   - Tests personal information updates
   - Validates field updates

3. **test_contact_details.py** (order=4)
   - Depends on: login, personal_details
   - Tests contact information management
   - Validates address and phone updates

4. **test_dependents.py** (order=5)
   - Depends on: personal_details, contact_details
   - Tests dependent record management
   - Validates child and other relationship types
   - Verifies record count and data

5. **test_immigration_details.py** (order=6)
   - Depends on: personal_details, contact_details
   - Tests immigration record management
   - Validates document numbers, dates, and country
   - Verifies record table data

### Fixtures

#### Session-scoped Fixtures
- `browser`: WebDriver instance for entire test session
- `logged_in_browser`: Authenticated browser session

#### Function-scoped Fixtures
- Individual page objects as needed
- Test data cleanup

## Test Execution

### Running Tests

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Environment**
   - Create `.env` file in `core/` directory
   - Configure all required environment variables

3. **Validate Test Files**
   ```bash
   python tools/validate_test_file.py
   ```

4. **Run All Tests**
   ```bash
   pytest tests/ -v
   ```

5. **Run Specific Test File**
   ```bash
   pytest tests/test_immigration_details.py -v
   ```

6. **Generate HTML Report**
   ```bash
   pytest tests/ --html=report.html --self-contained-html -v
   ```

7. **Run with Specific Markers**
   ```bash
   pytest tests/ -m "dependency" -v
   ```

### Pytest Configuration (pytest.ini)
```ini
[pytest]
markers =
    dependency: Tests with dependencies on other tests
    run: Tests with specific execution order
addopts = -v --strict-markers
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

## Validation and Assertions

### Test File Validation
- `validate_test_file.py` ensures test files exist with correct content
- Creates missing files automatically
- Validates file content matches expected values
- Returns status: "ok", "created", or "invalid"

### Test Assertions

1. **Personal Details**
   - Verify first name and last name updates
   - Check success toast messages

2. **Contact Details**
   - Verify address fields (street, city, state, zip)
   - Verify work phone number
   - Check success toast messages

3. **Dependents**
   - Verify record count: "(2) Records Found"
   - Verify dependent names in table
   - Check both Child and Other relationship types

4. **Immigration Records**
   - Verify immigration number in table
   - Verify country of issuance
   - Verify issue and expiry dates (both formats)
   - Check record existence after save

## Error Handling

### Exception Management
- Descriptive error messages for page load failures
- Context-specific exception handling
- Failed test cleanup to maintain test independence

### Wait Strategies
- Explicit waits for elements
- Loader disappearance handling
- Dynamic page loading management
- Strategic time.sleep() for UI stability

## Best Practices

1. **Maintainability**
   - Page Object Model for separation of concerns
   - Centralized configuration management
   - Reusable base page methods
   - Type hints for better code documentation

2. **Reliability**
   - Explicit waits over implicit waits
   - Proper exception handling
   - Test independence through cleanup
   - Session-level authentication

3. **Scalability**
   - Modular page objects
   - Environment-based configuration
   - Dependency management between tests
   - Ordered test execution

4. **Reporting**
   - HTML report generation with pytest-html
   - Verbose logging for debugging
   - Clear assertion messages
   - Self-contained HTML reports

## Future Enhancements

1. **Test Coverage**
   - Add negative test scenarios
   - Edge case testing
   - Cross-browser testing
   - Parallel test execution

2. **Reporting**
   - Integration with CI/CD pipelines
   - Screenshot capture on failure
   - Video recording of test execution
   - Allure reporting integration

3. **Data Management**
   - Test data factories
   - Database validation
   - API integration for data setup
   - Dynamic test data generation

4. **Performance**
   - Parallel test execution with pytest-xdist
   - Optimized wait strategies
   - Resource pooling
   - Test execution time monitoring

## Dependencies

```txt
attrs==25.4.0
certifi==2026.1.4
h11==0.16.0
idna==3.11
iniconfig==2.3.0
outcome==1.3.0.post0
packaging==25.0
pluggy==1.6.0
Pygments==2.19.2
PySocks==1.7.1
pytest==9.0.2
pytest-html==4.1.1
pytest-ordering==1.2.1
python-dotenv==1.0.1
selenium==4.39.0
sniffio==1.3.1
sortedcontainers==2.4.0
trio==0.32.0
trio-websocket==0.12.2
typing_extensions==4.15.0
urllib3==2.6.3
websocket-client==1.9.0
wsproto==1.3.2
```

## Conclusion

This test strategy provides a robust, maintainable, and scalable framework for automating OrangeHRM tests. The combination of Page Object Model, pytest features, and proper configuration management ensures reliable test execution and easy maintenance.
