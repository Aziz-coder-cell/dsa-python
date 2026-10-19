class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

if __name__ == '__main__':
    
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4= Node(40)

    head = n1

    n1.next = n2
    n2.next = n3
    n3.next = n4

    prev = None
    current = n1

    node_data = []
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    
    while prev:
        node_data.append(str(prev.data))
        prev = prev.next
        
    print('-->'.join(node_data))
    