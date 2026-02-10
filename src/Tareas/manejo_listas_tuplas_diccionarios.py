"""
Assignment: Python Collections (Lists, Tuples, Dictionaries)
File: 2330245_MartinezVictor.py
"""

import math

# -------------------------------------------------------------------------
# Problem 1: Shopping list basics (list operations)
# Description: Processes a string of products and quantities into a list,
# allows adding new items, and searches for specific items.
# 
# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)
# 
# Outputs:
# - Items list (list)
# - Total items (int)
# - Found item (bool)
# 
# Validations:
# - Input string not empty.
# - Inputs are stripped and normalized to lowercase.
# 
# Test cases:
# 1) Normal: "apple:2,banana:5", "orange:6", "apple" -> Found: True
# 2) Edge case: "apple:1", "apple:2", "pear" -> Found: False (Duplicates allowed)
# 3) Error: "", "milk", "milk" -> "Error: invalid input"
# -------------------------------------------------------------------------

print("--- Problem 1: Shopping List ---")
initial_items_text = "apple:2, banana:5, orange:6"
new_item = "grapes:10"
search_item = "banana"

if not initial_items_text.strip():
    print("Error: invalid input")
else:
    # 1. Create list and normalize
    items_list = [item.strip().lower() for item in initial_items_text.split(",")]
    
    # 2. Add new item
    if new_item.strip():
        items_list.append(new_item.strip().lower())
    
    # 3. Total elements
    len_list = len(items_list)
    
    # 4. Search (Normalizing the search term to match the list)
    # We look for the product name within the "name:qty" string
    search_term = search_item.strip().lower()
    is_in_list = any(search_term in item for item in items_list)
    
    print(f"Items list: {items_list}")
    print(f"Total items: {len_list}")
    print(f"Found item '{search_term}': {is_in_list}")


# -------------------------------------------------------------------------
# Problem 2: Points and distances with tuples
# Description: Calculates the Euclidean distance and midpoint between two
# points in a 2D plane represented by tuples.
#
# Distance Formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
# Midpoint Formula: $M = (\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2})$
# 
# Inputs:
# - x1, y1, x2, y2 (float)
# 
# Outputs:
# - Point A, Point B (tuples)
# - Distance (float)
# - Midpoint (tuple)
# 
# Validations:
# - Numeric conversion check.
# 
# Test cases:
# 1) Normal: 0, 0, 3, 4 -> Distance: 5.0, Midpoint: (1.5, 2.0)
# 2) Edge case: 1.1, 1.1, 1.1, 1.1 -> Distance: 0.0, Midpoint: (1.1, 1.1)
# 3) Error: "a", 0, 0, 0 -> "Error: invalid input"
# -------------------------------------------------------------------------

print("\n--- Problem 2: Points and Distances ---")


try:
    x1, y1 = 0.0, 0.0
    x2, y2 = 3.0, 4.0
    
    point_a = (float(x1), float(y1))
    point_b = (float(x2), float(y2))
    
    distance = math.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)
    midpoint = ((point_a[0] + point_b[0]) / 2, (point_a[1] + point_b[1]) / 2)
    
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, 2)}")
    print(f"Midpoint: {midpoint}")
except ValueError:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 3: Product catalog with dictionary
# Description: Manages a catalog and calculates a purchase total based 
# on product existence and unit price.
# 
# Inputs:
# - product_name (string)
# - quantity (int)
# 
# Outputs:
# - Unit price, quantity, and total.
# 
# Validations:
# - Product must exist in dict.
# - Quantity must be > 0.
# 
# Test cases:
# 1) Normal: "apple", 5 -> Total: 50.0
# 2) Edge case: "ORANGE", 1 -> Total: 15.0 (Case insensitive)
# 3) Error: "pizza", 2 -> "Error: product not found"
# -------------------------------------------------------------------------

print("\n--- Problem 3: Product Catalog ---")
product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 15.0
}

buy_name = "  APPLE  ".strip().lower()
buy_qty = 5

if buy_name not in product_prices:
    print("Error: product not found")
elif buy_qty <= 0:
    print("Error: invalid quantity")
