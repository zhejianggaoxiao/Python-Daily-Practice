"""
-------------------------------------------------
   File Name：     5.3-binary_search
   Description :
   Author :       gaox
   date：          7/30/18
-------------------------------------------------
   Change Activity:
                   7/30/18:
-------------------------------------------------
"""
__author__ = 'gaox'

def binary_search(data, item):
    s = 0
    e = len(data)-1
    while s<=e:
        m = (s+e)//2
        if data[m]<item:
            s=m+1
        elif data[m]>item:
            e=m-1
        else:
            return m
    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))