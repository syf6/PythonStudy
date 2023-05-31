from multiprocessing import Process 
#从模块中导入类
import os,time

#直接实例化Process
#先定义一个方法
def childProcess(second): 
    print("process {} starts and sleep {} seconds".format(os.getpid(),second))
    time.sleep(second) #float
    print("process {} sleep ends".format(os.getpid()))

#childProcess(3)

if __name__ == '__main__': #冒号后必有缩进
    #创建一个多进程
    #target传入函数名,args是可迭代的对象，一般用元组,是指传入函数的参数
    #kwargs是以mapping 也就是字典的方式去传递的，有键值对需要**
    p1 = Process(target=childProcess,args=(10,),name="No1")
    p2 = Process(target=childProcess,args=(2,),name="No2")
    p3 = Process(target=childProcess,args=(3,),name="No3")
    #是否是后台进程,如果是，主进程关闭，后台进程也会关闭释放资源
    #p1.daemon = True
    print("process start")
    #调用线程
    p1.start()
    p2.start()
    p3.start()
    #查看进程的信息 is_alive是一个方法
    print("p1:name={},pid={},is_alive={}".format(p1.name,p1.pid,p1.is_alive()))
    print("p2:name={},pid={},is_alive={}".format(p2.name,p2.pid,p2.is_alive()))
    print("p3:name={},pid={},is_alive={}".format(p3.name,p3.pid,p3.is_alive()))
    #等待子进程结束，如果没有这个，子进程不会结束
    p1.join()
    p2.join()
    p3.join()
    #查看进程的信息
    print("p1:name={},pid={},is_alive={}".format(p1.name,p1.pid,p1.is_alive()))
    print("p2:name={},pid={},is_alive={}".format(p2.name,p2.pid,p2.is_alive()))
    print("p3:name={},pid={},is_alive={}".format(p3.name,p3.pid,p3.is_alive()))
    #日志输出
    print("program over")