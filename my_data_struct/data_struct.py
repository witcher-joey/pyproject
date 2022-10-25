#栈  先进先出 初始化栈  判断栈为空  入栈 出栈 栈顶元素 栈大小
class Stack:
    #初始化栈（创建栈）
    def __init__(self):
        self.items=[]
    #判断为空
    def isEmpty(self):
        self.items==[]
    #入栈 pyhton中 通过在列表插入的方式 本知识点重要的地方
    #有两种append 和 insert
    def push(self,item):
        self.items.append(item)
    #出栈
    def pop(self):
        return self.items.pop()
    #取栈顶元素
    def peek(self):
        return self.items.pop([len(self.items)-1])  #类的函数中的变量都要通过self调用
    def size(self):
        return len(self.items)
#队列