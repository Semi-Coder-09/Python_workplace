# Array
# 0(n) Time Complexcity - loop runs n times where n is the number of elements in the array

arr = [4, 2, 9, 1]

max_num = arr[0]

for num in arr:
    if num > max_num:
        max_num = num

print(max_num)

# Strings

s = "python"

print(s[::-1])

# manual reverse

rev = ""

for ch in s:
    rev = ch + rev

print(rev)

# Hash Map (Dictionary)

s = "banana"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# two pointers

arr = [1,2,3,4]

left = 0
right = len(arr)-1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(arr)

# sliding window
# Initial Setup
arr = [1, 2, 3, 4, 5]  # Memory stores an array of 5 elements: indices 0 to 4
k = 3                  # Window size is set to 3

# --- INITIAL WINDOW CALCULATION ---
window = sum(arr[:k])  # Evaluates sum([1, 2, 3]). Backend sets: window = 6
max_sum = window       # Backend sets: max_sum = 6

# --- THE LOOP ---
# len(arr) is 5, so range(3, 5) will loop twice: when i = 3 and i = 4.
for i in range(k, len(arr)):

    # =========================================================================
    # CASE 1: i = 3 (First Iteration of the loop)
    # =========================================================================
    window += arr[i] - arr[i - k]
    # Backend translation: window += arr[3] - arr[0]
    # Lookup:              window += 4 - 1  (which is +3)
    # New state:           window becomes 9 (6 + 3) -> representing [2, 3, 4]

    max_sum = max(max_sum, window)
    # Backend translation: max(6, 9)
    # New state:           max_sum updates to 9

    # =========================================================================
    # CASE 2: i = 4 (Second Iteration of the loop)
    # =========================================================================
    window += arr[i] - arr[i - k]
    # Backend translation: window += arr[4] - arr[1]
    # Lookup:              window += 5 - 2  (which is +3)
    # New state:           window becomes 12 (9 + 3) -> representing [3, 4, 5]

    max_sum = max(max_sum, window)
    # Backend translation: max(9, 12)
    # New state:           max_sum updates to 12

# Loop ends here because range(3, 5) is exhausted.

# =============================================================================
# CASE 3 & 4: (Conceptually, if the array kept going)
# Let's pretend arr had more elements: [1, 2, 3, 4, 5, 6, 7]
# =============================================================================

# CASE 3 (If i = 5):
# window += arr[5] - arr[2]  -> window += 6 - 3  -> window becomes 15 [4, 5, 6]
# max_sum = max(12, 15)      -> max_sum becomes 15

# CASE 4 (If i = 6):
# window += arr[6] - arr[3]  -> window += 7 - 4  -> window becomes 18 [5, 6, 7]
# max_sum = max(15, 18)      -> max_sum becomes 18


# --- FINAL OUTPUT ---
print(max_sum)  # Backend retrieves max_sum from memory (which is 12) and prints it

# Recursion

def fact(n):
    if n == 1:
        return 1

    return n * fact(n-1)

print(fact(5))

# =========================================================================
# CASE 1: fact(5) is called
# =========================================================================
# n = 5
# Is 5 == 1? No.
# Backend waits to calculate: 5 * fact(4)  <-- Paused! Needs fact(4) first.

# Stack using list [ Last  in, First out ]

stack = []

stack.append(1)
stack.append(2)

print(stack.pop())
print(stack)

# Queue [ First in, First out ]

from collections import deque

q = deque()

q.append(1)
q.append(2)

# print(q.popleft())
print(q.pop())
print(q)