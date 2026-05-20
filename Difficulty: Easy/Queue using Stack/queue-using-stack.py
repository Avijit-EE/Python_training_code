class myQueue:

    def __init__(self):
        # Initialize your data members
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        # Implement the enqueue operation
        self.s1.append(x)
        
    def dequeue(self):
        # Implement the dequeue operation
        if not self.s1 and not self.s2:
            return 
        if not self.s2:
            while self.s1:self.s2.append(self.s1.pop())
        self.s2.pop()    
       

    def front(self):
        # Return the front element of the queue
        if self.s2:
            return self.s2[-1]
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        return -1    


    def size(self):
        # Return the current size of the queue
        return len(self.s1) + len(self.s2)