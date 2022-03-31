class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


P = Person("小明", 24)
print(P.age)
#给对象添加属性
P.sex = "male"
print(P.sex)
P1 = Person("小丽", 22)
#给对象添加属性只能用于单个对象，如下会报错
#print(P1.sex)


#给类添加属性
Person.sex = None
print(P1.sex)















