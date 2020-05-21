# Given two int arrays. Find out common numbers and different numbers.


def com(n1:list, n2:list):
    count = dict()
    n1.extend(n2)
    for i in n1:
        if i in count:
            count[i] +=1
        else:
            count[i] =1
    return count


print(com([1,2,3,7],[1,2,3,4,5,6,7]))