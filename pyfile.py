#文件
'''
问题：
 1、什么是文件？
 2、文件有什么作用？
 答：能够实现程序与文件之间的数据交互。
 3、如何创建、使用文件？
 答：open(外部文件名，处理模式)=>返回一个文件对象

文件的创建： open(外部文件名，处理模式)=>返回一个文件对象
方法：
    read() 全部读出  返回的是字符串

文件读写：
1、字符串很容易实现读写
2、当要保存复杂数据类型时（嵌套列表和字典），手动解析和系列化就会变得复杂。 用Json实现数据交互


'''
#=========================================================文件=========================================
#文件
'''
with open('pi_digits.txt') as pd:
    content = pd.read()        #会读出文件全部内容
print('-----------')
print(content)
print('-----------')
#删除末尾空行
#print(content.rstrip())
'''
'''
#逐行读取,使用for循环;;  .strip()消除空白行
with open('pi_digits.txt') as pd:  #with获取的文件对象只在当前with块中
    for str in pd:
        print(str.strip())
        print('===')
'''
'''
import os
print(os.getcwd())   获取当前工作路径
with open('/media/joey/hdd1/pyproject/pyproject/testfile.txt', 'w') as f:
    f.write("first write")
    f.close()
'''

#================2023110
f = open('filelearn.txt', 'w')  #默认在当前工作目录创建文件
#在文件中写入内容
f.write('hello text file')  #以‘r’模式打开时，无法写入
f.write('goodbye text file\n')  #输入中 \n 在txt中会自动换行
f.write('goodbye again text file')
f.close()

f1 = open('filelearn.txt')
#print(f1.read())   # read() 全部读出  返回的是字符串
#print(f1.readline()) #readline() 一次读一行
#print(f1.readline())

for line in f1:          #逐行输出
    print("print:",line)
f1.close()
#========Json
print('=' * 10,'json')
import json
l1 = [1,'simple','lsit']
print(type(l1)) #<class 'list'>
print(l1)       #[1, 'simple', 'lsit']

print(json.dumps(l1))  #[1, "simple", "lsit"]
print(type(json.dumps(l1)))  # <class 'str'>