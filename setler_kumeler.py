import random
hayvanlar = {"tavuk", "tavşan", "koyun", "keçi", "inek", "tavuk"}

print(hayvanlar)

def rastgele(a, b):
    global tuple
    liste = []
    for i in range(a, b):
        liste.append(str(i))
    kume = set(liste)
    tuple = tuple(kume)

    return tuple[0]


print(rastgele(10,100))

rakamlar = {0, 5, 10, 15, 20}
rakamlar.add(1)
print(rakamlar)
rakamlar.update([2, 6, 8])
print(rakamlar)

rakamlar.remove(5)
print(rakamlar)


rakamlar.discard(20)
print(rakamlar)

rakamlar.clear()
print(rakamlar)

# birleşim-kesişim-fark

A = {1, 2, 3, 5, 7}
B = {2, 3, 4, 5, 6, 8, 9}
# Birleşim union
C = A.union(B)
print(C)
# Kesişim
E = A.intersection(B)
print(E)

F = B.intersection(A)
print(F)

M = A.difference(B)
print(M)

N = B.difference(A)
print(N)
