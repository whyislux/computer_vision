"""
Assignment: Control Structures - Loops (for, while)
File: 2330245_MartinezVictor.py
"""

# -------------------------------------------------------------------------
# Problem 1: Sum of integers in a range
# Description: Calculates the total sum and the sum of even numbers 
# from 1 to n using a for loop with range().
# 
# Inputs:
# - n (int)
# 
# Outputs:
# - Sum 1..n (int)
# - Even sum 1..n (int)
# 
# Validations:
# - n must be an integer >= 1.
# 
# Test cases:
# 1) Normal: n = 10 -> Sum: 55, Even Sum: 30
# 2) Edge case: n = 1 -> Sum: 1, Even Sum: 0
# 3) Error: n = 0 -> "Error: invalid input"
# -------------------------------------------------------------------------

print("--- Problem 1: Range Sum ---")
try:
    user_input = input("Enter an integer n: ")
    n = int(user_input)
    
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0
        
        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i
        
        print(f"Sum 1..{n}: {total_sum}")
        print(f"Even sum 1..{n}: {even_sum}")
except ValueError:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 2: Multiplication table with for
# Description: Generates a multiplication table for a base number 
# up to a limit m.
# 
# Inputs:
# - base (int)
# - m (int)
# 
# Outputs:
# - Multiplication lines (e.g., "5 x 1 = 5")
# 
# Validations:
# - m must be >= 1.
# 
# Test cases:
# 1) Normal: base=5, m=4 -> 5x1=5 ... 5x4=20
# 2) Edge case: base=0, m=2 -> 0x1=0, 0x2=0
# 3) Error: base=5, m=-1 -> "Error: invalid input"
# -------------------------------------------------------------------------

print("\n--- Problem 2: Multiplication Table ---")
try:
    base = int(input("Enter base number: "))
    m = int(input("Enter table limit m: "))
    
    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            result = base * i
            print(f"{base} x {i} = {result}")
except ValueError:
    print("Error: invalid input")


# -------------------------------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# Description: Repeatedly reads positive numbers until a sentinel (-1) 
# is entered. Calculates count and average.
# 
# Inputs:
# - number (float)
# 
# Outputs:
# - Count (int)
# - Average (float)
# 
# Validations:
# - Numbers must be >= 0 (except sentinel).
# - Handles "no data" if sentinel is the first input.
# 
# Test cases:
# 1) Normal: 10, 20, 30, -1 -> Count: 3, Average: 20.0
# 2) Edge case: -1 -> "Error: no data"
# 3) Error: "abc" -> "Error: invalid input" (then continues)
# -------------------------------------------------------------------------

print("\n--- Problem 3: Sentinel Average ---")


SENTINEL_VALUE = -1
total_acc = 0.0
count = 0

while True:
    entry = input(f"Enter a number (or {SENTINEL_VALUE} to stop): ")
    try:
        val = float(entry)
        if val == SENTINEL_VALUE:
            break
        if val < 0:
            print("Error: only positive numbers accepted")
            continue
        
        total_acc += val
        count += 1
    except ValueError:
        print("Error: invalid input")

if count == 0:
    print("Error: no data")
else:
    average_value = total_acc / count
    print(f"Count: {count}")
    print(f"Average: {average_value}")


# -------------------------------------------------------------------------
# Problem 4: Password attempts with while
# Description: Checks user password against a constant. Limits attempts 
# to a maximum value.
# 
# Inputs:
# - user_password (string)
# 
# Outputs:
# - "Login success" or "Account locked"
# 
# Validations:
# - Max attempts count.
# 
# Test cases:
# 1) Normal: "admin123" on 1st try -> Success
# 2) Edge case: Fails twice, succeeds on 3rd -> Success
# 3) Error: 3 failed attempts -> "Account locked"
# -------------------------------------------------------------------------

print("\n--- Problem 4: Password Security ---")
CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0
success = False

while attempts < MAX_ATTEMPTS:
    user_password = input(f"Attempt {attempts + 1}/{MAX_ATTEMPTS} - Enter password: ")
    if user_password == CORRECT_PASSWORD:
        success = True
        break
    else:
        print("Incorrect password.")
        attempts += 1

if success:
    print("Result: Login success")
else:
    print("Result: Account locked")


# -------------------------------------------------------------------------
# Problem 5: Simple menu with while
# Description: Provides a persistent menu for greeting and counting.
# 
# Inputs:
# - option (int)
# 
# Outputs:
# - Menu responses based on choice.
# 
# Validations:
# - Option must be 0, 1, 2, or 3.
# 
# Test cases:
# 1) Normal: 1, 3, 2, 0 -> "Hello", "Incremented", "Counter: 1", "Bye"
# 2) Edge case: 5 -> "Error: invalid option"
# 3) Error: "x" -> "Error: invalid option"
# -------------------------------------------------------------------------

print("\n--- Problem 5: Interactive Menu ---")
menu_counter = 0
option = -1

while option != 0:
    print("\n--- MENU ---")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")
    
    choice = input("Select an option: ")
    
    try:
        option = int(choice)
        
        if option == 1:
            print("Result: Hello!")
        elif option == 2:
            print(f"Result: Counter: {menu_counter}")
        elif option == 3:
            menu_counter += 1
            print("Result: Counter incremented")
        elif option == 0:
            print("Result: Bye!")
        else:
            print("Error: invalid option")
    except ValueError:
        print("Error: invalid option")
        option = -1 


# -------------------------------------------------------------------------
# Problem 6: Pattern printing with nested loops
# Description: Prints a triangle of asterisks of size n, and an inverted one.
# 
# Inputs:
# - n (int)
# 
# Outputs:
# - Visual patterns of '*'
# 
# Validations:
# - n must be >= 1.
# 
# Test cases:
# 1) Normal: n = 3 -> Triangle and Inverted triangle of size 3.
# 2) Edge case: n = 1 -> Single '*' for both.
# 3) Error: n = -2 -> "Error: invalid input"
# -------------------------------------------------------------------------

print("\n--- Problem 6: Pattern Printer ---")


try:
    n_rows = int(input("Enter number of rows: "))
    
    if n_rows < 1:
        print("Error: invalid input")
    else:
        print("Normal Pattern:")
        for i in range(1, n_rows + 1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)
            
        print("\nInverted Pattern:")
        for i in range(n_rows, 0, -1):
            print("*" * i) 
            
except ValueError:
    print("Error: invalid input")