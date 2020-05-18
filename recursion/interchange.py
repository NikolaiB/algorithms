# Генерация всех перестоновок

def gen_simple(M, prefix=""):
    if M == 0:
        print(prefix)
    else:
        for i in "a", "b":
            gen_simple(M - 1, prefix + i)


gen_simple(3)

# N - число, в пределах которого делать перестановки,
# M - число, количество набора комбинаций в строке
def gen_number(N:int, M:int, prefix=None):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for dig in range(N):
        prefix.append(dig)
        gen_number(N, M-1, prefix)
        prefix.pop()

gen_number(4, 4)
