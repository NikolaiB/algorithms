# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# Hints: #7, #84, #722, #737


def perm(str1, str2):
    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')
    if len(str1) != len(str2):
        return 'It is not a Permutation'
    for i in str1:
        if i in str2:
            str2 = str2.replace(i, '', 1)
    if str2 == '':
        return 'It is a Permutation'
    else:
        return 'It is not a Permutation'


print(perm('dreiving', 'drrrring'))
