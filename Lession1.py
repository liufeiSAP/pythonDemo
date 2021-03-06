

################################字符串含有单/双引号##############################
#str = 'let's go' , 单引号和双引号是一样的，但是已经包含单引号的，外层一定要用双引号
import sys

str = "let's go"
print("1" + str)
str = "let\'s go"
print("2" + str)
str = 'let\'s go'  # 用转义字符也行, 这里必须用转义
print("3" + str)
str = 'A\" fsdf '
print("4" + str)
str = 'A" fsdf '
print("5" + str)
str = "\"hellow world\" she said"  # 如果是包含双引号，也用转义字符
print(str)

# 综上，单引号包含双引号，转义是否都可以；
#        双引号包含单引号，转义是否都可以
#        单引号包含双引号，双引号包含单引号都必须转义；
##############################拼接字符串##################################################
x = "hello1"
y = "world2"
print(x+y)
################################长字符串################################################
lenStr = '''
我是长
字符串'''
print(lenStr)

lenStr2 = '我是长\n字符串2'
print(lenStr2)

lenStr2 = "我是长\n字符串3"
print(lenStr2)

lenStr3 = """我也是
一个
长字符串"""
print(lenStr3)

# 多行的长字符串的定义方式：  三个单引号； 三个双引号； \n；
###############################原始字符串（对反斜线不会特殊对待）#################################################
#以r开头的的字符串，对反斜线不会特殊对待
path = 'c:\nowhere'   #路径是c:\nowhere
print(path)
#结果是 c:
# owhere

#一种解决方案：但是如果里面有很多反斜杠的话，处理起来很麻烦，需要找到每一个反斜杠，都转义
path = 'c:\\nowhere'
print(path)

#另外解决方案，用r原样输出，这样可以把所有的反斜杠都转义
path = r'c:\nowhere'
print(path)

#   反斜杠\是转义字符，如果想不被当成转义字符处理，可一两种解决方案： 用两个反斜杠 \\;    用r开头定义字符串
#################################Unicode字符串#################################
#python普通字符串是以8位ASCII码形式存储的，而Unicode是以16位unicode字符存储。
#用前缀U表示Unicode字符串：
print(u"hello world")

var = 'c'
var2 = u"c"
print(len(var))
print(len(var2))

print(sys.getsizeof(var))
print(sys.getsizeof(var2))
################################################################################
# 这里的斜杠表示： 虽然写法上换行了，但实际不换行，不仅仅是字符串，其他类型也好使
str = "hello \
world"
print(str)
print(str[1:3])   # 截取其中一段，注意是闭开区间