"""
Assignment: String Manipulation Exercises
File: 2330245_MartinezVictor_t_strings.py
"""

# -------------------------------------------------------------------------
# Problem 1: Full name formatter (name + initials)
# Description: Normalizes a full name string, converts it to Title Case, 
# and extracts initials separated by dots.
# 
# Inputs:
# - full_name (string)
# 
# Outputs:
# - Formatted name (Title Case)
# - Initials (X.X.X.)
# 
# Validation:
# - Not empty after strip().
# - At least two words required.
# 
# Test cases:
# 1) Normal: "  juan carlos tovar  " -> "Juan Carlos Tovar", "J.C.T."
# 2) Edge case: "ALICE smith" -> "Alice Smith", "A.S."
# 3) Error: "Juan" -> "Error: at least two names required"
# -------------------------------------------------------------------------

print("--- Problem 1: Full Name Formatter ---")
full_name_input = "  juan carlos tovar  " 

clean_name = full_name_input.strip()

if not clean_name:
    print("Error: invalid input (empty)")
else:
    words = clean_name.split()
    if len(words) < 2:
        print("Error: invalid input (at least two names required)")
    else:
        formatted_name = clean_name.title()
        formatted_name = " ".join(words).title()
        
        initials_list = [word[0].upper() for word in words]
        initials = ".".join(initials_list) + "."
        
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")


# -------------------------------------------------------------------------
# Problem 2: Simple email validator (structure + domain)
# Description: Checks for a valid email structure (single @, period after @, 
# and no spaces). Extracts the domain if valid.
# 
# Inputs:
# - email_text (string)
# 
# Outputs:
# - Valid email: True/False
# - Domain: <string>
# 
# Validation:
# - Not empty after strip().
# - Exactly one '@'.
# - No spaces allowed.
# 
# Test cases:
# 1) Normal: "user@example.com" -> Valid: True, Domain: example.com
# 2) Edge case: "a@b.c" -> Valid: True, Domain: b.c
# 3) Error: "user @example.com" -> Valid: False (contains space)
# -------------------------------------------------------------------------

print("\n--- Problem 2: Email Validator ---")
email_text = "user@example.com" 

clean_email = email_text.strip()

if not clean_email:
    print("Error: invalid input")
else:
    has_one_at = clean_email.count("@") == 1
    has_no_spaces = " " not in clean_email
    
    is_valid = False
    domain = ""
    
    if has_one_at and has_no_spaces:
        at_index = clean_email.find("@")
        domain_part = clean_email[at_index + 1:]
        if "." in domain_part:
            is_valid = True
            domain = domain_part

    print(f"Valid email: {is_valid}")
    if is_valid:
        print(f"Domain: {domain}")


# -------------------------------------------------------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# Description: Determines if a phrase reads the same forwards and backwards,
# ignoring capitalization and whitespace.
# 
# Inputs:
# - phrase (string)
# 
# Outputs:
# - Is palindrome: True/False
# 
# Validation:
# - Not empty after strip().
# - Minimum 3 characters after removing spaces.
# 
# Test cases:
# 1) Normal: "Anita lava la tina" -> True
# 2) Edge case: "No" -> Error: too short
# 3) Error: "Hello world" -> False
# -------------------------------------------------------------------------

print("\n--- Problem 3: Palindrome Checker ---")
phrase = "Anita lava la tina"

clean_phrase = phrase.strip().lower().replace(" ", "")

if len(clean_phrase) < 3:
    print("Error: input too short to evaluate")
else:
    reversed_phrase = clean_phrase[::-1]
    is_palindrome = clean_phrase == reversed_phrase
    
    print(f"Normalized: {clean_phrase}")
    print(f"Is palindrome: {is_palindrome}")


# -------------------------------------------------------------------------
# Problem 4: Sentence word statistics
# Description: Analyzes a sentence to count words and identify the first, 
# last, shortest, and longest words.
# 
# Inputs:
# - sentence (string)
# 
# Outputs:
# - Word count, First, Last, Shortest, Longest words.
# 
# Validation:
# - Not empty.
# - At least one word.
# 
# Test cases:
# 1) Normal: "The quick brown fox" -> Count: 4, Shortest: The, Longest: quick
# 2) Edge case: "   SingleWord   " -> Count: 1, Shortest/Longest: SingleWord
# 3) Error: "    " -> Error: invalid input
# -------------------------------------------------------------------------

print("\n--- Problem 4: Word Statistics ---")
sentence = "The quick brown fox"

clean_sentence = sentence.strip()

if not clean_sentence:
    print("Error: invalid input")
else:
    word_list = clean_sentence.split()
    
    word_count = len(word_list)
    first_word = word_list[0]
    last_word = word_list[-1]
    
    # Logic to find min/max length words
    shortest_word = word_list[0]
    longest_word = word_list[0]
    
    for word in word_list:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word
            
    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# -------------------------------------------------------------------------
# Problem 5: Password strength classifier
# Description: Categorizes password strength into weak, medium, or strong 
# based on length and character diversity.
# 
# Rules:
# - Strong: length >= 8, has upper, lower, digit, and symbol.
# - Medium: length >= 8 and at least two types of characters.
# - Weak: length < 8 or only one type of character.
# 
# Inputs:
# - password_input (string)
# 
# Outputs:
# - Password strength: <category>
# 
# Validation:
# - Not empty.
# 
# Test cases:
# 1) Normal: "SafePass123!" -> strong
# 2) Edge case: "password" -> weak
# 3) Error: "" -> Error: invalid input
# -------------------------------------------------------------------------

print("\n--- Problem 5: Password Strength ---")
password_input = "SafePass123!" 

if not password_input:
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    
    for char in password_input:
        if char.isupper(): has_upper = True
        elif char.islower(): has_lower = True
        elif char.isdigit(): has_digit = True
        elif not char.isalnum(): has_symbol = True
            
    points = sum([has_upper, has_lower, has_digit, has_symbol])
    length = len(password_input)
    
    strength = "weak"
    if length >= 8:
        if points == 4:
            strength = "strong"
        elif points >= 2:
            strength = "medium"
            
    print(f"Password strength: {strength}")


# -------------------------------------------------------------------------
# Problem 6: Product label formatter (fixed-width text)
# Description: Formats product info into a 30-character string, 
# padding or trimming as necessary.
# 
# Inputs:
# - product_name (string)
# - price_value (float/string)
# 
# Outputs:
# - Label: "<30 character string>"
# 
# Validation:
# - Name not empty.
# - Price must be positive.
# 
# Test cases:
# 1) Normal: "Apple", 1.50 -> "Product: Apple | Price: $1.5" (padded)
# 2) Edge case: "Super Ultra Large Watermelon", 10.0 -> (trimmed to 30)
# 3) Error: "", -5 -> Error: invalid input
# -------------------------------------------------------------------------

print("\n--- Problem 6: Product Label ---")
product_name = "Apple"
price_value = 1.50
MAX_WIDTH = 30

if not product_name.strip() or price_value < 0:
    print("Error: invalid input")
else:
    base_label = f"Product: {product_name.strip()} | Price: ${price_value}"
    
    if len(base_label) > MAX_WIDTH:
        final_label = base_label[:MAX_WIDTH]
    else:
        # Use ljust to add spaces to the right
        final_label = base_label.ljust(MAX_WIDTH)
        
    print(f"Label: '{final_label}'")
    print(f"Length: {len(final_label)}")