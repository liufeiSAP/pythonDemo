str = "let's go"
print(str)

################################字符串含有单/双引号##############################

#str = 'let's go' , 单引号和双引号是一样的，但是已经包含单引号的，外层一定要用双引号

str = 'let\'s go'  # 用转义字符也行

str = "\"hellow world\" she said"  # 如果是包含双引号，也用转义字符
print(str)
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

lenStr3 = """我也是
一个
长字符串"""
print(lenStr3)

###############################原始字符串（对反斜线不会特殊对待）#################################################
#以r开头的的字符串，对反斜线不会特殊对待
path = 'c:\nowhere'   #路径是c:\nowhere
print(path)
#结果是 c:
# owhere

#一种解决方案：
path = 'c:\\nowhere'
print(path)

#另外解决方案，用r原样输出
path = r'c:\nowhere'
print(path)
#################################Unicode字符串#################################
#python普通字符串是以8位ASCII码形式存储的，而Unicode是以16位unicode字符存储。
#用前缀U表示Unicode字符串： 

print(u"hello world")
################################################################################

input("ennd")