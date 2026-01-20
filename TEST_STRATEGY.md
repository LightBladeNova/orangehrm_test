# OrangeHRM Test Strategy - Technical Requirements Document

**Project:** OrangeHRM Employee Information System Testing  
**Testing Framework:** Selenium with pytest  

---

## Table of Contents
1. [Overview](#overview)
2. [Test Objectives](#test-objectives)
3. [Test Scope](#test-scope)
4. [Test Architecture](#test-architecture)
5. [Test Cases](#test-cases)
6. [Helper Functions & Utilities](#helper-functions--utilities)

---

## Overview

This document outlines the comprehensive test strategy for validating the OrangeHRM Employee Information System. The test suite focuses on critical employee information management workflows using Selenium WebDriver automation framework with Python and pytest.

**Target Application:** OrangeHRM (Open Source Human Resource Management System)  
**URL:** `https://opensource-demo.orangehrmlive.com`  
**Testing Approach:** Functional Testing

---

## Test Objectives

1. **Validate Authentication Flow**
   - Verify successful login with valid credentials
   - Confirm rejection of invalid credentials with appropriate error messaging

2. **Validate Employee Information Management**
   - Test updating personal details (first name, last name)
   - Test updating contact information (address, phone numbers)
   - Verify data persistence across page navigation

3. **Validate Dependent Management**
   - Test adding multiple dependents with different relationships
   - Test validation requirements (mandatory fields)
   - Test duplicate dependent handling
   - Test deletion of existing dependents

4. **Validate Immigration Document Management**
   - Test file upload functionality for immigration documents
   - Test file download capability
   - Test file deletion functionality
   - Verify file content integrity after download

5. **Validate UI Responsiveness & Element Interaction**
   - Ensure robust element detection with multiple selector strategies
   - Handle dynamic loading overlays (form loaders)
   - Manage asynchronous element updates
   - Handle stale element references

---

## Test Scope

### In Scope
- Authentication (login/logout)
- Personal Information Tab
- Contact Information Tab
- Dependents Tab
- Immigration Documents Tab
- File upload and download operations
- CRUD operations for employee information
- Form validation and error handling
- Data persistence verification

### Out of Scope
- Performance testing (load/stress testing)
- Security testing (SQL injection, XSS, etc.)
- Browser compatibility testing beyond Chrome

---

## Test Architecture

### Technology Stack
```
Language:           Python 3.14+
Web Driver:         Selenium 4.x
Test Framework:     pytest 9.x
Browser:            Google Chrome (latest)
Operating System:   macOS (primary), cross-platform compatible
```

### Project Structure
```
orangehrm_test/
├── orangehrm_test.py      # Main test cases
├── requirements.txt        # Project dependencies
├── TEST_STRATEGY.md        # This document
├── .venv/                  # Python virtual environment
├── config/
│   ├── config_data.py      # Test data and configuration constants
│   └── __pycache__/
├── pages/
│   ├── login.py            # LoginPage class for authentication
│   ├── personal_details.py # PersonalDetails class
│   ├── contact_details.py  # ContactDetails class
│   ├── dependents.py       # Dependents class
│   ├── immigration.py      # Immigration class
│   └── __pycache__/
├── utils/
│   ├── helpers.py          # Shared helper functions
│   └── __pycache__/
└── __pycache__/
```

### Key Dependencies
- `selenium==4.x` - WebDriver automation
- `pytest==9.x` - Test framework
- `pytest-xdist` - Parallel test execution (optional)

---

## Configuration & Test Data

### ConfigData Module (`config/config_data.py`)

The ConfigData module centralizes all test data and configuration constants, ensuring maintainability and easy updates.

#### Constants

**Application Configuration:**
- `BASE_URL` - Login page URL: `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login`

**Authentication Data:**
- `USERNAME` - Valid admin username: "Admin"
- `PASSWORD` - Valid admin password: "admin123"
- `INVALID_USERNAME` - Invalid username for testing: "InvalidUser"
- `INVALID_PASSWORD` - Invalid password for testing: "InvalidPass"

**Personal Details Test Data:**
- `FIRST_NAME` - "John"
- `LAST_NAME` - "Doe"

**Contact Details Test Data:**
- `STREET_1` - "2600 Great America Way"
- `CITY` - "Santa Clara"
- `STATE` - "California"
- `ZIP` - "95054"
- `WORK_PHONE` - "4087330480"

**Dependent Details Test Data:**
- `CHILD_DEPENDENT_NAME` - "Kevin"
- `CHILD_DEPENDENT_DOB` - "2015-01-01"
- `OTHER_DEPENDENT_NAME` - "Samantha"
- `OTHER_DEPENDENT_DOB` - "1980-01-01"
- `OTHER_DEPENDENT_RELATIONSHIP` - "Mother"

**Immigration Record Test Data:**
- `IMMIGRATION_NUMBER` - "777"
- `IMMIGRATION_ISSUE_DATE` - "2020-01-01"
- `IMMIGRATION_EXPIRY_DATE` - "2030-01-01"
- `IMMIGRATION_ISSUED_BY` - "Afghanistan"
- `IMMIGRATION_TEST_FILE_PATH` - "/tmp/test_immigration_document.txt"
- `IMMIGRATION_ATTACHMENT_CONTENT` - "Test immigration document"

---

## Page Object Classes

### Overview
Page Object Model (POM) is implemented to encapsulate page-specific elements and interactions. Each page has a corresponding class in the `pages/` directory.

### 1. LoginPage Class (`pages/login.py`)
**Purpose:** Handles authentication interactions on the login page

**Attributes:**
- `driver` - Selenium WebDriver instance

**Methods:**

#### `navigate_to_login_page()`
- Navigates to the login URL defined in config
- Returns: None

#### `fill_username(username)`
- Locates username field (name="username")
- Clears any existing value
- Enters the provided username
- Returns: None

#### `fill_password(password)`
- Locates password field (name="password")
- Clears any existing value
- Enters the provided password
- Returns: None

#### `click_login()`
- Locates and clicks the submit button
- Returns: None

#### `get_invalid_credentials_error()`
- Retrieves error message displayed on failed login
- Returns: WebElement containing error text

---

### 2. PersonalDetails Class (`pages/personal_details.py`)
**Purpose:** Manages personal information tab interactions

**Attributes:**
- `driver` - Selenium WebDriver instance

**Methods:**

#### `click_myinfo()`
- Navigates to My Info section
- Uses href containing '/web/index.php/pim/viewMyDetails'
- Returns: None

#### `firstname()`
- Returns WebElement for first name input field
- Uses locator: name="firstName"
- Waits until element is clickable (10s timeout)

#### `lastname()`
- Returns WebElement for last name input field
- Uses locator: name="lastName"
- Waits until element is clickable (10s timeout)

#### `fill_firstname(firstname)`
- Fills first name field using helper function
- Includes 1-second delay for stability
- Parameters: firstname (str)
- Returns: None

#### `fill_lastname(lastname)`
- Fills last name field using helper function
- Includes 1-second delay for stability
- Parameters: lastname (str)
- Returns: None

---

### 3. ContactDetails Class (`pages/contact_details.py`)
**Purpose:** Manages contact information tab interactions

**Attributes:**
- `driver` - Selenium WebDriver instance

**Methods:**

#### `click_myinfo()`
- Navigates to My Info section
- Returns: None

#### `click_contact_details_tab()`
- Navigates to Contact Details tab
- Uses href containing '/web/index.php/pim/contactDetails/empNumber/7'
- Returns: None

#### `street1()`
- Returns WebElement for Street 1 input field
- Waits until element is clickable (10s timeout)

#### `city()`
- Returns WebElement for City input field
- Waits until element is clickable (10s timeout)

#### `state()`
- Returns WebElement for State/Province input field
- Waits until element is clickable (10s timeout)

#### `zip()`
- Returns WebElement for Zip/Postal Code input field
- Waits until element is clickable (10s timeout)

#### `work_phone()`
- Returns WebElement for Work phone input field
- Waits until element is clickable (10s timeout)

#### `fill_street1(street1)`
- Fills Street 1 field
- Parameters: street1 (str)

#### `fill_city(city)`
- Fills City field
- Parameters: city (str)

#### `fill_state(state)`
- Fills State/Province field
- Parameters: state (str)

#### `fill_zip(zip)`
- Fills Zip/Postal Code field
- Parameters: zip (str)

#### `fill_work_phone(phone)`
- Fills Work phone field
- Parameters: phone (str)

---

### 4. Dependents Class (`pages/dependents.py`)
**Purpose:** Manages dependent information tab interactions

**Attributes:**
- `driver` - Selenium WebDriver instance

**Methods:**

#### `click_myinfo()`
- Navigates to My Info section
- Returns: None

#### `click_dependents_tab()`
- Navigates to Dependents tab
- Uses href containing '/web/index.php/pim/viewDependents/empNumber/7'
- Returns: None

#### `delete_existing_dependents()`
- Deletes all existing dependent records
- Iterates through all Delete buttons (i.oxd-icon.bi-trash)
- Confirms each deletion
- Waits for loader to disappear between deletions
- Handles exceptions gracefully if no dependents exist
- Returns: None

#### `click_add_dependent()`
- Clicks the Add button to create new dependent
- Returns: None

#### `click_relationship_dropdown()`
- Opens the relationship dropdown selector
- Returns: None

#### `click_child_relationship_option()`
- Selects "Child" from relationship dropdown (2nd option)
- Returns: None

#### `click_other_relationship_option()`
- Selects "Other" from relationship dropdown (3rd option)
- Returns: None

#### `fill_name(name)`
- Fills dependent name field
- Waits for element and uses fill_input helper
- Parameters: name (str)
- Returns: None

#### `fill_dob(dob)`
- Fills Date of Birth field
- Waits for element and uses fill_input helper
- Parameters: dob (str, format: "YYYY-MM-DD")
- Returns: None

#### `fill_relationship(relationship)`
- Fills relationship description field (for "Other" relationship type)
- Parameters: relationship (str)
- Returns: None

#### `dependents_records()`
- Returns text element showing record count
- Returns: WebElement

#### `dependents_table()`
- Returns the table body containing dependent records
- Returns: WebElement

---

### 5. Immigration Class (`pages/immigration.py`)
**Purpose:** Manages immigration records and attachments tab interactions

**Attributes:**
- `driver` - Selenium WebDriver instance

**Methods:**

#### `click_myinfo()`
- Navigates to My Info section
- Returns: None

#### `click_immigration_tab()`
- Navigates to Immigration tab
- Uses XPath with text matching "Immigration"
- Returns: None

#### `delete_existing_immigration_record()`
- Deletes existing immigration record
- Clicks first Delete button (index 0)
- Confirms deletion
- Handles exceptions gracefully
- Returns: None

#### `delete_existing_immigration_attachment()`
- Deletes existing immigration attachment
- Clicks second Delete button (index 1)
- Confirms deletion
- Handles exceptions gracefully
- Returns: None

#### `click_add_immigration_record_button()`
- Clicks first Add button to create immigration record
- Returns: None

#### `click_add_immigration_attachment_button()`
- Clicks second Add button to create immigration attachment
- Returns: None

#### `fill_number(number)`
- Fills Document Number field
- Parameters: number (str)
- Returns: None

#### `fill_issue_date(issue_date)`
- Fills Issue Date field
- Parameters: issue_date (str, format: "YYYY-MM-DD")
- Returns: None

#### `fill_expiry_date(expiry_date)`
- Fills Expiry Date field
- Parameters: expiry_date (str, format: "YYYY-MM-DD")
- Returns: None

#### `click_issued_by_dropdown()`
- Opens the Issued By country dropdown
- Returns: None

#### `click_afghanistan_option()`
- Selects "Afghanistan" from Issued By dropdown (2nd option)
- Returns: None

#### `immigration_record_table()`
- Returns the table body containing immigration records
- Returns: WebElement

#### `upload_attachment_file(file_path)`
- Uploads file to immigration attachment
- Locates file input element (type='file')
- Sends absolute file path
- Parameters: file_path (str)
- Returns: None

#### `download_attachment_file()`
- Initiates download of immigration attachment
- Clicks download icon button
- Returns: None

---

## Test Cases

### 1. Authentication Tests

#### TC-001: Valid Credentials Login
**Objective:** Verify successful login with valid credentials

**Preconditions:**
- Browser is open on login page
- Valid credentials available (Admin / admin123)

**Steps:**
1. Navigate to OrangeHRM login page
2. Enter username: "Admin"
3. Enter password: "admin123"
4. Click login button

**Expected Results:**
- User is redirected to dashboard
- URL contains "/dashboard"
- No error messages displayed

**Test Function:** `test_login_success()`  

---

#### TC-002: Invalid Credentials Login
**Objective:** Verify login rejection with invalid credentials

**Preconditions:**
- Browser is open on login page

**Steps:**
1. Navigate to OrangeHRM login page
2. Enter username: "Hello"
3. Enter password: "World"
4. Click login button

**Expected Results:**
- Login fails with error alert
- Alert text contains "Invalid credentials"
- URL does not contain "/dashboard"
- User remains on login page

**Test Function:** `test_login_fail()`  

---

### 2. Personal Information Tests

#### TC-003: Update Personal Details
**Objective:** Verify ability to update employee first and last name

**Preconditions:**
- User is logged in with valid credentials
- My Info page is accessible

**Steps:**
1. Login with valid credentials
2. Navigate to My Info page
3. Wait for page loader to disappear
4. Fill firstName field with "John"
5. Fill lastName field with "Doe"
6. Click save button
7. Verify success message appears
8. Retrieve and validate saved values

**Expected Results:**
- firstName field value = "John"
- lastName field value = "Doe"
- Success toast notification displayed
- Data persists after page reload

**Test Function:** `test_add_personal_details()`  

---

### 3. Contact Information Tests

#### TC-004: Update Contact Details
**Objective:** Verify ability to update employee contact information

**Preconditions:**
- User is logged in with valid credentials
- Contact Details tab is available

**Test Data:**
| Field | Value |
|-------|-------|
| Street 1 | 2600 Great America Way |
| Street 2 | 330 Potrero Ave |
| City | Santa Clara |
| State | CA |
| Zip Code | 95054 |
| Work Phone | 4087330480 |

**Steps:**
1. Login with valid credentials
2. Navigate to My Info → Contact Details
3. Wait for form to load
4. Fill all address fields with test data
5. Click save button
6. Verify success message

**Expected Results:**
- All fields updated with correct values
- Success toast notification displayed
- Form state persists after navigation away and back

**Test Function:** `test_add_contact_details()`  

---

### 4. Dependents Management Tests

#### TC-005: Add Multiple Dependents
**Objective:** Verify ability to add multiple dependents with validation

**Preconditions:**
- User is logged in
- Dependents tab is accessible
- Any existing dependents are deleted first

**Test Data:**
| Dependent | Relationship | Name | DOB |
|-----------|--------------|------|-----|
| 1 | Child | Kevin | 2015-01-01 |
| 2 | Other | Samantha | 1980-01-01 |

**Steps:**
1. Login and navigate to My Info → Dependents
2. Delete any existing dependents
3. Add first dependent (Child - Kevin)
   - Click Add button
   - Verify validation error on save without required fields
   - Select relationship from dropdown
   - Fill name and DOB
   - Save and verify success
4. Add second dependent (Other - Samantha)
   - Click Add button
   - Select relationship
   - Fill name and relationship description
   - Fill DOB
   - Save and verify success
5. Verify record count shows (2) Records Found
6. Verify both names appear in dependent list

**Expected Results:**
- Validation prevents empty form submission
- Both dependents successfully added
- Record count displays correctly
- Both dependents visible in table

**Test Function:** `test_add_dependents()`  

---

### 5. Immigration Records Tests

#### TC-006: Add Immigration Records
**Objective:** Verify ability to add immigration records with validation

**Preconditions:**
- User is logged in
- Immigration tab is accessible
- Any existing immigration records are deleted first

**Test Data:**
| Field | Value |
|-------|-------|
| Document Number | 777 |
| Issue Date | 2020-01-01 |
| Expiry Date | 2030-01-01 |
| Issued By | Afghanistan |

**Steps:**
1. Login and navigate to My Info → Immigration
2. Wait for page to fully load
3. Delete any existing immigration records
4. Click Add button to add new immigration record
5. Verify validation error on save without required fields
6. Fill document number field with "777"
7. Fill issue date field with "2020-01-01"
8. Fill expiry date field with "2030-01-01"
9. Select "Afghanistan" from Issued By dropdown
10. Click save button and verify success notification
11. Wait for page to reload
12. Verify record appears in immigration records table
13. Verify all fields display correctly in table

**Expected Results:**
- Validation prevents empty form submission
- Record successfully added with all fields populated
- Success notification displayed after save
- Record visible in table with correct values:
  - Document Number: "777"
  - Issue Date: "2020-01-01"
  - Expiry Date: "2030-01-01"
  - Issued By: "Afghanistan"

**Test Function:** `test_add_immigration_details()`  

---

### 6. Immigration Attachments Tests

#### TC-007: Upload and Download Immigration Document Attachment
**Objective:** Verify file upload, deletion, and download functionality for immigration documents

**Preconditions:**
- User is logged in
- Immigration tab is accessible
- Test file exists or can be created

**Steps:**
1. Login and navigate to My Info → Immigration
2. Wait for page to fully load
3. Delete any existing immigration attachments (if present)
4. Create test file with content: "Test immigration document"
5. Click Add button to add new immigration attachment record
6. Upload test file via file input
7. Save the record and verify success notification
8. Record file timestamps in Downloads folder BEFORE download
9. Click download icon on immigration attachment record
10. Wait for download to complete
11. Verify new/modified file appeared in Downloads
12. Read downloaded file and verify content matches uploaded file

**Expected Results:**
- File successfully uploaded without errors
- Success notification displayed after save
- File download initiated when download icon clicked
- Downloaded file exists with correct modification time
- Downloaded file content matches original

**Test Function:** `test_add_immigration_attachment()`  

---

## Helper Functions & Utilities

### Core Helper Functions

#### 1. `login(driver, username, password)`
**Purpose:** Authenticate user to OrangeHRM system

**Parameters:**
- `driver` (WebDriver): Selenium WebDriver instance
- `username` (str): Login username
- `password` (str): Login password

**Implementation Details:**
- Navigates to login URL
- Enters credentials into form fields
- Clicks submit button
- Returns control when authentication complete

---

#### 2. `wait_for_loader_to_disappear(driver, timeout=10)`
**Purpose:** Handle asynchronous form loader overlays

**Parameters:**
- `driver` (WebDriver): Selenium WebDriver instance
- `timeout` (int): Maximum wait time in seconds (default: 10)

**Behavior:**
- Waits for `div.oxd-form-loader` to become invisible
- Prevents element interaction while loading
- Raises TimeoutException if loader persists

---

#### 3. `wait_for_element_to_be_clickable(driver, by, locator, timeout=5)`
**Purpose:** Wait for element to be in clickable state

**Parameters:**
- `driver` (WebDriver): Selenium WebDriver instance
- `by` (By): Locator strategy (By.NAME, By.CSS_SELECTOR, etc.)
- `locator` (str): Element locator value
- `timeout` (int): Maximum wait time in seconds

**Returns:** WebElement that is clickable

---

#### 4. `fill_input(driver, webelement, value, timeout=10, attempts=3)`
**Purpose:** Robustly fill input fields with data, handling various clearing methods

**Parameters:**
- `driver` (WebDriver): Selenium WebDriver instance
- `webelement` (WebElement): Target input element
- `value` (str): Text to enter
- `timeout` (int): Timeout per attempt
- `attempts` (int): Number of retry attempts

**Clearing Strategy (Multiple Methods):**
1. Send Ctrl+A followed by Delete
2. JavaScript `element.value = ''`
3. Standard element.clear()
4. Click element first to ensure focus

**Error Handling:**
- Retries on StaleElementReferenceException
- Retries on ElementClickInterceptedException
- Returns True/False based on success

---

#### 5. `click_save_button_and_verify(driver, timeout=5)`
**Purpose:** Click save button and verify success notification

**Implementation:**
1. Locates save button (type='submit')
2. Clicks the button
3. Waits for success toast (class='oxd-toast--success')
4. Asserts success message appeared
5. Raises AssertionError if no success notification

---

### Environment Setup
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest orangehrm_test.py -v
```
