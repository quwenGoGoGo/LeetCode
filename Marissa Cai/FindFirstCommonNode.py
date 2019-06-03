'''
题目：
    输入两个链表，找出它们的第一个公共结点
'''
'''
思考：
    注意，这里的公共结点的意思是相同的点，不仅值相同，next也相同，
    那么同理公共结点后面的点也是不仅值相同，而且next也相同，这样的话，就可以把两条链看成Y字形了，
    某一个结点后面的点全部一样，举例：1->2->3->4->6和2->3->5->4->6，4就是他们的第一个公共结点
'''
'''
方法一：
    把全部结点分别压入两个栈，利用栈的特性LIFO，然后同时pop出栈
    一开始两边的元素肯定是相同的，当遇到不同的元素时，肯定已经遇到了最后一个结点，就break
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def append(self, item):
        q = ListNode(item)
        if self.head == None:
            self.head = q
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = q

    def initlist(self, data):
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next


class Solution(object):
    def FindFirstCommonNode(self, pHead1, pHead2):
        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        node1 = None
        while stack1 and stack2 and stack1[-1] is stack2[-1]:
            node1 = stack1.pop()
            stack2.pop()
        return node1


# l1 = LinkList()
# l2 = LinkList()
# l1.initlist([1, 2, 3, 4, 5])
# l2.initlist([1, 2, 3, 7, 8])
# s = Solution()
# print(s.FindFirstCommonNode(l1, l2))