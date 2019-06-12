### File: queue_alt.py
class QueueAlt:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            raise Exception("Cannot dequeue from an empty queue")
        return self.items.pop(0)
    
    def peek(self):
        if len(self.items) == 0:
            raise Exception("Queue is empty")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        resultStr = "(front)"
        for item in self.items:
            resultStr = resultStr + " " + str(item)
        resultStr = resultStr + " (rear)"
        return resultStr
    
        
