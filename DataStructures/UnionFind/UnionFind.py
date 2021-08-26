UF = {}

def find(x):
    if x != UF[x]:
        UF[x] = find(UF[x])
    return UF[x]

def union(x, y):
    UF.setdefault(x, x)
    UF.setdefault(y, y)
    UF[find(x)] = find(y)

def numberOfSets():
    return len({find(x) for x in UF})

union(1,1)
print(UF)


union(1, 2)
print(UF)
union(3, 4)
print(UF)
union(1, 4)
print(UF)