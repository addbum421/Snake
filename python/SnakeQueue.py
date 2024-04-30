from CircularQueue import CircularQueue

class SnakeQueue(CircularQueue):
    def __init__(self, capacity, limit=4):
        super().__init__(capacity)
        self.limit = limit
    
    def enqueue(self, elem):
        if self.size == self.limit:
            e = super().dequeue(); 
            super().enqueue(elem)
            return e
        else: super().enqueue(elem)

    def increaseLimit(self, ex=1):
        self.limit += ex

    def dequeue(self):
        return super().dequeue()
    
    def display(self):
        super().display()

    def isIn(self, elem):
        p = self.front
        for i in range(self.size):
            if (self.array[p] == elem): return True
            p = (p + 1) % self.capacity
        else: return False

if __name__ == "__main__":
    S = SnakeQueue(10)
    S.enqueue((1,0)); S.enqueue((1,1)); S.display() 
    S.enqueue((1,0)); S.enqueue((1,2)); S.display() 
    S.enqueue((2,1)); S.enqueue((1,1)); S.display() 
    S.increaseLimit(); S.enqueue((3,3)); S.display()



