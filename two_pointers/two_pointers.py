class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

if __name__ == '__main__':
    
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4

    head = n1

    if head is None:
        print('Linked list is empty')
    elif head.next is None:
        print('Linked list have only two elements',head.data)
    else:
        slow = fast = n1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print('The middle element is:' ,slow.data)
