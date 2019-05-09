class Stack():
    def __init__(self,sample):
        print("New Stack object")
        self.stack=[]
        self.sample=sample
        print("New stack object")


    def pop(self):
        print("Popping...")
        return self.stack.pop()

    def push(self, value):
        if not isinstance(value,type(self,sample)):
            raise ValueError('Expected integer but got()'.format(type(value)))
        else:
            self.stack.append(value)
            print("pushing...")


class IntStack(Stack):
    def__init__(self,0):
    Stack.__init__(self,0)
