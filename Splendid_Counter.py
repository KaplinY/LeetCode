class Splendid_Counter():
    def __init__(self, size):
        self.size = size
        self.val = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= self.size:
            x = self.val
            self.val += 1
            return "this beautiful number is", x
        else:
            raise StopIteration
    
counter = Splendid_Counter(10)
for i in counter:
    print(i)