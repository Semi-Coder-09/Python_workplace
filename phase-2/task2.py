# Longest substring without repeating
def longest_substring(s):
    longest = 0
    for i in range(len(s)):
        current = ""
        for j in range(i, len(s)):
            if s[j] in current:   # if character already in substring, stop
                break
            current += s[j]       # add character to substring
            longest = max(longest, len(current))
    return longest

print(longest_substring("abcabcbb"))  # Backend calls the function 'longest_substring' with the argument "abcabcbb".
print(longest_substring("bbbbb"))     
print(longest_substring("pwwkewuhuvunkjlknjyugiuv"))     

# Maximum subarray

def max_subarray(nums):
    # Start with the first element
    max_sum = nums[0]
    current_sum = nums[0]

    # Loop through the rest of the array
    for num in nums[1:]:
        # Either add the current number to the running sum
        # or start fresh from the current number
        current_sum = max(num, current_sum + num)
        # Update the maximum sum found so far
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6


# Container with most water

def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate area between left and right
        width = right - left
        area = min(height[left], height[right]) * width
        max_area = max(max_area, area)

        # Move the pointer with the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage
print(max_area([1,8,6,2,5,4,8,3,7]))  # Output: 49


