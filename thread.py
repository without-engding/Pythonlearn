'''
线程：进程内部的子任务成为线程

进程：正在运行中的程序

例如
我电脑上有QQ，如果我没有打开QQ，他就只是一个程序，但打开之后，便成为正在运行的程序，简称进程
在打开QQ之后，多个对话框的开展，就是多线程

'''

'''import time
def fun_1(num):
    for i in range(1,num+1):
        print('拿第'+str(i)+'个红杯子，时刻为'+time.ctime()+'\n')
        time.sleep(1)#程序休眠

def fun_2(num):
    for i in range(1,num+1):
        print('拿第'+str(i)+'个绿杯子，时刻为'+time.ctime()+'\n')
        time.sleep(1)#程序休眠

fun_1(5)
fun_2(5)
'''
'''import time
import threading#多线程标准库

def fun_1(num):
    for i in range(1,num+1):
        print('拿第'+str(i)+'个红杯子，时刻为'+time.ctime()+'\n')
        time.sleep(1)#程序休眠

def fun_2(num):
    for i in range(1,num+1):
        print('拿第'+str(i)+'个绿杯子，时刻为'+time.ctime()+'\n')
        time.sleep(1)#程序休眠

thread_1=threading.Thread(target=fun_1,args=(5,))#创建线程
                        #目标函数      函数参数
thread_2=threading.Thread(target=fun_2,args=(5,))
thread_1.start()#线程1启动
thread_2.start()
#多线程同时工作，提高程序运行效率

#线程阻塞：线程先暂停，等某一件事情完成之后再执行
#print('所有任务执行完毕','\n')
#当程序运行起来时，会产生一个主线程和程序中的两个线程，主线程主要生成子线程和print，因此会导致主线程和子线程分支运行
#专业术语为线程异步

#阻塞主线程
thread_1.join()#子线程调用join函数是让主线程等子线程完全调用结束之后再运行
thread_2.join()
print('所有任务执行完毕')'''

#线程同步
'''import time
import threading

cap_num=0

def fun_1(num):
    global cap_num

    for i in range(1,num+1):
        cap_num+=1
        print('甲放一个杯子，当前杯子数量为'+str(cap_num)+'\n')
        time.sleep(1)


def fun_2(num):
    global cap_num

    for i in range(1, num + 1):
        cap_num += 1
        #print('乙放一个杯子，当前杯子数量为' + str(cap_num) + '\n')
        time.sleep(1)

thread_1=threading.Thread(target=fun_1,args=(5,))
thread_2=threading.Thread(target=fun_2,args=(5,))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print('ALL thread finished')'''

#原因：资源抢夺，两个线程同时在修改杯子的数量，造成混乱
#例如，打印机，如果不做规定，两个人发送的不同内容会打印到同一张纸上

#实现杯子数量只能由一个线程进行修改，不能同时修改
import time
import threading

cap_num=0
lock=threading.Lock()#线程锁

def fun_1(num):
    global cap_num
    global lock

    lock.acquire()#加锁
    for i in range(1,num+1):
        cap_num+=1
        print('甲放一个杯子，当前杯子数量为'+str(cap_num)+'\n')
        time.sleep(1)
    lock.release()


def fun_2(num):
    global cap_num
    global lock

    lock.acquire()
    for i in range(1, num + 1):
        cap_num += 1
        print('乙放一个杯子，当前杯子数量为' + str(cap_num) + '\n')
        time.sleep(1)
    lock.release()

thread_1=threading.Thread(target=fun_1,args=(5,))
thread_2=threading.Thread(target=fun_2,args=(5,))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print('ALL thread finished')
#在多线程中，对全局变量的修改一定要进行加锁和解锁操作，保证程序执行的顺序
