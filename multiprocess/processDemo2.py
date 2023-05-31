from multiprocessing import Process
import os,time

#在复杂环境中，重写子进程
class ChildProcess(Process):
    def __init__(self,second,name='') -> None: #不返回任何东西
        #super().__init__(self)
        Process.__init__(self) #这里需要直接调用Process类
        self.second = second
        if self.second < 0:
            self.second = 0
        else:
            self.second = second # 在这里传递参数

        if name: #如果名字不为空
            self.name = name #可以做逻辑上校验处理
    
    #重写run的方法,不能这样直接加second，因为是重写
    #def run(self,second) -> None:
    def run(self) -> None:
        print("process {} start to sleep {} seconds".format(os.getpid(),self.second))
        time.sleep(self.second)
        print("process {} sleep over".format(os.getpid()))

if __name__ == '__main__': 
    p1=ChildProcess(10,name = 'No1') #这里必须指定参数名
    p2=ChildProcess(second = 2,name = 'No2')
    p3=ChildProcess(second =1,name = 'No3')

    #和之前一样
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
