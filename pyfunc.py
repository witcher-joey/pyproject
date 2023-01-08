#py 函数
#对每个知识点，理解后，怎样才能记住它？
#魔术方法 20221217=======================================================
'''
分类：
1、创建、初始化、销毁：__new__\__init__与__del__
  1)类创建对象时：
  a、为对象在内存中分配空间(__new__)；b、为对象属性设置初始值(__init__)
     先 __new__ 后 __init__,需要的参数跟__init__有关
  2)__init__ ：专门用来定义一个类具有哪些属性方法!;对象初始化，定义实例属性
  3)__new__ 由基类object提供的内置静态方法：
    a、在内存中为对象分配空间；b、返回对象的引用；
    c、重写__new__方法一定要 return super().__new__(cls)(得不到对象引用就不会调用对象初始化方法)（返回基类的new方法+）
    d、静态方法，调用时需(cls)   什么是静态方法？


2、可视化
3、bash
4、bool
__bool__  没有定义__bool__(),就找__len__()返回长度，非0为真。若__len__()也没定义，那么所有实例都返回真。
空容器是false list\set\tuple\dict

5、运算符重载
  定义：为运算符定义方法；  作用：让自定义的实例对象实现运算符操作。

6、容器与大小
7、可调用对象
8、上下文管理
9、反射
10、描述器
11、其他
   1）__repr__() 显示属性
   在输出实例化对象时，调用的是该对象的__repr__()方法，输出的是__repr__()方法的返回值。
   默认输出的是：类名+object+内存地址
   __repr__()：每个类都包含这个方法（因为object包含这个方法）；
               重写这个方法可以得到想要的信息（直接： return 想要的信息）。
   2）__dir__() 查看对象内置的方法
   3)__call__() 实例方法，功能类似于在类中重载()运算符，使得实例对象可以像调用普通函数那样，以“对象名()”形式使用。
     class A:
         def __call__():
             print()
     a = A()
     a()  #调用的类中的__call__方法，得到print()里的内容
'''





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
# 柯里化   可以拆分函数    解决装饰器最好的武器
'''
将原来接受两个参数的函数变成新的接受一个参数的函数的过程，新的函数返回一个以原有第二个参数为参数的函数。
将fnu(x,y)变成fn(x)(y)

#示例
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
'''



#==================================================装饰器========================================================
#装饰器
'''
总结：
什么是装饰器？：python中的一种设计模式，允许用户在不修改函数本身的情况下向函数增加新的功能。
构成装饰器的条件：有闭包（就有自由变量的绑定）
怎么用？：定义在被装饰函数的前面   @装饰函数； 带有内部函数的包装函数
有什么用（用来干什么）？：说白了就是装饰，用来装饰函数或类
什么时候用？：
怎么写？：先写被装饰函数，再写装饰函数（装饰器），最后调整位置。
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

@logger 
def add(x, y, *z):       #add=logger(add)<=>add=wrapper
    time.sleep(2)
    return x + y + sum(z)
print(add(1,2))
    
<-2022114    
'''



'''
装饰器示例--无参装饰器

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
#带参装饰器--2022115
'''
每次学习新知识之前，都要提前问自己些问题。
1、这个是什么（what）？2、这个用来干什么，怎么用（how）？3、这个在哪里用（where）？4、这个和现有知识如何产生联系？
'''
'''
#文档字符串   函数语句块的第一句   可使用特殊属性__doc__访问这个文档
干什么：描述函数功能、参数含义
如何使用：
def add():
    """
    add document#第一行
    x int:
    y int:
    return int:
    """
#add.__name__  #在pycharm控制台中输出需要用print
print(add.__name__)
print(add.__doc__)
help(add)
'''

# 要使add.__name__得到的是add 而不是wrapper,使用覆盖；；属性拷贝
import datetime
import time


# wrapper.__name__=fn.__name__
# wrapper.__doc__=fn.__doc__
# 覆盖
# def copy_properties(dst, src):
#     dst.__name__ = src.__name__  # dst <- wrapper; src <- fn
#     dst.__doc__ = src.__doc__
#将上述注释柯里化
'''
def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__  # dst <- wrapper; src <- fn  #闭包 记住dst
        dst.__doc__ = src.__doc__
        return dst   #如果不返回，则wrapper=None
    return _copy

def logger(fn):
                          #cop_properties(fn)是一个整体   wrapper=cop_properties(fn)(wrapper)=》wrapper=wrapper
    @copy_properties(fn)  # 等价于 wrapper=cop_properties(fn)(wrapper) 《==》_copy(fn) 带参装饰器
    def wrapper(*args, **kwargs): #执行过程：将wrapper作为参数传入copy_properties(fn),之后再将结果赋给wrapper，如上
        """wrapper function"""
        start=datetime.datetime.now()
        res = fn(*args, **kwargs)
        use_time=(datetime.datetime.now() - start).total_seconds()  #total_seconds()将时间记为秒
        print('{} took {}s'.format(fn.__name__, use_time))
        return res
    #copy_properties(wrapper, fn)    #调用后，全局（外部）print(add.__name__和add.__doc__时就会显示外部的add)
                                    #从而将内部wrapper隐藏起来。
    #cop_properties(wrapper)(fn)      #_copy(fn)  将此调用方法写到上面，写成装饰模式
    #copy_properties(fn)(wrapper)     #将copy_properties(dst)换成copy_properties(src)后
    return wrapper

