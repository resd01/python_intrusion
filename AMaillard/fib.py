# coding: utf-8
# python 3.7.1 x86_64

__author__ = "Maillard Alexandre"

import time

def fibo(max=50):
    i, a, b = 0, 0, 1
    while True:
        yield a
        if i == max: return
        a, b = b, a + b
        i +=1

start = time.time()
for i, j in enumerate(fibo(max=50)):
    print(f"{i}: {j}")
end = time.time() - start
print(end)
