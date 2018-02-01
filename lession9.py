#//////////////////////python构造函数//////////////
class FooBar:
    def __init__(self):    # 构造函数
        self.var1 = 42

    def getVar(self):
        return self.var1

f = FooBar()              # 类后面是有括号的
print(f.var1)
#//////////////////////调用未绑定的超类构造方法//////////////
class Bird:
    def __init__(self):
        print("bird constructor")

class SongBird(Bird):
    def __init__(self):
       # Bird.__init__(self)                     #可以直接调用父类的构造函数
        super(SongBird, self).__init__()         # 另外一种方式是使用super函数
        print("somebird constructor")
f = SongBird()