@logger
def add(x, y, *z):       #add=logger(add)<=>add=wrapper
    """add function"""
    time.sleep(2)
    return x + y + sum(z)

print(add.__name__,':',add.__doc__)
'''
'''

#必须驾驭下面的内容
#logger设定一个阈值，对执行时长超过阈值的记录一下
def copy_properties(src):   #覆盖wrapper的名，用add覆盖（伪装）
    def _copy(dst):
        dst.__name__ = src.__name__  # dst <- wrapper; src <- fn  #闭包 记住dst
        dst.__doc__ = src.__doc__
        return dst   #如果不返回，则wrapper=None；返回后fn.__name__=add
    return _copy
                     #output 函数定义
def logger(duration, output = lambda name, usetime: print("{} tooks {}s slow".format(name, usetime))): #思考：如果在logger中继续添加参数（有明确含义的业务参数），该怎么解决？
    def _logger(fn):
        # cop_properties(fn)是一个整体   wrapper=cop_properties(fn)(wrapper)=》wrapper=wrapper
        @copy_properties(fn)  # 等价于 wrapper=cop_properties(fn)(wrapper) 《==》_copy(fn) 带参装饰器
        def wrapper(*args, **kwargs):  # 执行过程：将wrapper作为参数传入copy_properties(fn),之后再将结果赋给wrapper，如上
            """wrapper function"""
            start = datetime.datetime.now()
            res = fn(*args, **kwargs)
            use_time = (datetime.datetime.now() - start).total_seconds()  # total_seconds()将时间记为秒
            #如果超出阈值，记录一下，为了灵活，对超出阈值的信息用一个函数记录
            if use_time > duration:
                output(fn.__name__,use_time)  #记录函数调用
            # if use_time > duration:   #来自外部的参数，外面用带参装饰器解决
            #     print('{} took {}s. Slow'.format(fn.__name__, use_time))
            # else:
            #     print('{} took {}s fast'.format(fn.__name__, use_time))
            # return res
        # copy_properties(wrapper, fn)    #调用后，全局（外部）print(add.__name__和add.__doc__时就会显示外部的add)
        # 从而将内部wrapper隐藏起来。
        # cop_properties(wrapper)(fn)      #_copy(fn)  将此调用方法写到上面，写成装饰模式
        # copy_properties(fn)(wrapper)     #将copy_properties(dst)换成copy_properties(src)后
        return wrapper
    return _logger

@logger(5)  #add=logger(5)(add)=>add=_logger(add)=>add=wrapper=>add(x,y,*z)=wrapper(x,y,*z)
def add(x, y, *z):  # add=logger(add)<=>add=wrapper
    """add function"""
    time.sleep(2)
    return x + y + sum(z)

add(4,5)             #调用函数本身即可
'''


#装饰器函数中接收参数（内部嵌套函数接受参数）
'''
知道内部执行流程后，不用每次都去细想。熟悉后知道怎么用就行了。
'''
#写一个普通函数格式化输出一串字符（一句话），不返回，直接打印；写一个装饰函数在原函数的基础上再加一句话。
#结果写法：先写装饰函数，再写原函数；思考写法：先写原函数，再写装饰函数
'''
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
'''

#属性更新--20221111
'''
from functools import wraps
@wraps(fn)             #wraps必须返回一个单参函数；；用来解决文档、名称等问题
def 装饰函数
'''

#装饰器进阶--20221125
'''
思考问题：（这几个问题搞清楚，装饰器就ok了）
1、add函数、sub函数执行吗？logger什么时候执行？logger执行过几次？
2、wraps装饰器执行过几次？
3、wrapper的__name__等属性被覆盖过几次？
4、add.__name__打印什么名称？
5、sub.__name__打印什么名称？

尝试回答：（不能想当然的回答，要思考、推理、分析）
1、执行过；装饰的时候执行；两次
正确回答{没有执行（因为没有调用()）；}
2、两次
3、两次
4、add
5、sub

'''

import  datetime
import time
from functools import wraps

#定义一个装饰函数,为被装饰函数添加执行的时间
def logger(fn):  #fn用来接收被装饰函数
    @wraps(fn)  #用来属性更新,从functools导入
    def wrapper(*args,**kwargs):  #用来接收被装饰函数的参数
                                 #为什么此处来接收被装饰函数参数？只需要思考logger(fn,*args,**kwargs)柯里化就明白了。
                                 #logger执行时，临时创建内部函数对象，如同局部变量一样
        start=datetime.datetime.now()
        ret=fn(*args,**kwargs)#这里的*和**是表示参数解构，与上面的含义不同；上面表示接收位置参数和关键字传参。原函数（被装饰函数）
                              #闭包，原来的fn（add和sub），外部函数的局部变量
        use_time=(datetime.datetime.now()-start).total_seconds()
        print(use_time)
        return ret     #返回的是被装饰函数
    return wrapper

#定义被装饰函数
@logger
def add(x,y):
    return x+y

@logger         #函数的每一次调用都是独立的
def sub(x,y):
    return x-y

print(add.__name__,add.__doc__)
print(sub.__name__,sub.__doc__)