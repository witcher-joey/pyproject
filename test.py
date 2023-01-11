from my_data_struct import data_struct
from my_data_struct.data_struct import myStack #这才是正确的写法；包名.包中文件名.文件中的类名; import classname/method
# print('this is first test python file!')
# print('all is well')

s=myStack()

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

#移到hdd上后的测试
hdd = "移动到hdd后的测试"
print(hdd)
if hdd:
    print("if hdd not none:",hdd)

import requests

r = requests.get("https://www.shanghairanking.cn/rankings/bcur/2022")
print(r.status_code)
#=========
D = {'a':1,'b':2}
print(D)
print(str(D))
print(type(D))
print(type(str(D)))
#=======输出
print('输出')
var1 = '2023'
var2 = '1'
print(f'this is {var1} {var2}')
#=======列表
lis = [{'Name': 'Joey', 'Age': '26', 'Birthday': '1996'}, {'Name': 'Yu', 'Age': '0', 'Birthday': '2023'}]
print(lis[0]['Name']) #列表中第一个元素=>字典；访问字典关键字Name=>Joey

out = 'Name,Age,Birthday'
obj = {'Name': 'Joey', 'Age': '26', 'Birthday': '1996'}
print(obj['Name'])

out += f'\n{obj["Name"]},{obj["Age"]},{obj["Birthday"]}' # 'Name' 报错;“Name” 才对 为什么？ # +=字符拼接

print(out)

s1 = '123'
s2 = '456'
s1 += s2
print(s1)