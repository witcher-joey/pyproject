'''
20221217
并发编程
并发和并行
并行 parallel：同时做某些事，可以互不干扰地 同一时刻 做几件事。
并发 concurrency：同时做某些事，强调 一个时段内 有事情要处理。

并发的解决（若面试中有问，则可以讲这个：高速公路收费站）

高并发：压力大了就是高并发      思考问题的时候从最简单的开始
1、排队（队列-FIFO）就是缓冲区 考虑优先队列 queue模块的类Queue LifoQueue PriorityQueue(小顶堆)
什么时候用缓存（反复计算，耗时长、输入一定），什么时候用缓冲（来不及处理 排队）？

2、争抢
锁机制，排他锁。但是有可能有人很长时间抢不到。

3、预处理    非常重要
提前加载用户需要的数据思路，预处理思想，缓存常用。

4、并行  是并发的一种解决方案  实际中也常用，从硬件角度
成本上升，
日常可购买更多服务器，或开多进程、线程实现并行处理，来解决并发问题。（这些都是水平扩展思想）

如果线程在单CPU上处理，就不是真的并行
现在多数服务器都是多CPU，至少也是单核多CPU，服务器的部署往往是多机的、分布式的。

5、提速    （垂直扩展思想）
提高单个CPU性能，或单个服务器安装更多CPU


6、消息中间件
两套系统之间用的。
高吞吐量，

根据实际情况选择方案。可能是多种方式的优化组合
不要盲目扩大设计。

==============================
queue模块--队列
一、Queue 先进先出
queue.Queue(maxsize=0):1、创建FIFO队列，返回Queue对象。2、maxsize<=0，队列长度没有限制

Queue.get(block=True,timeout=None):
1、从队列中移除元素并返回这个元素
2、block为阻塞，timeout为超时
3、block为True,是阻塞；timeout为None就是一直阻塞
4、block为True但timeout有值，就阻塞到一定秒数抛出Empty异常
5、block为False，是非阻塞，timeout将被忽略，要么成功返回一个元素，要么抛出empty异常。
二、LifoQueue
三、PriorityQueue






'''
from queue import Queue, LifoQueue, PriorityQueue
q = Queue(2)  #  (self, maxsize=0, *, ctx),如果是你设计，采用什么样的数据结构来实现这个Queue(FIFO) Linkedlist(链表)
#尾部加入，头部拿走
q.put(1)
q.put(2)

print(q.get())
print(q.full())
print(q.get())
print(q.full())
#q.get()  #队列有数据，立即获取；没有数据，默认阻塞等待。 多线程解决
#print(q.get(timeout=5))  #等5s后，抛出异常 Empty
print(q.empty())
#q.put(3, True, timeout=3) #如果有空间，加入；否则等3s;  没空间，抛出异常
#q.put_nowait() # 不等
q.qsize()

#========LifoQueue  同上  采用 list（此处列表实现）或链表 数据结构 实现

#========PriorityQueue 小顶堆实现，元素要比较（大小）（放入的元素要满足这个要求）




'''
20221215
网络编程   网络必有
问题：
1、什么是socket套接字？进程间通信的插座。

socket套接字： 插座  对理解网络编程的深层原理很重要，
1、python中提供了socket标准库，很底层的接口
2、socket是通用的网络编程接口，和网络层次没有一一对应关系。

协议族：AF（Address Family）,是socket()的第一参数
AF_INET  IPV4
AF_INET6 IPV6
AF_UNIX  Unix Domain Socket,windows没有

Socket类型
SOCK_STREAM  面向连接的流套接字。默认值，TCP协议
SOCK_DGRAM   无连接的数据报文套接字。   UDP协议

TCP协议是流协议，将数据看作字节流，持续发送这些字节

socket编程：完成一端和另一端的通信（处于不同的进程）。每一个socket对象只表示其中的一端
业务角度：
 主动发送请求一端，客户端
 被动接收一端，服务端
又成为C/S编程。

服务端编程步骤（套路，必须得记住）
总结：先创建对象，然后在这个对象上绑定ip和port（能让别人找到它），绑定后就在这个端口上开始监听。
1、创建socket对象
2、bind()     绑定IP和Port。    IPV4为一个二元组('IP地址字符串'，port)  主机+端口 称为套接字
              绑定ip和port,就是能够让别人找到它
3、listen()   开始监听，将在指定IP的端口上监听。
4、获取用于传送数据的新的socket对象
  socket.accept()->(socket object, address info)
  accpet方法阻塞等待客户端建立连接，返回一个新的socket对象和客户端地址的二元组地址，IPV4中是一个二元组(clientaddr, port)
  接收数据：recv(bufsize,[flags])使用缓冲区接收数据
  发送数据：send(bytes)发送数据

问题：两次绑定同一个监听端口会怎么样? 只能绑定一次

查看监听端口
windows  netstat -anp tcp | findstr 9999 ; a:所有，n：网络，p：协议
linux    netstay -tanl | grep 9999
         ss -tanl | grep 9999
'''


'''
import socket

#创建socket对象 是类文件对象，占用文件描述符，fd有限制
#绑定 ip和端口
#监听 监听客户端的连接请求
#accept 分配新的socket对象 阻塞

server = socket.socket()  #默认 TCP 和 IPV4 所以不带参数  这里得到的是监听用的socket对象
addr = ('127.0.0.1', 9999)  #1024不要用
server.bind(addr) #绑定一次
server.listen()  #监听 等 三次握手建立稳定的可靠连接，放入队列中

print(server)
print('-' * 10)

# 服务端分配的第一个socket

newsocket, raddr = server.accept() #返回一个新的socket和一个二元组（远端的ip和端口）  等着连接
print(newsocket) #用来和客户端通信的
print(raddr)  

print(newsocket.getpeername()) #对端地址和端口
print(newsocket.getsockname()) #本地端口和地址

#收发数据   先收信息，再发信息
#发送数据
data = newsocket.recv(1024)  #阻塞到数据来 bytes类型
print(type(data), data)  #bytes类型


msg = b'hello'
newsocket.send(msg)

#服务端分配第二个socket给另一个客户端进程通信
newsocket2, raddr2 = server.accept()
data2 = newsocket2.recv(1024)
msg2 = b'2222'
newsocket2.send(msg2)

#close
newsocket2.close()
newsocket.close()
server.close()
'''


#======================================
'''
#群聊  20221217
#初始化配置 启动服务 停止服务
import socket
import logging
class server:
    def __int__(self, ip='127.0.0.1', port=9999):
        self.sock = socket.socket()  #阻塞的socket
        self.addr = ip, port
        #下面两句跟启动有关，如果不再初始化后马上启动，就不要
        #self.sock.bind(self.addr)
        #self.sock.listen()


    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()

        client, raddr = self.sock.accept() #服务端分配一个新的socket，供连接通信使用
        #通信连接建立后就开始 收发数据

       #循环后不能停止怎么解决？ 多线程
        while True:
            data = client.recv(1024)  #也是一个阻塞状态
            print(data)
            msg = "msg={}".format(data.decode())  #将bytes类型解为utf-8类型
            logging.info(msg)
            msg = msg.encode()  #编码
            client.send(msg)


    def stop(self):
        self.sock.close()

'''