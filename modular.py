'''import time
ticks=time.time()
print("当前时间戳为"+str(ticks))#1970年元旦至今的总秒数

time_str=time.ctime()
print("当前时间字符串为："+time_str)#人类易读时间

localtime=time.localtime()
print("时间元组为："+str(localtime))

print(time.strftime("%Y-%m-%d %H:%M:%S",localtime))
                         #时间模板'''

'''import os#与操作系统交互
print(os.getcwd())#获得当前路径
print(os.listdir('D:\PythonLearn'))#列出当前文件夹及文件
os.mkdir('test_dir')#新建文件夹
os.rmdir('test_dir')#删除文件夹
os.mkdir('test.txt')
os.rename('test.txt','new_test1.txt')#重命名文件
os.rmdir('new_test1.txt')'''

'''import sys #处理命令行参数

#print(sys.argv)#保存命令行参数的列表
print(int(sys.argv[1])+int(sys.argv[2]))'''#运行有报错

#import random
#随机数:按某次实验结果确定，该结果不可预测
#伪随机数：以一个初始数为种子，按照一定算法模拟产生，结果确定

'''print(random.random())#产生[0.0-1.0)之间的伪随机浮点数
print(random.uniform(10,20))#产生[a,b]之间的伪随机浮点数
print(random.randint(10,20))#产生[a,b]之间的伪随机整数
random.seed(10)#手动设置种子
print(random.random())
print(random.random())
'''

'''import math
print(math.pi)
print(math.sin(math.pi/2))#弧度
print(math.pow(2,10))#幂运算
print(math.log(2))
'''













