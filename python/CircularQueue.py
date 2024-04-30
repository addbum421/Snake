class CircularQueue:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def isEmpty(self): return self.size == 0

    def isFull(self): return self.size == self.capacity

    def enqueue(self, elem):
        if not(self.isFull()):
            self.array[self.rear] = elem
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1
        else: print("OverFlow")
    
    def dequeue(self):
        if not(self.isEmpty()):
            e = self.array[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return e
        else: print("UnderFlow")

    def display(self):
        c = self.front
        for i in range(self.size):
            print(self.array[c], end="-")
            c = (c + 1) % self.capacity
        print("\b ")
    
if __name__ == "__main__":
    Q = CircularQueue(10)
    Q.enqueue("A"); Q.enqueue("B"); Q.display()
    Q.enqueue("C"); Q.enqueue("E"); Q.display()
    Q.enqueue("1"); Q.enqueue("2"); Q.display()
    Q.enqueue("3"); Q.enqueue("4"); Q.display()
    Q.enqueue("5"); Q.enqueue("6"); Q.display()
    Q.enqueue("F")
    Q.dequeue(); Q.dequeue(); Q.display()
    Q.dequeue(); Q.dequeue(); Q.display()
    Q.dequeue(); Q.dequeue(); Q.display()
    Q.dequeue(); Q.dequeue(); Q.display()
    Q.dequeue(); Q.dequeue(); Q.display()
    Q.dequeue(); Q.dequeue(); Q.display()
    
