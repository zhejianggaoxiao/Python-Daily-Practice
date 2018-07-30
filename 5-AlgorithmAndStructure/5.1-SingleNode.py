"""
-------------------------------------------------
   File Name：     5.1-SingleNode
   Description :
   Author :       gaox
   date：          7/30/18
-------------------------------------------------
   Change Activity:
                   7/30/18:
-------------------------------------------------
"""
__author__ = 'gaox'


class SingleNode:
    """单链表节点"""
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        tmp = SingleNode(item)
        tmp.next = self._head
        self._head = tmp

    def append(self, item):
        # 空链表
        tmp = SingleNode(item)
        if not self._head:
            self._head = tmp
        # 插入最后
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = tmp

    def insert(self, pos, item):
        # 在头部插入
        if pos <= 0:
            self.add(item)
        # 在尾部插入
        elif pos > self.length() - 1:
            self.append(item)
        # 在中间插入
        else:
            tmp = SingleNode(item)
            count = 0
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            tmp.next = pre.next
            pre.next = tmp

    def remove(self, item):
        cur = self._head
        pre = None

        while cur:
            # 找到指定元素
            if cur.item == item:
                # 第一个节点
                if not pre:
                    self._head = cur.next
                # 非第一个节点
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()

