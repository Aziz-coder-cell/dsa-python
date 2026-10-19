#Basic and Intermediate
"""class stack:
    def __init__(self):
        self.list_stack = []

    def push(self,data=None):
        self.list_stack.append(data)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            x = self.list_stack.pop()
            print('Object popped is:',x)

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            print(self.list_stack[-1])

    def is_empty(self):
        if not self.list_stack:
            return True

    def traverse(self):
        print(self.list_stack)


if __name__ == '__main__':
    stack_obj = stack()
    stack_obj.push(10)
    stack_obj.pop()
    stack_obj.pop()
    stack_obj.peek()"""

#Advance
class stack:
    def __init__(self):
        self.bracket = []

    def push(self,data = None):
        self.bracket.append(data)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.bracket.pop()

    def is_empty(self):
        if not self.bracket:
            return True
    
    def check(self,str):
        if str:
            for i in str[:]:
                if i in '({[':
                    self.push(i)
                elif i == ')':
                    if self.pop() == '(':
                        continue
                    else: 
                        return False
                elif i == '}':
                    if self.pop() == '{':
                        continue
                    else:
                        return False
                else:
                    if self.pop() == '[':
                        continue
                    else:
                        return False
        if self.is_empty():
            return True
        else: 
            return False

if __name__ == '__main__':
    obj = stack()
    result = obj.check('({[]})')
    print(result)