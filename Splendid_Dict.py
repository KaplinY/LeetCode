class Splendid_Dictionary:
    def __init__(self, size):
        self.size = size
        self.dict = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size #get index in the array where key-value pair is stored
    
    def set(self, key, value):
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
  
splendid_dict = Splendid_Dictionary(5)
splendid_dict.set(0,"x")
splendid_dict.set(1,"a")
splendid_dict.set(2,"b")
splendid_dict.set(3,"c")
splendid_dict.set(4,"d")
splendid_dict.set(1,"e")
splendid_dict.set(1,"f")
splendid_dict.display()
print('------')
splendid_dict.remove(3)
splendid_dict.display()

