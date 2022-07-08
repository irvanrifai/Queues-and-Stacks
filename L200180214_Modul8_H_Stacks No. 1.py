
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self)==0

    def isFull(self):
        return len(self)!=0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()

    def push(self, data):
        self.items.append(data)

def cetakBiner(d):
    f = Stack()
    if d==0 : f.push(0);
    while d != 0:
        sisa = d%2
        d = d//2
        f.push(sisa)
    st = ""
    for i in range(len(f)):
        st = st + str(f.pop())
    return st

"""-----Stacks------"""

#1
def cetakHexa(n): 
    hexaDeciNum = ['0'] * 100; 
    i = 0; 
    while(n != 0):
        temp = 0  
        temp = n % 16
        if (temp < 10):
            hexaDeciNum[i] = chr(temp+48)
            i=i+1
        else:
            hexaDeciNum[i] = chr(temp+55)
            i=i+1
        n = int(n/16)
    j = i - 1; 
    while (j >= 0):
        print ((hexaDeciNum[j]))
        j = j-1

def cetakOcta(x):
    octalNum = [0] * 100; 
    i = 0; 
    while (x != 0): 
        octalNum[i] = x % 8; 
        x = int(x / 8); 
        i += 1;  
    for j in range(i - 1, -1, -1): 
        print(octalNum[j]); 
