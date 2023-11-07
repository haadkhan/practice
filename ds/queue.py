from collections import deque


class queue(object):
    def __init__(self):
        self.q = deque()

    def enq(self, num):
        self.q.append(num)

    def deq(self):
        num = self.q.popleft()
        return num


myq = queue()
for x in [5, 6, 7]:
    myq.enq(x)

assert myq.deq() == 5
assert myq.deq() == 6

myq.enq(29)
assert myq.deq() == 7
assert myq.deq() == 29
