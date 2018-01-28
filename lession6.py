
#////////////////////////////////魔法赋值////////////////////////////////////
x, y, z = 1, 2, 3
print(x, y, z)
#/////////////////////////////////交换多个值////////////////////////////////
x, y, z = y, z, x
print(x, y, z)
#/////////////////////////////////序列解包///////////////////////////////
# 将多个值的序列解开，放到变量的序列中
#  函数或方法返回元组（或其他序列或可迭代对象）时，这个特性尤为重要
source = {'name':'robin', 'gf':'marion'}
key, value = source.popitem();  #返回的key 和value都同时保存
print(key, value)
#/////////////////////////////////语句块///////////////////////////////
#空格就可以创建一个语句块
#冒号标识语句块开始
# 块中语句块是缩进的，当回退到和已闭合的块一样时，语句块就结束了

#/////////////////////////////////下面的作为布尔表达式的时候，会被当做 假///////////////////////////////
#False        None      0(包括浮点，长整和其他类型)         ""               ()          []            {}



#//////////////////////////////////相等运算符和同一运算符//////////////////////////////////////////
x = y = [1,2,3]
z = [1,2,3]
print(x == y)   #  相等性是判断对象的值是否相等
print(x == z)
print(x is z)   # 同一性是判断是否是同一个对象

#//////////////////////////////////成员资格运算符  IN //////////////////////////////////////////
print(1 in x)
#//////////////////////////////////布尔运算符也满足短路逻辑//////////////////////////////////////////

#//////////////////////////////////while//////////////////////////////////////////
x = 1
while x < 10:
    print(x)
    x+=1

# //////////////////////////////////for循环//////////////////////////////////////////
words = ['this','is','an']
for word in words:
    print(word)

# //////////////////////////////////range函数,range是分片，闭开区间//////////////////////////////////////////
for xx in range(10):
    print(xx)

print(range(5))

# //////////////////////////////////字典的迭代//////////////////////////////////////////
#方法一
mymap = {'x':1, 'y':2}
for key in mymap:
    print(key, "-",mymap.get(key))
#方法二
for key, value in mymap.items():
    print(key, "-", value)

# //////////////////////////////////一些迭代工具/////////////////////////////////////////
# 一：并行迭代range
names = ['anne','beth','george','damon']
ages = [12, 45, 32, 102]
for i in range(len(ages)):
    print(names[i], "-", ages[i])

# 二：并行迭代zip
for name, age in zip(names, ages):
    print(name, "-", age)

# //////////////////////////////////翻转和排序/////////////////////////////////////////
print('///////////1///////')
var = reversed('hello world')
print(list(var))

var = sorted((1,2,3,4))
print(var)

print('aaa'.join("bbb"))
# //////////////////////////////////列表推倒式/////////////////////////////////////////

var = [x*x for x in range(0,10) if x%3 == 0]
print(var)