else:
    unit_price = product_prices[buy_name]
    total_price = unit_price * buy_qty
    print(f"Unit price: {unit_price}")
    print(f"Quantity: {buy_qty}")
    print(f"Total: {total_price}")


# -------------------------------------------------------------------------
# Problem 4: Student grades with dict and list
# Description: Calculates average grades for students and determines
# if they passed the course.
# 
# Inputs:
# - student_name (string)
# 
# Outputs:
# - Average (float), Passed (bool)
# 
# Validations:
# - Student must exist.
# - Grades list cannot be empty.
# 
# Test cases:
# 1) Normal: "Alice" -> Average: 87.5, Passed: True
# 2) Edge case: "Charlie" -> Average: 65.0, Passed: False
# 3) Error: "John" -> "Error: student not found"
# -------------------------------------------------------------------------

print("\n--- Problem 4: Student Grades ---")
PASSING_GRADE = 70.0
gradebook = {
    "Alice": [90.0, 85.0],
    "Bob": [100.0, 95.0, 92.0],
    "Charlie": [60.0, 70.0]
}

search_student = "Alice".strip()

if search_student not in gradebook:
    print("Error: student not found")
else:
    grades = gradebook[search_student]
    if not grades:
        print("Error: no grades recorded")
    else:
        average = sum(grades) / len(grades)
        is_passed = average >= PASSING_GRADE
        print(f"Grades: {grades}")
        print(f"Average: {round(average, 2)}")
        print(f"Passed: {is_passed}")


# -------------------------------------------------------------------------
# Problem 5: Word frequency counter
# Description: Cleans a sentence of punctuation, counts word frequencies,
# and identifies the most frequent word.
# 
# Inputs:
# - sentence (string)
# 
# Outputs:
# - Frequency dictionary, Most common word.
# 
# Validations:
# - Sentence must not be empty.
# 
# Test cases:
# 1) Normal: "Code is life, code is fun!" -> code: 2, is: 2...
# 2) Edge case: "Test. Test? Test!" -> test: 3
# 3) Error: "   " -> "Error: invalid input"
# -------------------------------------------------------------------------

print("\n--- Problem 5: Word Frequency ---")


sentence = "Python is great. Python is fast, and Python is fun!"

if not sentence.strip():
    print("Error: invalid input")
else:
    # Remove basic punctuation
    clean_text = sentence.lower()
    for char in ".,!?;:":
        clean_text = clean_text.replace(char, "")
    
    words_list = clean_text.split()
    freq_dict = {}
    
    for word in words_list:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    # Finding the most common word
    most_common = ""
    max_freq = 0
    for word, freq in freq_dict.items():
        if freq > max_freq:
            max_freq = freq
            most_common = word
            
    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common}")


# -------------------------------------------------------------------------
# Problem 6: Simple address book (CRUD)
# Description: Simulates an address book with Create, Read, and Delete operations.
# 
# Inputs:
# - action_text ("ADD", "SEARCH", "DELETE")
# - name, phone (strings)
# 
# Outputs:
# - Confirmation message or phone number.
# 
# Validations:
# - Valid action choice.
# - Fields not empty.
# 
# Test cases:
# 1) Normal: ADD "Carlos", "555-123" -> Contact saved
# 2) Edge case: SEARCH "carlos" -> Phone: 555-123 (Title normalized)
# 3) Error: DELETE "Unknown" -> "Error: contact not found"
# -------------------------------------------------------------------------

print("\n--- Problem 6: Address Book (CRUD) ---")
contacts = {
    "Alice": "111-222",
    "Bob": "333-444"
}

action = "SEARCH".strip().upper()
target_name = "  alice  ".strip().title()
new_phone = "555-999"

if action == "ADD":
    if not target_name or not new_phone:
        print("Error: invalid input")
    else:
        contacts[target_name] = new_phone
        print(f"Contact saved: {target_name} {new_phone}")

elif action == "SEARCH":
    phone = contacts.get(target_name)
    if phone:
        print(f"Phone: {phone}")
    else:
        print("Error: contact not found")

elif action == "DELETE":
    if target_name in contacts:
        contacts.pop(target_name)
        print(f"Contact deleted: {target_name}")
    else:
        print("Error: contact not found")
else:
    print("Error: invalid action")