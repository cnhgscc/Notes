"""
编译命令
gcc -O2 -shared -fPIC -I/usr/include/python3.5m/ topk.c -o topk.so
"""

def add(vector, num, required_nums=1):

    tmp = []

    while len(vector):

        cv = vector.pop()
        if cv < num:
            tmp.append(cv)
        else:
            vector.append(cv)
            break

    vector.append(num)

    while len(tmp):
        vector.append(tmp.pop())

    if len(vector) > required_nums: vector.pop()



class TopK:

    def __init__(self, required_nums=1):

        self.required_nums = required_nums

        self.data = []

    def append(self, num):
        add(self.data, num, self.required_nums)
