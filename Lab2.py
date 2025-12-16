# ============================================================
# SET A: THE DATA FORMATTER
# ============================================================

print("=" * 60)
print("SET A: THE DATA FORMATTER")
print("=" * 60)

# --------------------------------------------------
# 1. Slicing & Methods: Extract and format names
# --------------------------------------------------
print("\n--- Task 1: Name Extraction ---")

# Get user input
full_name = input("Enter your full name (first and last): ")

# Remove extra spaces and split into parts
full_name = full_name.strip()  # Remove leading/trailing spaces
name_parts = full_name.split()  # Split by whitespace

# Extract first and last name
first_name = name_parts[0].strip().capitalize()  # First word
last_name = name_parts[-1].strip().capitalize()  # Last word

# Print results
print(f"\nFirst Name: {first_name}")
print(f"Last Name: {last_name}")

# --------------------------------------------------
# 2. Formatting: Create formatted filename
# --------------------------------------------------
print("\n--- Task 2: File Name Formatting ---")

# Use fixed timestamp
timestamp = "20241006"

# Create filename using f-string (lowercase names with underscore)
file_name = f"{first_name.lower()}_{last_name.lower()}_report_{timestamp}.txt"

print(f"Generated filename: {file_name}")

# --------------------------------------------------
# 3. Validation & Search: Password Validator
# --------------------------------------------------
print("\n--- Task 3: Password Validation ---")

def is_valid_password(password):
    """
    Check if password is valid:
    - At least 8 characters long
    - Contains at least one digit
    Returns True if valid, False otherwise.
    """
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    
    return has_digit

# Alternative using any():
def is_valid_password_v2(password):
    """Alternative implementation using any()"""
    return len(password) >= 8 and any(char.isdigit() for char in password)

# Test the function
test_passwords = ["hello", "password", "secure1234", "abc123", "MyPass9"]

print("Password Validation Tests:")
for pwd in test_passwords:
    result = is_valid_password(pwd)
    status = "✓ Valid" if result else "✗ Invalid"
    print(f"  '{pwd}' -> {status}")

# --------------------------------------------------
# 4. Complex Manipulation: Reverse Words
# --------------------------------------------------
print("\n--- Task 4: Reverse Words ---")

def reverse_words(sentence):
    """
    Reverse the order of words in a sentence.
    Example: "Python is fun" -> "fun is Python"
    """
    # Split sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]  # Using slicing to reverse
    
    # Join words back into a sentence
    return " ".join(reversed_words)

# Test the function
test_sentences = [
    "Python is fun",
    "Hello World",
    "I love programming in Python",
    "Reverse this sentence please"
]

print("Word Reversal Tests:")
for sentence in test_sentences:
    reversed_sentence = reverse_words(sentence)
    print(f"  Original: '{sentence}'")
    print(f"  Reversed: '{reversed_sentence}'\n")


# ============================================================
# SET B: THE LOG FILE PARSER
# ============================================================

print("=" * 60)
print("SET B: THE LOG FILE PARSER")
print("=" * 60)

# --------------------------------------------------
# 1. Slicing & Methods: Extract log components
# --------------------------------------------------
print("\n--- Task 1: Log Line Parsing ---")

log_line = "ERROR 2024-10-06 14:35:01 Database connection failed"

# Method 1: Using slicing
log_level = log_line[:5]  # First 5 characters

# Method 2: Using split for more robust extraction
parts = log_line.split()
log_level = parts[0]  # First word is the log level

# Extract the message (everything after the timestamp)
# The message starts after "ERROR 2024-10-06 14:35:01 "
message_start_index = log_line.find("14:35:01") + len("14:35:01 ")
message = log_line[message_start_index:]

# Alternative: Join remaining parts after timestamp
message_alt = " ".join(parts[3:])  # Skip first 3 elements (level, date, time)

print(f"Log Line: {log_line}")
print(f"Log Level: {log_level}")
print(f"Message: {message}")

# --------------------------------------------------
# 2. Formatting: Create readable summary
# --------------------------------------------------
print("\n--- Task 2: Log Summary Formatting ---")

# Using .format() method
summary = "[{level}] -> {msg}".format(level=log_level, msg=message)
print(f"Formatted Summary: {summary}")

# Alternative format styles
summary_v2 = "[{}] -> {}".format(log_level, message)
print(f"Alternative Format: {summary_v2}")

# --------------------------------------------------
# 3. Validation & Search: Find Emails
# --------------------------------------------------
print("\n--- Task 3: Email Finder ---")

def find_all_emails(text):
    """
    Find all substrings that contain an '@' symbol.
    Returns a list of potential email addresses.
    """
    emails = []
    words = text.split()  # Split text into words
    
    for word in words:
        if "@" in word:
            # Clean up punctuation from the word
            cleaned = word.strip(".,;:!?()[]{}\"'")
            emails.append(cleaned)
    
    return emails

# Test the function
sample_text = """
Please contact us at support@company.com for assistance.
You can also reach john.doe@email.org or sales@business.net.
Invalid entries like @incomplete or missing@ should be handled.
Send your resume to careers@techfirm.io today!
"""

found_emails = find_all_emails(sample_text)
print("Sample Text:")
print(sample_text)
print("Found Email-like Strings:")
for email in found_emails:
    print(f"  • {email}")

# --------------------------------------------------
# 4. Complex Manipulation: Convert to Title Case
# --------------------------------------------------
print("\n--- Task 4: Underscore to Title Case ---")

def convert_to_title_case(underscore_string):
    """
    Convert underscore-separated string to title case with spaces.
    Example: "customer_account_id" -> "Customer Account Id"
    """
    # Split by underscore
    words = underscore_string.split("_")
    
    # Capitalize each word
    title_words = [word.capitalize() for word in words]
    
    # Join with spaces
    return " ".join(title_words)

# Test the function
test_strings = [
    "customer_account_id",
    "first_name",
    "user_email_address",
    "order_total_amount",
    "is_active"
]

print("Title Case Conversion Tests:")
for s in test_strings:
    converted = convert_to_title_case(s)
    print(f"  '{s}' -> '{converted}'")

# ============================================================
# SET C: THE USER INPUT SANITIZER
# ============================================================

print("=" * 60)
print("SET C: THE USER INPUT SANITIZER")
print("=" * 60)

# --------------------------------------------------
# 1. Slicing & Methods: Phone Number Formatting
# --------------------------------------------------
print("\n--- Task 1: Phone Number Sanitization ---")

# Sample input with inconsistent formatting
raw_phone = " 555-123-4567 "
print(f"Original input: '{raw_phone}'")

# Step 1: Remove all spaces and hyphens
cleaned_phone = raw_phone.strip().replace("-", "").replace(" ", "")