#用于python相关知识的学习

#可迭代对象

#可变参数
'''
1、*变量名 => 可变位置参数，可收集多个实参，被收集到一个元祖对象中；可变位置参数，按位置传参。 放在前
2、**变量名 => 可变关键字参数，可接受多个关键字参数，收集实参的名和值，放到dict中。         放在后
'''
'''
# keyword-only参数  仅仅能关键字传参的形参，在*后的参数;  **kwargs放在最后

# positional-only参数   用/   python 3.8开始

参数规则：一般顺序（positional-only参数，普通参数，缺省参数，可变位置参数，keyword-only参数（可带缺省值），可变关键字参数）
见名知意； 最常用的往前放，定义为普通参数

#参数解构
add(*(4,5)) 调用时，对实参加入*；  **{} 仅用于字典 ，等价于k=v。按位置传参
*结构位置传参，**结构关键字传参

'''

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
#逐行读取,使用for循环;;  .strip()消除空白行
with open('pi_digits.txt') as pd:  #with获取的文件对象只在当前with块中
    for str in pd:
        print(str.strip())
        print('===')