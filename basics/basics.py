# =========================================================
# PYTHON FUNDAMENTALS - COMPLETE PRACTICE FILE
# Covers:
# Variables, Data Types, Input, Conditions, Loops,
# Functions, Lists, Tuples, Sets, Dictionaries,
# Strings, Exception Handling, List Comprehension
# =========================================================


# =========================================================
# 1. VARIABLES & DATA TYPES
# =========================================================

name = "Bhabani"
age = 23
height = 5.9
is_working = True

print("===== VARIABLES =====")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Working:", is_working)


# =========================================================
# 2. USER INPUT
# =========================================================

print("\n===== USER INPUT =====")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Welcome", user_name)
print("Next year age:", user_age + 1)


# =========================================================
# 3. CONDITIONS (if, elif, else)
# =========================================================

print("\n===== CONDITIONS =====")

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# =========================================================
# 4. LOOPS
# =========================================================

print("\n===== FOR LOOP =====")

for i in range(1, 6):
    print(i)

print("\n===== WHILE LOOP =====")

count = 1

while count <= 5:
    print(count)
    count += 1


# =========================================================
# 5. FUNCTIONS
# =========================================================

print("\n===== FUNCTIONS =====")

def add(a, b):
    return a + b

result = add(10, 20)

print("Addition:", result)


# Function with user input

def greet(name):
    print("Hello", name)

greet(user_name)


# =========================================================
# 6. LISTS
# =========================================================

print("\n===== LISTS =====")

numbers = [1, 2, 3, 4, 5]

print("Original List:", numbers)

numbers.append(6)
print("After Append:", numbers)

numbers.remove(3)
print("After Remove:", numbers)

print("First Element:", numbers[0])

for num in numbers:
    print(num)


# =========================================================
# 7. TUPLES
# =========================================================

print("\n===== TUPLES =====")

colors = ("red", "green", "blue")

print(colors)
print(colors[1])


# =========================================================
# 8. SETS
# =========================================================

print("\n===== SETS =====")

data = {1, 2, 3, 3, 4}

print(data)

data.add(5)

print(data)


# =========================================================
# 9. DICTIONARIES
# =========================================================

print("\n===== DICTIONARIES =====")

student = {
    "name": "Bhabani",
    "age": 23,
    "course": "CSE"
}

print(student)

print(student["name"])

student["age"] = 24

print(student)


# Loop through dictionary

for key, value in student.items():
    print(key, ":", value)


# =========================================================
# 10. STRINGS
# =========================================================

print("\n===== STRINGS =====")

text = "Python"

print(text.upper())
print(text.lower())
print(text[::-1])   # reverse string

print("Length:", len(text))

for ch in text:
    print(ch)


# =========================================================
# 11. STRING LOGIC EXAMPLES
# =========================================================

print("\n===== PALINDROME CHECK =====")

word = input("Enter word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# =========================================================
# 12. LIST LOGIC EXAMPLES
# =========================================================

print("\n===== FIND MAX NUMBER =====")

nums = [4, 7, 1, 9, 2]

max_num = nums[0]

for n in nums:
    if n > max_num:
        max_num = n

print("Max Number:", max_num)


# =========================================================
# 13. COUNT FREQUENCY USING DICTIONARY
# =========================================================

print("\n===== FREQUENCY COUNTER =====")

text = "banana"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


# =========================================================
# 14. EXCEPTION HANDLING
# =========================================================

print("\n===== EXCEPTION HANDLING =====")

try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter another number: "))

    print("Division:", num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Program Finished")


# =========================================================
# 15. LIST COMPREHENSION
# =========================================================

print("\n===== LIST COMPREHENSION =====")

squares = [x*x for x in range(1, 6)]

print(squares)


# =========================================================
# 16. MINI PROJECT - SIMPLE CALCULATOR
# =========================================================

print("\n===== SIMPLE CALCULATOR =====")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operation = input("Choose (+, -, *, /): ")

if operation == "+":
    print("Result:", a + b)

elif operation == "-":
    print("Result:", a - b)

elif operation == "*":
    print("Result:", a * b)

elif operation == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid Operation")


# =========================================================
# 17. PRIME NUMBER CHECK
# =========================================================

print("\n===== PRIME NUMBER CHECK =====")

num = int(input("Enter a number: "))

is_prime = True

if num <= 1:
    is_prime = False

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime")


# =========================================================
# 18. FACTORIAL
# =========================================================

print("\n===== FACTORIAL =====")

num = int(input("Enter number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)


# =========================================================
# 19. FIBONACCI SERIES
# =========================================================

print("\n===== FIBONACCI SERIES =====")

n = int(input("Enter range: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    temp = a
    a = b
    b = temp + b


# =========================================================
# 20. END
# =========================================================

print("\n\n===== PHASE 1 COMPLETED =====")
print("You covered Python fundamentals successfully!")