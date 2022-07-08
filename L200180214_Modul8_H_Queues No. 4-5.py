from queue import PriorityQueue

"""-----Queues------"""

class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self.qlist)
        
    def enqueue(self,data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)
    

#4.1.A
    def getFrontmost(self):
        return self.qlist[0]

#4.1.B
    def getRearmost(self):
        return self.qlist[-1]
    

class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
        self.item = None
        self.priority = None

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self,data,priority):
        entry = PriorityQEntry(data,priority)
        self.qlist.append(entry)
    
#4.2.A
    def getFrontmost(self):
        return self.qlist[0]

#4.2.B
    def getRearmost(self):
        return self.qlist[-1]

#5
    def dequeue(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)

class PriorityQEntry(object):
    def __init__(self,data,priority):
        self.item = data
        self.priority = priority


C = PriorityQueue()
C.enqueue('andi',3)
C.enqueue('nur',1)
C.enqueue('fitri',6)
C.dequeue()
C.getFrontmost()
C.getRearmost()
    



