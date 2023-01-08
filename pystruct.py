#基础数据解构
#列表
'''
列表方法：
  1、l1=extend(l2) 将l2加到l1
  2、append() 末尾添加
  3、remove() 删除第一个
  4、insert(i, 元素) 指定位置插入

列表切片：
  L[start:stop:step]


字符串：
  str.split(指定分割符，分割符分割次数)



'''
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1.extend(list2) #赋值无效
list3 = list1
print(list1)
print(type(list3), list3)
str = "nihao"
str.split()
