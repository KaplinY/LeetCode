class Splendid_Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dict = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity #get index in the array where key-value pair is stored
    
    def set(self, key, value):
        if self.size == self.capacity:
            return ("max capacity has been achieved")
        self.size += 1
        index = self._hash(key)
        self.dict[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        temp = []
        for k, v in self.dict[index]:
            if k == key:
                temp.append(v)
        if temp: return temp
        else: return "oshibochka"
    
    def remove(self, key):
        index = self._hash(key)
        removed_item = self.dict.pop(index)
        self.size -=1
        return removed_item

    def __len__(self):
        return self.size
    
    def display(self):
        len = self.__len__()
        for i in range(len):
            print(self.dict[i])
  
splendid_dict = Splendid_Dictionary(10)
splendid_dict.set(1,"boris")
splendid_dict.set(2,"the")
splendid_dict.set(3,"blade")
splendid_dict.set(4,"bullet")
splendid_dict.set(1,"dogger")
splendid_dict.set(2,"snatch")
splendid_dict.set(3,"thames")
splendid_dict.display()
print('------')
splendid_dict.remove(3)
splendid_dict.display()

