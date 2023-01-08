'''
网络爬虫视角：网络上的任何一个内容都有一个url与之对应
网络爬虫尺寸
一、爬取网页 玩转网页：Requests库；小规模，数据量小；爬取速度不敏感
二、爬取网站 爬取系列网站：Scrapy库；中规模，数据规模较大；爬取速度敏感
三、爬取全网: 定制开发；大规模，搜索引擎；爬取速度关键

爬虫的限制
1、来源审查：判断User-Agent进行限制
2、发布公告：Robots协议（网络爬虫排除标准）
    *:所有   / ：根目录
    User-agent: 指定哪些爬虫  ;  Disallow: 指定访问范围
    网站根目录下放置robots文件



Requests:自动爬去Html页面，自动网络请求提交
# 7个主要方法   与HTTP协议方法对应
1、requests.request() 构造一个请求，支撑以下各方法的基础方法
2、requests.get()  获取html网页的主要方法，对应http的GET
   r=requests.get(url) 构造一个向服务器请求资源的Request对象，并返回一个包含服务器资源的Response对象给 r。
                       Response:返回了服务器全部内容
   response对象属性：
       r.status_code       http请求的返回状态，200表示连接成功，404表示失败



       r.text             http响应内容的字符串形式，url对应的页面内容
       r.encoding         从http header 中猜测的响应内容编码方式
         如果header中不存在charset，则认为编码为 ISO-8859-1
       r.apparent_encoding  从内容分析出的响应内容编码方式（备选编码方式）
       r.content           http 响应内容的二进制形式
   response方法：
              r.raise_for_status()   如果状态不是200，引发HTTPError异常


3、requests.head() 获取html网页头信息的方法，对应http的HEAD
4、requests.post() 向html网页提交POST请求方法,对应http的POST
5、requests.put()  向html提交PUT方法，对应http的PUT
6、requests.patch()向html提交局部修改请求，对应http的PATCH    主要好处：节省网络带宽
7、requests.delete() 向html提交删除请求，对应 DELETE

Requests库的异常
  requests.ConnectionError  网络连接错误异常，如DNS查询失败、拒绝连接等
  requests.HttpError        HTTP异常
  requests.URLReuired       URL缺失异常
  requests.TooManyRedirects 超过最大重定向次数，产生重定向异常
  requests.ConnectTimeout   连接远程服务器超时异常
  requests.Timeout          请求URL超时，产生超时异常




爬取网页通用代码框架：
import requests

def getHtmltext(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
    return "异常"

if __name__ == "__main__":
    url = "   "
    print(getHtmlText(url))



'''

#Beautiful Soup: 解析HTML页面 信息标记与提取方法
'''
from bs4 import BeautifulSoup 
 #beautifulsoup库是解析、遍历、维护、“标签树”的功能库
#BeautifulSoup(demo, "html.parser") # 第一个是需要解析的html格式的信息，第二个是解析器

Beautiful Soup 类的基本元素（Tag,Name,Attributes,NavigableString(非属性字符),Comment（注释））

库的解析器： 
1、bs4 html: BeautifulSoup(解析内容,'html.parser') 安装bs4库
2、lxml html：BeautifulSoup(解析内容,'lxml')   pip install lxml
3、lxml xml：BeautifulSoup(解析内容,'xml') pip install lxml
4、html5lib :BeautifulSoup(解析内容,'html5lib') pip install html5lib

Html 内容遍历 （上下左右）
1、标签树下行遍历 
   a. .contents    子节点的列表，将<tag>所有儿子节点存入列表   返回的是列表
   b. .children    子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
   c. .descendants 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
2、标签树上行遍历
   a. .parent  节点父亲标签
   b. .parents 节点先辈标签的迭代类型，用于循环遍历先辈节点
3、标签树平行遍历 针对同一个父节点
   a. .next_sibling      返回按照HTML文本顺序的下一个平行节点标签
   b. .previous_sibling  返回按照HTML文本顺序的上一个平行节点标签
   c. .next_siblings     迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
   d. .previous_siblings 迭代类型，返回按照HTML文本顺序的前续所有平行节点标签
   
信息标记  使能够理解信息的含义
标记的意义：1、形成信息组织结构，增加信息维度；2、可用于通信、存储或展示；3、有利于程序理解和运用 
信息标记形式：
    xml（可扩展性好，但繁琐：Internet信息交互与传递）； 
    json（信息有类型，适合程序处理，较xml简洁：移动应用云端和节点的信息通信，无注释）； 
    yaml（信息无类型，文本信息比例最高，可读性好：各类系统的配置文件，有注释易读）
信息提取：从标记后的信息提取
    1、完整解析信息的标记形式，再提取关键信息。需要标记解析器。优点：信息解析准确；缺点：提取过程繁琐，速度慢
    2、无视标记形式，直接搜索信息。 对信息的文本查找函数即可。 优点：提取过程简洁，速度较快。缺点：提取结果准确性与信息内容相关。
    3、融合方法：将1 2 结合。

#查找demo中所有的链接
<>.find_all(name, attrs, recursive, string, **kwargs) 返回一个列表类型，存储查找的结果
name：对标签名称的检索字符串
attrs:对标签属性值的检索字符串，可标注属性检索。  
recursive:是否对子孙全部检索，默认True
string:<>...</>中字符串区域的检索字符串。


soup = BeautifulSoup(demo, "html,parser")
for link in soup.find_all('a')
    print(link.get('href'))

'''



