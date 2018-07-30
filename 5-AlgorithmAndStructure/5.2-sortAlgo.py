"""
-------------------------------------------------
   File Name：     5.2-sortAlgo
   Description :
   Author :       gaox
   date：          7/30/18
-------------------------------------------------
   Change Activity:
                   7/30/18:
-------------------------------------------------
"""
__author__ = 'gaox'


def Insert_sort(data):
    if not data:
        return

    N = len(data)
    for i in range(1, N):
        tmp = data[i]
        j = i
        while j > 0 and data[j - 1] > tmp:
            data[j] = data[j - 1]
            j -= 1
        data[j] = tmp
    return data


def Shell_sort(data):
    if not data:
        return

    N = len(data)
    D = N // 2
    while D > 0:
        for i in range(D, N):
            tmp = data[i]
            j = i
            while j > D - 1 and data[j - D] > tmp:
                data[j] = data[j - D]
                j -= D
            data[j] = tmp
        D //= 2
    return data


def Select_sort(data):
    if not data:
        return

    N = len(data)

    for i in range(N ):  # 至多交换n-1次
        min_ind = i
        for j in range(i , N):
            if data[j] < data[min_ind]:
                min_ind = j
        if min_ind != i:
            data[min_ind], data[i] = data[i], data[min_ind]
    return data


def Quick_sort(data):
    if len(data)<=1:
        return data

    q = data[0]
    left = Quick_sort([x for x in data[1:] if x <= q])
    right = Quick_sort([x for x in data[1:] if x > q])
    return left + [q] + right


def Merge_sort(data):
    if len(data)<=1:
        return data

    m = len(data) // 2

    left = Merge_sort(data[:m])
    right = Merge_sort(data[m:])

    return Merge_core(left, right)


def Merge_core(A, B):
    l = 0
    r = 0
    res = []
    while l < len(A) and r < len(B):
        if A[l] <= B[r]:
            res.append(A[l])
            l += 1
        else:
            res.append(B[r])
            r += 1
    res = res + A[l:]
    res = res + B[r:]
    return res

alist = [54,26,93,17,77,31,44,55,20]
# data = Insert_sort(alist)
# data = Shell_sort(alist)
# data = Select_sort(alist)
# data = Quick_sort(alist)
data = Merge_sort(alist)
print(data)