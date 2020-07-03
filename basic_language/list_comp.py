def findi(lst, val):
    ind = [i for i in range(len(lst)) if lst[i] == val]
    return ind

def findip(lst, pred):
    ind = [i for i in range(len(lst)) if pred(lst[i])]
    return ind

def pred1(x):
    return x < 5




lst1 = [i for i in range(10)]
print(lst1)

lst2 = [(i,2*i) for i in range(1,10)]
print(lst2)


lst = [1,2,3,3,2,4,5,6,6,6,1]
res1 = findi(lst, 2)
print(res1)

res2 = findip(lst, pred1)
print(res2)
