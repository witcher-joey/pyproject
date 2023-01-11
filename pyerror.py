# 异常 202318
'''
问题：what why how
 1、什么是异常？
 2、为什么要用异常？
 3、什么时候要用到异常处理？


'''
#example
def fetcj(obj, index):
    return obj[index]

s = 'spam'
try:
    print(fetcj(s,4)) #IndexError: string index out of range
except:
    print("error")