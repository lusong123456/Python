import types
import os
os.walk()

class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")


# 定义一个实例方法
def run(self, speed):
    print("%s在移动，速度是%d km/h" % (self.name, speed))


# 定义一个类方法
@classmethod
def testClass(cls):
    cls.num = 100


# 定义一个静态方法
@staticmethod
def testStatic():
    print("static method")
    return "s"


# 创建一个实例对象
P = Person("老王", 24)
# 调用在class中的方法
P.eat()

# 给这个对象添加实例方法
P.run = types.MethodType(run, P)
# 调用实例方法
P.run(180)

# 给Person类绑定类方法
Person.testClass = testClass
# 调用类方法
# print(Person.num)
Person.testClass()
print(Person.num)

# 给Person类绑定静态方法
Person.testStatic = testStatic
Person.testStatic()
# 打印类的方法和属性
print("\n".join(["%s:%s" % item for item in Person.__dict__.items()]))






















