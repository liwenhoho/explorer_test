#-*-coding:utf-8-*-

class test(object):
    def __init__(self):
        self.num = 10
        self._num = 20
        self.__num = 30

def test():
    print("--test()--")

def _test2():
    print("--_test2--")

def __test3():
    print("---__test3--")
t = test()
print(t.num)
print(t._num)
print(t.__num)