class Queue:
    def __init__(self):
        self.queue_list =[]

    def enqueue(self,data = None):
        self.queue_list.append(data)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            return f"Element dequeued is: {self.queue_list.pop(0)}"

    def peek(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            return f"Element at start of queue is: {self.queue_list[0]}"
    
    def is_empty(self):
        if not self.queue_list:
            return True

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    print(queue.dequeue())
    print(queue.peek())