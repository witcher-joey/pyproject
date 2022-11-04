#py 函数

#生成器、迭代器、装饰器


#=============================================闭包=====================================================
#闭包
'''
定义：延伸了作用域的函数，能够引用嵌套函数（定义体）外封闭函数内的非全局变量。
场景：只有涉及嵌套函数时才会有闭包问题。

def 外部函数（）：
    变量
    def 嵌套函数（）：
        处理（自由）变量
        return 嵌套函数处理结果
    return 嵌套函数       #此处不带括号，返回的是嵌套函数本身。因为要从外部访问内部的嵌套函数，所以在这里返回。外部函数就是接口。
闭包=变量+嵌套函数

'''
'''
闭包示例
写一个加10的闭包函数

#写法一    自我测试    后面装饰器会用这种写法
def add_func(num):      #参数从外部函数传递
    var_num=10
    def add_ten():
        return var_num+num
    return add_ten()   #带括号，得到的是执行后的结果
print(add_func(10))

#写法二    用改写法
def add_func():
    var_num=10
    def add_ten(num):    #参数从嵌套函数传递
        return var_num+num
    return add_ten

res_add_ten=add_func()  #  add_func()得到的是add_ten函数本身,
print(res_add_ten(10))     #add_ten()获得了参数
print(add_func()(10))

'''
# 柯里化   可以拆分函数
'''
将原来接受两个参数的函数变成新的接受一个参数的函数的过程，新的函数返回一个以原有第二个参数为参数的函数。
将fnu(x,y)变成fn(x)(y)
'''
def add(x,y,z):
    return x+y+z
#add(4)(5,6)
def add(x):
    def inner(y,z):
        return x+y+z
    return inner
print(add(4)(5,6))

##这个例子很关键！！！
#add(4)(5)(6)
def add(x):
    def outinner(y):
        def ininner(z):
            print(z)    #z=6
            return x+y+z
        return ininner
    return outinner
print(add(4)(5)(6))   # 从外往内，依次调用
#add(4,5)(6)


#==================================================装饰器========================================================
#装饰器
'''
什么是装饰器？：python中的一种设计模式，允许用户在不修改函数本身的情况下向函数增加新的功能。
怎么用？：定义在被装饰函数的前面   @装饰函数； 带有内部函数的包装函数
有什么用（用来干什么）？：说白了就是装饰，用来装饰函数或类
什么时候用？：

def 装饰函数：
    def wrapper():
        装饰处理
        被装饰函数调用
        return 处理结果
    return wrapper      #外部函数返回内部函数是为了，通过外部函数接口访问到内部函数
     
@装饰函数       #此处运行机制：将下面的函数名作为参数（实参）传入， xyz=装饰函数(xyz) #两边的xyz不是同一个东西
def 被装饰函数：      def xyz():                      #左边的xyz指向了wrapper里的被装饰函数（闭包自由变量绑定的概念）
    pass               pass                         #右边的warpper指向外面的被装饰函数
    


#非业务代码写在业务代码中，不好

# 实参传递，关键字(**kwargs)和位置传参（*args）
'''
'''
2022114->
def add(x,y,*z):
    return x+y+sum(z)

def logger(fn,*args,**kwargs):   #可变参数
    print('装饰前')
    print('{} function called. {} {}'.format(fn.__name__, args, kwargs))
    #调用被装饰函数
    res=fn(*args,**kwargs) #参数解构，*args变成位置传参，**kwargs变成关键字传参。如果不加*和**，传的就是元祖或字典，add函数就无法接收
    print('装饰后')
    return res
logger(add,1,y=10)

柯里化后：
def logger(fn):
    def wrapper(*arg,**kwarg):
        print('{} function called. {} {}'.format(fn.__name__, args, kwargs))
        #调用被装饰函数
        res=fn(*args,**kwargs) #参数解构，*args变成位置传参，**kwargs变成关键字传参。如果不加*和**，传的就是元祖或字典，add函数就无法接收
        print('装饰后')
        return res
    return wrapper
    
add=logger(add)
result=add(1,2)
print(result)
    
写成装饰器模式
def logger(fn):      #装饰函数   装饰器函数
    def wrapper(*arg,**kwarg):
        print('{} function called. {} {}'.format(fn.__name__, args, kwargs))
        #调用被装饰函数
        res=fn(*args,**kwargs) #参数解构，*args变成位置传参，**kwargs变成关键字传参。如果不加*和**，传的就是元祖或字典，add函数就无法接收
        print('装饰后')
        return res
    return wrapper
                
                # 学习期间一定要把等价式写在后面   此处很重要
@logger         #无参装饰器, 是一种语法糖 .本质上等效为 一个参数的函数   #等价于 add=logger(add)<=>add=wrapper
def add(x,y,*z):
    return x+y+sum(z)
<-2022114    
'''
#写个记录函数执行时长的装饰器
import datetime
import time
def logger(fn):
    def wrapper(*args, **kwargs):
        start=datetime.datetime.now()
        res = fn(*args, **kwargs)
        use_time=(datetime.datetime.now() - start).total_seconds()  #total_seconds()将时间记为秒
        print('{} took {}s'.format(fn.__name__, use_time))
        return res

    return wrapper

