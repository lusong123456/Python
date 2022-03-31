class A:
    def __init__(self, name):
        self.name = name
        print(name)


class B(A):
    sex = "man"

    def __init__(self, name, age):
        super(B, self).__init__(name)
        self.age = age

    def printName(self):
        print(self.age)

    print(sex)


print("b")
b = B("songLu", "26")
b.printName()

