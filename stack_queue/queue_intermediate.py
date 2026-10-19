class QueueFromStack:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self,data = None):
        self.stack_in.append(data)

    def _transfer(self):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

    def dequeue(self):
        self._transfer()
        if self.stack_out:
            return self.stack_out.pop()
        
queue = QueueFromStack()
queue.enqueue(38)
queue.enqueue(23)
queue.enqueue(12)
queue._transfer()
print(queue.dequeue())
print(queue.dequeue())