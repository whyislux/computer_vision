"""
Course: Computer Vision
Topic: Functions and Modular Logic
File: 2330245_MartinezVictor.py
"""

# -------------------------------------------------------------------------
# Problem 1: Rectangle area and perimeter (basic functions)
# Description: Defines two functions to calculate the area and perimeter 
# of a rectangle based on width and height.
# 
# Inputs:
# - width (float)
# - height (float)
# 
# Outputs:
# - Area (float)
# - Perimeter (float)
# 
# Validations:
# - Width and height must be greater than 0.
# 
# Test cases:
# 1) Normal: width=5.0, height=10.0 -> Area: 50.0, Perimeter: 30.0
# 2) Edge case: width=0.1, height=0.1 -> Area: 0.01, Perimeter: 0.4
# 3) Error: width=-5, height=10 -> "Error: invalid input"
# -------------------------------------------------------------------------

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

print("--- Problem 1: Rectangle Calculations ---")
w_in = 5.0
h_in = 10.0

if w_in > 0 and h_in > 0:
    print(f"Area: {calculate_area(w_in, h_in)}")
    print(f"Perimeter: {calculate_perimeter(w_in, h_in)}")
else:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 2: Grade classifier (function with return string)
# Description: Receives a numeric score and returns the corresponding 
# letter grade (A-F).
# 
# Inputs:
# - score (int/float)
# 
# Outputs:
# - Category (string)
# 
# Validations:
# - Score must be between 0 and 100.
# 
# Test cases:
# 1) Normal: score=85 -> Category: B
# 2) Edge case: score=90 -> Category: A
# 3) Error: score=105 -> "Error: invalid input"
# -------------------------------------------------------------------------



def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("\n--- Problem 2: Grade Classifier ---")
test_score = 85

if 0 <= test_score <= 100:
    grade_letter = classify_grade(test_score)
    print(f"Score: {test_score}")
    print(f"Category: {grade_letter}")
else:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 3: List statistics function (min, max, average)
# Description: Takes a list of numbers and returns a dictionary 
# with basic statistics.
# 
# Inputs:
# - numbers_text (string)
# 
# Outputs:
# - Min, Max, Average (float)
# 
# Validations:
# - String must not be empty.
# - Items must be valid numbers.
# 
# Test cases:
# 1) Normal: "10, 20, 30" -> Min: 10, Max: 30, Avg: 20.0
# 2) Edge case: "5.5" -> Min: 5.5, Max: 5.5, Avg: 5.5
# 3) Error: "10, hello, 30" -> "Error: invalid input"
# -------------------------------------------------------------------------

def summarize_numbers(numbers_list):
    stats = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return stats

print("\n--- Problem 3: List Statistics ---")
numbers_text = "10, 20, 30"
clean_text = numbers_text.strip()

if not clean_text:
    print("Error: invalid input")
else:
    try:
        float_list = [float(x.strip()) for x in clean_text.split(",")]
        results = summarize_numbers(float_list)
        print(f"Min: {results['min']}")
        print(f"Max: {results['max']}")
        print(f"Average: {round(results['average'], 2)}")
    except ValueError:
        print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 4: Apply discount list (pure function)
# Description: Applies a discount to a list of prices and returns 
# a new list without modifying the original.
# 
# Inputs:
# - prices_text (string)
# - discount_rate (float)
# 
# Outputs:
# - Original prices (list)
# - Discounted prices (list)
# 
# Validations:
# - Prices > 0, Discount rate between 0 and 1.
# 
# Test cases:
# 1) Normal: "100, 200", 0.10 -> Original: [100.0, 200.0], New: [90.0, 180.0]
# 2) Edge case: "50", 0.0 -> Original: [50.0], New: [50.0]
# 3) Error: "100", 1.5 -> "Error: invalid input"
# -------------------------------------------------------------------------



def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]

print("\n--- Problem 4: Discount Applier ---")
prices_text = "100, 200, 300"
rate = 0.10

try:
    p_list = [float(p.strip()) for p in prices_text.split(",") if p.strip()]
    
    if p_list and all(p > 0 for p in p_list) and (0 <= rate <= 1):
        new_prices = apply_discount(p_list, rate)
        print(f"Original prices: {p_list}")
        print(f"Discounted prices: {new_prices}")
    else:
        print("Error: invalid input")
except ValueError:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 5: Greeting function with default parameters
# Description: Generates a greeting message, optionally including a title.
# 
# Inputs:
# - name (string)
# - title (string, optional)
# 
# Outputs:
# - Greeting message (string)
# 
# Validations:
# - Name must not be empty.
# 
# Test cases:
# 1) Normal (Positional): "Alice", "Dr." -> "Hello, Dr. Alice!"
# 2) Edge case (Named): name="Bob" -> "Hello, Bob!"
# 3) Error: name="" -> "Error: invalid input"
# -------------------------------------------------------------------------

def greet(name, title=""):
    full_name = f"{title.strip()} {name.strip()}".strip()
    return f"Hello, {full_name}!"

print("\n--- Problem 5: Greet Function ---")
n = "Alice"
t = "Dr."

if n.strip():
    print(f"Greeting: {greet(n, t)}")
    print(f"Greeting: {greet(name='Charlie')}")
else:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 6: Factorial function (iterative)
# Description: Calculates the factorial of n using an iterative approach.
# Choice: Iterative (for loop) chosen to avoid recursion depth limits.
# 
# Inputs:
# - n (int)
# 
# Outputs:
# - Factorial value (int)
# 
# Validations:
# - n must be an integer between 0 and 20.
# 
# Test cases:
# 1) Normal: n=5 -> Factorial: 120
# 2) Edge case: n=0 -> Factorial: 1
# 3) Error: n=-5 -> "Error: invalid input"
# -------------------------------------------------------------------------



def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\n--- Problem 6: Factorial ---")
MAX_FACTORIAL = 20

try:
    n_val = 5
    if 0 <= n_val <= MAX_FACTORIAL:
        fact = calculate_factorial(n_val)
        print(f"n: {n_val}")
        print(f"Factorial: {fact}")
    else:
        print("Error: invalid input")
except (ValueError, TypeError):
    print("Error: invalid input")