@logger  #add=logger(add)<=>add=wrapper
def add(x, y, *z):
    time.sleep(2)
    return x + y + sum(z)
print(add(1,2))



'''
装饰器示例
#定义一个普通函数，返回一个字符串；再定义一个装饰函数，将普通函数的返回字符串大写。
#普通函数
def low_func():
    return 'all is well'
#装饰函数
def upper_func():
    def wrapper(func):         #内部函数接收到要处理的外部函数，获取外部函数的处理结果，然后将结果根据需求处理（核心），最后返回结果
        res_str=func()
        res_upper=res_str.upper()
        return res_upper
    return wrapper   #外部函数返回内部函数是为了，通过外部函数接口访问到内部函数

wrapper_func=upper_func()  #得到wrapper
wrapper_func(low_func)   #得到wrapper()后的结果（res_upper）;注意：传入的是函数本身
print('普通函数+闭包写法：',wrapper_func(low_func))#再输出一下


#写成装饰器模式，用@打包

#错误示例
@upper_func
def low_func():      #意外：出错了。为什么？因为外部函数upper_func()并没有接收到参数
    return 'all is well'

#正确示例
def upper_func(func):
    def wrapper():
        res_str=func()
        res_upper=res_str.upper()
        return res_upper
    return wrapper

@upper_func         #low_func作为参数（此处不带括号），传入upper_func()
def low_func():
    return 'all is well'

print('装饰器的写法：',low_func())  #被装饰器装饰后，可直接调用函数本身得到装饰后的结果

'''

#装饰器函数中接收参数（内部嵌套函数接受参数）
'''
知道内部执行流程后，不用每次都去细想。熟悉后知道怎么用就行了。
'''
#写一个普通函数格式化输出一串字符（一句话），不返回，直接打印；写一个装饰函数在原函数的基础上再加一句话。
#结果写法：先写装饰函数，再写原函数；思考写法：先写原函数，再写装饰函数
def print_full_name(first_name,last_name,country):
    print("I am {} {}. I love to learn".format(first_name,last_name,country))

def decorator_func(func):
    def wrapper_accept_paraments(par1,par2,par3):   #内部函数接收被装饰函数的参数
        func(par1,par2,par3)                          #执行被装饰函数
        print("I live in {}".format(par3))         #装饰：后面再加一句
    return wrapper_accept_paraments

@decorator_func
def print_full_name(first_name,last_name,country):
    print("I am {} {}. I love to learn".format(first_name,last_name,country))
print_full_name('zhou','joey','San')

#I am zhou joey. I love to learn
#I live in San
