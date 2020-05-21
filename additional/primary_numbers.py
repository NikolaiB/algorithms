# Find Prime numbers

def prime():
    r = []
    for i in range(1, 100):
        l = []
        for j in range(1, 100):
            if i % j == 0:
                l.append(i)
        # print(l)
        if len(l)<=2:
           r.extend(l)
    return set(r)
# print(prime())

# Find Prime number
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")