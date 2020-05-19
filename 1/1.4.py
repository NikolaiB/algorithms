# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin- drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.) Hints: #106, #121, #134, #136


#Palindrom with String
def palindrome_s(s):
    s = s.replace(' ', '')
    rev = s[::-1].replace(' ', '')
    if s == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")

# palindrome_s("taco cat")


#Palindrom with list
def palindrome_l(s):
    if isinstance(s, str):
        s = s.replace(' ', '')
        orig = list(s)
        rev = list(reversed(s))
        if orig == rev:
            print("Palindrome")
        else:
            print("Not a palindrome")

# palindrome_l("taco cat")


# Doing Palindrome for a number
def palindrome_n(s):
    rev = int(str(s)[::-1])
    if s == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")

# palindrome_n(99699)
