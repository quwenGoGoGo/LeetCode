class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = 0

    def initList(self,data):
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

class Solution:
    def printListFromTailToHead(self,listNode):
        l = []
        head = listNode
        while head:
            l.insert(0,head.val)
            head = head.next
        return l

if __name__ == '__main__':
    listNode = LinkList()
    listNode.initList(range(0,20))
    l = Solution().printListFromTailToHead(listNode.head)

    # 也可以这样
    # head = ListNode(0)
    # p = head
    # for i in [1,2,3,4]:
    #     newNode = ListNode(i)
    #     p.next = newNode
    #     p = p.next
    # print(head)

    # 用range不行，待后续找出原因
    # for i in range(1,20):
    #     newNode = ListNode(i)
    #     p.next = newNode
    #     p = p.next

    print(l)

