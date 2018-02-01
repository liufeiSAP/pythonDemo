#///////////////抽象////////////////////////////////////////////////////////

#///////////////////////////不管是字符串还是列表，count()函数都可以工作
var = (1, 2, 3).count(1)
print(var)
var = [1, 2, 3].count(1)
print(var)
var = "123".count('1')
print(var)
#///////////////////////////self: 类自动将自己作为第一个参数传递进去，代表对象本身

#///////////////////////////自定义类, 创建实例///////////////////////
class Person:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print('Hello world  I am %s' % self.name)

foo = Person()
foo.setName('Jet')
foo.greet()
#///////////////////////////////////////////////////////////////////////
'''
为了让方法或者变量变为私有（从外部无法访问），只要在它的名字前面加上双下划线即可幕后是这么做的：
以双下划线开始的名字都被翻译成前面加上单下划线和类名的形式，所以还是可以在类的外部调用这些私有方法和变量（这样做不好）。
如果不需要使用这种方法但是又想让其他对象不要访问内部数据，那么可以使用单下划线。这只是个习惯，但有实际效果。
例如，前面有下划线的名字都不会被带星号的import语句（from module import *）导入。
'''
#/////////////////////////////////////给类指定超类//////////////////////////////////
class Student(Person):
    def setAge(self, age):
        age = age

foo = Student()
foo.setName("fds")      # 从父类继承
foo.setAge(5)
#/////////////////////////////////////检查一个类是另一个类的超类//////////////////////////////////
print(issubclass(Student, Person))#检查一个类是另一个类的超类
print(Student.__bases__)   # 类的基类
print(isinstance(foo, Student)) # 是否是类的实例
#////////////////////////////////////python允许多继承//////////////////////////////////
'''
多重继承的两个类如果有方法同名，那么先继承的类的方法会覆盖后继承的类的方法。
'''