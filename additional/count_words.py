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


def count():
    with open('test.txt', 'r') as text:
        res = text.read()
        c = dict()
        for word in res.split():
            if word in c:
                c[word] +=1
            else:
                c[word] = 1

        return c

# print(count())