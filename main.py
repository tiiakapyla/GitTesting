# --- so the code works in terminal too ---
#!/usr/bin/python3

# --- function 'add', returns sum of the two numbers ---
def add(number1, number2):
    return number1 + number2
# --- function 'deduct', returns remainder of the two numbers ---
def deduct(number1, number2):
    return number1 - number2

# --- function 'deduction', returns remainder of the two numbers ---
def deduction(number1, number2):
    return number1 - number2

# --- user input numbers 1 and 2 ---
number1, number2 = int(input()), int(input())

# --- prints return, so it shows in terminal too
print(add(number1, number2))
print(deduct(number1, number2))
