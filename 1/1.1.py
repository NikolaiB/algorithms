#Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def unique(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return f'The String, {s}, doesn\'t have unique characters'
    else:
        return f'The String, {s}, has all unique characters'


print(unique('test1233'))