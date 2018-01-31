#//////////////////////////////斐波那契数列////////////////////////////////
fabs = [0, 1]
for i in range(10):
    fabs.append(fabs[-2] + fabs[-1])
print(fabs)
#//////////////////////////////定义函数////////////////////////////////
def fibs(num):
    fabs = [0, 1]
    for i in range(10):
        fabs.append(fabs[-2] + fabs[-1])
    return fabs

print(fibs(10))
#//////////////////////////////引入其他模块的函数///////////////////////////////
import  module1                           # 直接导入模块的所有函数
from module1 import fun                   # 只导入需要的函数
from module1 import fibs as fibsNew       # 可以给重名的函数起别名

print(module1.fibs(18))                    # 如果有重名的函数，就用模块名限定
print(fun(4))
print(fibsNew(45))
#//////////当字符串，数字，元组等不可变类型作参数的时候，是不会改变的///////////////////////////
print("///////////////////////////////////////")
def changeStr(n):
    n = "new String"
    return n

def changeInt(n):
    n = 9
    return n

def changeY(n):
    n = (1,2,3,4,5,6)
    return n

str = "old string"
changeStr(str)
print(str)

intV = 1
changeInt(intV)
print(intV)

aa = (1,2,3)
changeY(aa)
print(aa)
#////当列表在函数内放生变化的时候，是影响调用实参的。当两个变量引用一个列表的时候，他们确实引用同一个列表///

#/////////////////////////////如何防止列表在函数内改动影响外部的列表？/////////////////////////////
print("///////////////////////////////////////")
names = [1, 2, 3]
names1 = names               # 指向相同的列表
names2 = names[:]            #  列表复制

print(names1 == names)        # True
print(names1 is names)        # True
print(names2 == names)        # True
print(names2 is names)        # False

#////////////////////函数参数的默认值/////////////////////////////
def hello_2(greeting = "Hello ", name = " world"):
    print("%s %s"  %  (greeting,name))

hello_2()          # 有默认值的话，可以省略参数

#////////////////////可变参数//////////////////////////////////////////
def print_pa(*pa):
    print(pa)

print_pa(1, 2, 3, [4,5], {6,7}, {"1": "a", "2": "b"})

#////////////////////全局变量//////////////////////////////////////////
x = 100
def change_g():
    global x         # 全局变量
    global y
    y = y + 1

y = 10
change_g()
print(y, x)









