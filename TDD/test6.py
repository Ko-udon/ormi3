import pdb

def add(a, b):
    return a + b

def test():
    for i in range(10):
        x = add(i, 10)
        pdb.set_trace()
    for i in range(10):
        y = add(i, 100)
        pdb.set_trace()

test()