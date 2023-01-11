#用于python相关知识的学习
#工程上的可靠性和稳定性

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
#=======================输入输出
'''
2023110
输出：
1、格式化输出：
   1）格式化字符字面值: f'str{var1}{var2}...'
      var1 = '2023'
      var2 = '1'
      print(f'this is {var1} {var2}')
   2）str.format(): print('{0} {1}...'.format(var1,var2,...))
     a、大括号数字表示位置传参
     b、还可以用变量名实现关键字传参
2、格式调整
   1）“：” 后面写整数，表示该字段最小字符宽度。对齐时很有用
     

'''
