# python 3.6 字典是有序的

a = ["a", "b", "c"]
# b = ["A", "B", "C"]
# c = dict(zip(a, b))
# d = sorted(c.items(), key=lambda item: item[0], reverse=True)
# print(dict(d))



b = a
b[2] = 1
print(a)