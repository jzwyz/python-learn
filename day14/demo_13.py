#!/usr/local/bin/python3
"""
多进程和多线程

Unix和Linux 提供了 fork() 系统调用创建进程, 调用fork()函数的是父进程，创建出的是子进程，子进程是父进程的一个拷贝，但是子进程拥有自己的PID;
Python 的 os 模块提供了 fork() 函数;
Windows系统可以使用 multiprocessing 模块的 Process 类来创建子进程;
threading 模块提供的 Thread 类 创建/启动线程;
多线程 锁;
单线程 + 异步I/O
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep
from threading import Thread, Lock


class DownloadTask(Thread):
    """
    类的继承, 封装自己的线程类, 实现 run() 方法
    """

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('文件下载线程启动:正在下载文件[%s]' % (self._filename))
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def download_task(filename):
    print('启动下载进程,进程PID:[%d]' % getpid())
    time_download_random = randint(5, 10)
    sleep(time_download_random)
    print('[%s]下载成功,耗时:%d' % (filename, time_download_random))


def main():
    start = time()
    """
    很懵逼,args参数 元祖后面为什么要加一个,号
    解答:https://zhidao.baidu.com/question/620851933490552492.html
    """
    p1 = Process(target=download_task, args=('1.pdf',))
    '''start()  启动进程'''
    p1.start()
    p2 = Process(target=download_task, args=('2.avi',))
    p2.start()
    '''join() 等待进程执行完成'''
    p1.join()
    p2.join()
    end = time()
    print('进程执行完成,耗时%s' % (end-start))


def thread_main():
    t_start = time()
    t1 = DownloadTask('1.pdf')
    t1.start()
    t2 = DownloadTask('2.avi')
    t2.start()
    t1.join()
    t2.join()
    t_end = time()
    print('文件下载线程执行完成,耗时:%d' % (t_end - t_start))


class Account(object):

    def __init__(self):
        super().__init__()
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money=0):
        self._lock.acquire()  # 操作前开启锁
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()  # 操作完释放锁

    @property
    def balanc(self):
        '''getattrf方法'''
        return self._balance


class AddMoneyTask(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def lock_main():
    print('lock操作')
    account = Account()
    ts = []
    for _ in range(100):
        at = AddMoneyTask(account, 1)
        ts.append(at)
        at.start()
    for ttt in ts:
        ttt.join()
    print('账户余额为:%d' % account.balanc)


if __name__ == "__main__":
    # main()
    # thread_main()
    lock_main()