'''
Re： 正则表达式，提取页面关键信息。




'''
import requests
# r = requests.get("http://www.baidu.com")
#
# print(r.status_code)
# print(type(r))
# print(r.headers)
# print(r.apparent_encoding)
# print(r.content)
# print(r.text)
# print(r.encoding)
# print('-' * 20)
# r.encoding = 'utf-8'
# print(r.text)
# print(r.apparent_encoding)

'''

def getHtmlText(url):
    try:
        # 修改头部 User-Agent
        kv = {'User-Agent': 'Mozilla/5.0'}
        keyword = {'wd':'Python'}
        r = requests.get(url, headers = kv, params=keyword)  #关键字修改

        r.raise_for_status()
        print(r.request.url)
        print(r.apparent_encoding)
        
        r.encoding = r.apparent_encoding

        print(r.headers)
        print(r.request.headers)
        print(r.request.headers['User-Agent'])

        print(len(r.text))
        print('=' * 30)
       # print(r.text)


    except:
        print("错误")

'''
#ip地址查询
# def getIp(url1):
#
#     r = requests.get(url1)  # 获取地址资源
#     print(r.status_code)

'''
from bs4 import BeautifulSoup  # 类


if __name__ == '__main__':
    #url = "http://c.biancheng.net/view/2380.html"
    #url = "http://www.baidu.com/s"  #百度关键词接口
    #url1 = "https://m.ip138.com/iplookup.asp?ip="
    #url2 = "https://www.cnblogs.com/byron0918/p/10209341.html"
    r = requests.get("http://python123.io/ws/demo.html")
    print(r.status_code)
    #print(r.text)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser") # 第一个是需要解析的html格式的信息，第二个是解析器
    print(soup.title)
    print(soup.a.parent.name)
    tag = soup.a
    print(tag)
    print(tag.attrs) #标签属性
    print(type(tag)) #
    print(tag.string)  #标签之间的字符串
    print(type(tag.string))   # <class 'bs4.element.NavigableString'>

    #print(soup.prettify())  #为标签和文本添加换行符。

    #getIp(url2)
    #getHtmlText(url)
'''

#功能描述：
#输入： 大学排名URL连接
#输出：大学排名信息的屏幕输出（排名，大学名称，总分）
#技术路线
#定向爬虫：仅对输入URL进行爬取，不扩展爬取
#程序结构设计
#1、从网络上获取大学排名网页内容
#2、提取网页内容中信息到合适的数据结构
#3、利用数据结构展示并输出结果

import bs4  #使用标签类型定义
from bs4 import BeautifulSoup
import requests

def getHtml(url):
    try:
        ht = requests.get(url)  #得到连接的页面
        ht.raise_for_status()  # 抛出状态异常，以便被捕获
        ht.encoding = ht.apparent_encoding #编码更改,根据页面中的编码来定义实际编码
        return ht.text

    except:
        print("异常")

def fillList(ulist, html): #将页面中的内容解析并提取到列表中
    soup = BeautifulSoup(html, 'html.parser')
    #解析后找到所需内容标签   table->thead(排名、学校名称、省市、类型、总分) tbody（tr的父标签）->tr
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):   #过滤非标签类型信息 #现在该网页源码（标签分布有变）
            #print('fill',tr('td'))
            tds = tr('td')  #保存tr下的所有td标签  没太明白
            ulist.append([tds[0].text , tds[1].text, tds[2].text])  #以列表的形式加入到列表中
            #将标签的内容放到列表中

def printInfo(ulist, num):
    # 采用中文字符填充 chr(12288)
    #print("{:^10}\t{:^100}\t{:^10}".format("排名", "学校名称", "省市"))
    splt = "{0:^10}\t{1:{3}<80}\t{2:<10}"
    print(splt.format("排名", "学校名称", "省市", chr(12288)))
    for i in range(num):
        u = ulist[i]
        #print("printInfo", u[0])
        print(splt.format(u[0].strip(), u[1].strip(), u[2].strip(), chr(12288)))

    return

def main():
    uinfo = []  #用于存放从页面中获取的数据
    url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
    html = getHtml(url)  # 将获取的页面保存在一个变量中
    fillList(uinfo, html) #将html页面中的内容用一个列表（uinfo）保存起来
    printInfo(uinfo, 20)

main()

