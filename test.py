def chenFaBiao():
    # 乘法口诀表
    for i in range(1, 10):
        for j in range(1, i+1):
            print(str(j)+"x"+str(i)+"="+str(i*j), end=" ")
        print()
def shuiXianHua():
    # 水仙花数，一个三位数，各个位的立方和等与这个三位数
    for i in range(100, 1000):
        numList = [n for n in str(i)]
        if int(numList[0]) ** 3 +int(numList[1]) ** 3 +int(numList[2]) ** 3 == i:
            print(i)

def fenJie(x):
    flag = True
    print(str(x), end="=")
    while flag:
        for i in range(2, x+1):
            if x % i == 0:
                x = x//i
                if x == 1:
                    print(i, end="")
                    flag = False
                else:
                    print(i, end="*")
                break
fenJie(999**999)