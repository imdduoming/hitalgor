a =[[1,2,3],[4,5,6]]
a = list(zip(*a[::-1]))
a = [list(s) for s in a]

print(a)