class Stack:
    def __init__(self,max_size):
        self.max_size=max_size
        self.stack=[None]*self.max_size
        self.top=-1
    def Isempty(self):
        if self.top==-1:
            return True
    def Isfull(self):
        if self.top==self.max_size-1:
            return True

    def push(self,data):
        if self.Isfull():
            print('The Stack is Empty !!')
            print('Unable To Push Data !!')
            return 

        else:
            self.top=self.top+1
            self.stack[self.top]=data
            print('Data Pushed !!')
    def pop(self):
        if self.Isempty():
             print('The Stack OverFlows !!')
             print('Unable to Pop the Stack !!')
             return
        else:
            temp=self.stack[self.top]
            self.stack[self.top]=None
            self.top=self.top-1
            print('Data Poped !!')
            return temp
    def display(self):
        return self.stack
        