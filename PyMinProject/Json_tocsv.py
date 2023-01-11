#Json to CSV 2023110
'''
步骤：
 1、打开Json文件，可读方式
 2、转换json格式数据至 csv数据 ；将json文件反序列化python对象
 3、将csv数据写入文件
'''
import json

if __name__ == '__main__':
    with open('input.json') as f:
        data = json.loads(f.read())  #将 f.read() 反序列化为一个python对象，因为json数据保存在[]中，所以data会得到一个[]
                                    #核心部分  数据转换loads()

    output = ','.join([*data[0]])  #<class 'str'> Name,Age,Birthday 将关键字之间用逗号分隔
    #这部分就是做数据拼接
    for obj in data:
        output += f'{obj["Name"]},{obj["Age"]},{obj["Birthday"]}'

        #print('obj:',obj) #<class 'dict'>
                         #{'Name': 'Joey', 'Age': '26', 'Birthday': '1996'} {'Name': 'Yu', 'Age': '0', 'Birthday': '2023'}

    with open('output.csv','w') as f: #将转换后的数据写入csv文件
        f.write(output)


    # print(data) #[{'Name': 'Joey', 'Age': '26', 'Birthday': '1996'}, {'Name': 'Yu', 'Age': '0', 'Birthday': '2023'}]
    # print(data[0])  # <class 'dict'>  {'Name': 'Joey', 'Age': '26', 'Birthday': '1996'}
    # print(*data[0])   # 参数结构  data[0]是一个字典类型，*data[0]结构，就得到的字典的关键字  Name Age Birthday
    #print(f.read())   #ValueError: I/O operation on closed file. 因为with结束后会自动close()
