# Reverse string

def reverse_string(s):
    rev = ""            # Backend initializes an empty string variable 'rev' to store the reversed string

    for ch in s:        # Backend starts a loop that iterates over each character 'ch' in the input string 's'
        rev = ch + rev  # For each character, the backend updates 'rev' by concatenating the current character 'ch' to the front of 'rev'. 
                        # This effectively builds the reversed string as it iterates through 's'.

    return rev          # After the loop completes, the backend returns the fully reversed string stored in 'rev' to the caller.

print(reverse_string("good man"))  # Backend calls the function 'reverse_string' with the argument "hello".
                                # The function processes the string and returns "olleh", which is then printed to the


# | Step | Character (``ch``) | New ``rev`` value |
# | --- | --- | --- |
# | 1 | ``g`` | ``"g"`` |
# | 2 | ``o`` | ``"og"`` |
# | 3 | ``o`` | ``"oog"`` |
# | 4 | ``d`` | ``"doog"`` |
# | 5 | (space ``" ``"``) | ``" ``doog"`` |
# | 6 | ``m`` | ``"m ``doog"`` |
# | 7 | ``a`` | ``"am ``doog"`` |
# | 8 | ``n`` | ``"nam ``doog"`` |

a = "hello world"

for ch in a:
    print(ch)


# Palindrome

# word palindrome: madam, racecar, level
def is_palindrome(s):
    rev = ""

    for ch in s:
        rev = ch + rev

    return rev == s 

print(is_palindrome("madam"))  # Backend calls the function 'is_palindrome' with the argument "madam".

# number palindrome: 12321, 1221, 1

def find_palindrome(num):
    s = str(num)  # Backend converts the input number 'num' to a string and stores it in variable 's'
    rev = ""      # Backend initializes an empty string variable 'rev' to store the reversed string representation of the number

    for ch in s:  # Backend starts a loop that iterates over each character 'ch' in the string 's'
        rev = ch + rev  # For each character, the backend updates 'rev' by concatenating the current character 'ch' to the front of 'rev'. 
                        # This effectively builds the reversed string as it iterates through 's'.

    return rev == s  # After the loop completes, the backend compares the reversed string 'rev' with the original string 's'. 
                     # It returns True if they are equal (indicating that the number is a palindrome) and False otherwise.

print(find_palindrome(12321))  # Backend calls the function 'find_palindrome' with the argument 12321.
print(find_palindrome(1221))   # Backend calls the function 'find_palindrome' with the argument 1221.
print(find_palindrome(1))      # Backend calls the function 'find_palindrome' with the argument 1.

# make palindrome in number range (1000, 9999) 
for num in range(1000, 10000):
    if find_palindrome(num):
        print(num,end=" ")
print(" ")

# Two Sum

def two_sum(a, b):

    if a and b == int:
        return a + b
    print("total is: ", a + b)

# a = int(input("Enter the number: "))
# b = int(input("Enter another number: "))

# two_sum(a,b)

# Max number

def max_num(arr):
    max_num = arr[0]  

    for num in arr:  
        if num > max_num:  
            max_num = num  

    return max_num  

arr = [3, 1, 4, 1, 5, 9]
print(max_num(arr))  

# Frequency counter

def frequency_counter(arr):
    freq = {}  

    for num in arr:  
        freq[num] = freq.get(num, 0) + 1 

    return freq 

arr = [1, 2, 2, 3, 3, 3]
print(frequency_counter(arr))

# reverse series of numbers

for i in range(15, 10, -1):
    print(i, end=" ")
print(" ")

