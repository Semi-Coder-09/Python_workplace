import numpy as np

# Matrix Calculator

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Addition
print("A + B =")
print(A + B)

# Subtraction
print("A - B =")
print(A - B)

# Multiplication (matrix product)
print("A x B =")
print(np.dot(A, B))

# Element-wise multiplication
print("A * B =")
print(A * B)


# Marks Analyzer

def mark_analyzer(marks):
    # Basic statistics
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Grade assignment (simple logic)
    grades = []
    for m in marks:
        if m >= 90:
            grades.append("A")
        elif m >= 75:
            grades.append("B")
        elif m >= 50:
            grades.append("C")
        else:
            grades.append("F")

    # Print results
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Grades:", grades)


# Example usage
marks = [95, 82, 67, 45, 88]
mark_analyzer(marks)


# Temperature Converter

def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = int(input("Choose an option (1-4): "))
    temp = float(input("Enter temperature value: "))

    if choice == 1:
        result = (temp * 9/5) + 32
        print(f"{temp}°C = {result}°F")
    elif choice == 2:
        result = (temp - 32) * 5/9
        print(f"{temp}°F = {result}°C")
    elif choice == 3:
        result = temp + 273.15
        print(f"{temp}°C = {result}K")
    elif choice == 4:
        result = temp - 273.15
        print(f"{temp}K = {result}°C")
    else:
        print("Invalid choice!")

# Example run
temperature_converter()
