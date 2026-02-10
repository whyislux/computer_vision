"""
Course: Programming Fundamentals
Script: Numeric and Boolean Logic Exercises
File: 2330245_MartinezVictor.py
"""

# -------------------------------------------------------------------------
# Problem 1: Temperature converter and range flag
# Description: Converts Celsius to Fahrenheit and Kelvin, and flags high temps.
# Formulas: 
# $T_{F} = T_{C} \times \frac{9}{5} + 32$
# $T_{K} = T_{C} + 273.15$
#
# Inputs:
# - temp_c (float)
#
# Outputs:
# - Fahrenheit (float)
# - Kelvin (float)
# - High temperature (bool)
#
# Validations:
# - temp_c >= -273.15 (Absolute zero)
#
# Test cases:
# 1) Normal: 25.0 -> F: 77.0, K: 298.15, High: False
# 2) Edge case: 30.0 -> F: 86.0, K: 303.15, High: True
# 3) Error: -300.0 -> "Error: invalid input"
# -------------------------------------------------------------------------

print("--- Problem 1: Temperature Converter ---")
ABSOLUTE_ZERO_C = -273.15
HIGH_TEMP_THRESHOLD = 30.0

try:
    temp_c = float(input("Enter temperature in Celsius: "))
    
    if temp_c < ABSOLUTE_ZERO_C:
        print("Error: invalid input (below absolute zero)")
    else:
        temp_f = (temp_c * 9/5) + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= HIGH_TEMP_THRESHOLD
        
        print(f"Fahrenheit: {round(temp_f, 2)}")
        print(f"Kelvin: {round(temp_k, 2)}")
        print(f"High temperature: {is_high_temperature}")
except ValueError:
    print("Error: invalid input (must be a number)")


# -------------------------------------------------------------------------
# Problem 2: Work hours and overtime payment
# Description: Calculates weekly pay with a 150% bonus for hours over 40.
#
# Inputs:
# - hours_worked (int)
# - hourly_rate (float)
#
# Outputs:
# - Regular pay (float)
# - Overtime pay (float)
# - Total pay (float)
# - Has overtime (bool)
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
#
# Test cases:
# 1) Normal: 45 hours, $10 rate -> Regular: 400, Overtime: 75, Total: 475, Has OT: True
# 2) Edge case: 40 hours, $20 rate -> Regular: 800, Overtime: 0, Total: 800, Has OT: False
# 3) Error: -5 hours, $10 rate -> "Error: invalid input"
# -------------------------------------------------------------------------

print("\n--- Problem 2: Overtime Payment ---")
MAX_REGULAR_HOURS = 40
OVERTIME_MULTIPLIER = 1.5

try:
    hours_worked = int(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, MAX_REGULAR_HOURS)
        overtime_hours = max(0, hours_worked - MAX_REGULAR_HOURS)
        
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > MAX_REGULAR_HOURS
        
        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")
        print(f"Has overtime: {has_overtime}")
except ValueError:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 3: Discount eligibility with booleans
# Description: Checks eligibility for 10% discount based on status or purchase amount.
#
# Inputs:
# - purchase_total (float)
# - is_student_text (string: "YES"/"NO")
# - is_senior_text (string: "YES"/"NO")
#
# Outputs:
# - Discount eligible (bool)
# - Final total (float)
#
# Validations:
# - purchase_total >= 0
# - Text inputs must be "YES" or "NO"
#
# Test cases:
# 1) Normal: 500.0, NO, YES -> Eligible: True, Total: 450.0
# 2) Edge case: 1000.0, NO, NO -> Eligible: True, Total: 900.0
# 3) Error: 100.0, Maybe, NO -> "Error: invalid input"
# -------------------------------------------------------------------------

print("\n--- Problem 3: Discount Eligibility ---")
DISCOUNT_THRESHOLD = 1000.0
DISCOUNT_RATE = 0.10

try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Are you a student? (YES/NO): ").strip().upper()
    is_senior_text = input("Are you a senior? (YES/NO): ").strip().upper()
    
    valid_responses = ["YES", "NO"]
    
    if purchase_total < 0 or is_student_text not in valid_responses or is_senior_text not in valid_responses:
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"
        
        discount_eligible = is_student or is_senior or (purchase_total >= DISCOUNT_THRESHOLD)
        
        if discount_eligible:
            final_total = purchase_total * (1 - DISCOUNT_RATE)
        else:
            final_total = purchase_total
            
        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {round(final_total, 2)}")
except ValueError:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 4: Basic statistics of three integers
# Description: Calculates sum, average, max, min, and checks if all are even.
#
# Inputs:
# - n1, n2, n3 (int)
#
# Outputs:
# - Sum (int)
# - Average (float)
# - Max (int)
# - Min (int)
# - All even (bool)
#
# Validations:
# - Inputs must be valid integers.
#
# Test cases:
# 1) Normal: 2, 4, 6 -> Sum: 12, Avg: 4.0, All even: True
# 2) Edge case: -1, 0, 1 -> Sum: 0, Avg: 0.0, All even: False
# 3) Error: 2, "hello", 4 -> "Error: invalid input"
# -------------------------------------------------------------------------

print("\n--- Problem 4: Integer Statistics ---")

try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))
    
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    
    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")
except ValueError:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 5: Loan eligibility (income and debt ratio)
# Description: Evaluates loan approval based on income, debt ratio, and credit score.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - Debt ratio (float)
# - Eligible (bool)
#
# Validations:
# - monthly_income > 0
# - monthly_debt >= 0
# - credit_score >= 0
#
# Test cases:
# 1) Normal: 9000, 2000, 700 -> Ratio: 0.22, Eligible: True
# 2) Edge case: 8000, 3200, 650 -> Ratio: 0.4, Eligible: True
# 3) Error: 0, 1000, 700 -> "Error: invalid input"
# -------------------------------------------------------------------------

print("\n--- Problem 5: Loan Eligibility ---")
MIN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650

try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))
    
    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= MIN_INCOME and 
                    debt_ratio <= MAX_DEBT_RATIO and 
                    credit_score >= MIN_CREDIT_SCORE)
        
        print(f"Debt ratio: {round(debt_ratio, 2)}")
        print(f"Eligible: {eligible}")
except ValueError:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 6: Body Mass Index (BMI) and category flag
# Description: Calculates BMI and categorizes weight status.
# Formula: $BMI = \frac{weight}{height^{2}}$
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - BMI (float)
# - Underweight (bool)
# - Normal (bool)
# - Overweight (bool)
#
# Validations:
# - weight_kg > 0
# - height_m > 0
#
# Test cases:
# 1) Normal: 70kg, 1.75m -> BMI: 22.86, Normal: True
# 2) Edge case: 50kg, 1.70m -> BMI: 17.3, Underweight: True
# 3) Error: 70kg, 0m -> "Error: invalid input"
# -------------------------------------------------------------------------

print("\n--- Problem 6: BMI Calculator ---")

try:
    weight_kg = float(input("Enter weight in kg: "))
    height_m = float(input("Enter height in meters: "))
    
    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m ** 2)
        
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0
        
        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")
except ValueError:
    print("Error: invalid input")