from my_data_struct import data_struct
from my_data_struct.data_struct import Stack #这才是正确的写法；包名.包中文件名.文件中的类名; import classname/method
# print('this is first test python file!')
# print('all is well')

s=Stack()

print(s.size())
s.push(1)
s.push('all')
s.push('is')
s.push('well')
print(s.size())
print(s.pop())
print(s.size())
print(type(s.isEmpty()))

def po_juice():
    return 1==1
print(type(po_juice()))

tu=(1,)
print(tu)


