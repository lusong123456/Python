# 列表的删除方法
a = [1, 2, 3, 4, 5, 1, 6, 2]
b = ["a", "b", "c", "d", "e", "a", "b"]

# pop   参数是index
# b.pop(1)

# remove  参数是对象的值，匹配到第一个值相等的要素进行删除
# 此处不符合预期，值删除了位置1的b
# b.remove(b[-1])

# del 删除索引范围内的对象
del(b[-1])

print(b)

a = 10
while True:
    b = a*a
    a = b