# Write a Python program to count the occurrences of each word in a given sentence.


def calc(arr):
    count = dict()
    for word in arr.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


print(calc('the quick brown fox jumps over the lazy dog.'))