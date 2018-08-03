import time
import inspect
import os
import multiprocessing
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager


class RpcQueueManager(BaseManager):

    @classmethod
    def from_settings(cls, address=('127.0.0.1', 5000), authkey=b'izoeys', qname="task_queue"):
        _queue = Queue()
        RpcQueueManager.register(qname, callable=lambda: _queue)

        return cls(address=address, authkey=authkey)


class XProcess(Process):

    def __init__(self, debug=True, *args, **kwargs):

        super(XProcess, self).__init__(*args, **kwargs)

        self._queue = Queue()
        self.is_run = False
        self.ppid = os.getppid()
        self.debug = debug

    def __str__(self):

        return "<_{0} running:{1} pid={2} ppid={3}>".format(self.name, self.is_run, self.pid, self.ppid)

    def run(self):

        while True:

            self.is_run = False
            task = self._queue.get()
            self.is_run = True

            if self.debug:

                print(self, task)

            if callable(task):
                task()

    def put(self, context):
        self._queue.put(context)


class Task:

    def __init__(self, func, *args, **kwargs):

        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        signature = inspect.signature(self.func)
        name = self.func.__name__
        return "< _Scheduler_Task:{0}{1} args={2} kwargs={3} >".format(name, signature, self.args, self.kwargs)

    def __call__(self):
        self.func(*self.args, **self.kwargs)


class ProcessScheduler:

    def __init__(self, pcount=None, rpc_queue=None, debug=True):
        self.pcount = pcount or multiprocessing.cpu_count()
        self.pool = []

        self.rpc_queue = rpc_queue or []
        self.debug = debug

    def run(self, sleep_time=0.5):

        for i in range(self.pcount):
            pname = "Scheduler Process-{}".format(i+1)
            p = XProcess(name=pname, debug=self.debug)
            self.pool.append(p)
            p.start()

        while True:

            try:
                task = self.rpc_queue.get(timeout=1)
            except Exception:
                if self.debug:
                    time.sleep(sleep_time*8)
                    print("ProcessScheduler Stats: \n count:{}".format(len(self.pool)))
                    for p in self.pool:
                        print(p, p.is_run)
            else:
                self.add_task(task)

            time.sleep(sleep_time)

    def add_task(self, task):

        for xp in self.pool:
            if not xp.is_run:
                xp.put(task)
                break


if __name__ == "__main__":

    def add(x, y):
        print(x + y)
        return x + y

    rpc_manager = RpcQueueManager.from_settings(qname="task_queue")
    rpc_manager.start()
    rpc_task = rpc_manager.task_queue()

    ps = ProcessScheduler(rpc_queue=rpc_task)
    ps.run()
