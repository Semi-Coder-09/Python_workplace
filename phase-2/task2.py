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