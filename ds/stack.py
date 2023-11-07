class stack(object):
    def __init__(self):
        self.s = []
    
    def push(self, num):
        self.s.append(num)
        
    def pop(self):
        num = self.s.pop()
        return num

mys = stack()
for x in [5,6,7]:
    mys.push(x)

assert mys.pop()==7
assert mys.pop()==6

mys.push(29)
assert mys.pop()==29
assert mys.pop()==5
