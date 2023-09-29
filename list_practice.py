li = [1, 2, 3, 4, 4, 4, 4, 4, 5]
p = li.index(4)
print(p)
p_1 = len(li) - li[::-1].index(4) - 1
print(li[::-1])
print(len(li))
print(p_1)
