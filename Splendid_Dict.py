class Splendid_Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity #get index in the array where key-value pair is stored
    
    def set(self, key, value):
        index = self._hash(key)
        self.dict[index] = (key, value)
    
    def __setitem__(self,key,value):
        index = self._hash(key)
        self.dict[index] = (key, value)
    
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
        return self.capacity
    
    def display(self):
        len = self.__len__()
        for i in range(len):
            print(self.dict[i])
  
splendid_dict = Splendid_Dictionary(5)
splendid_dict[0] = "audi"
splendid_dict[1] = "mercedes"
splendid_dict[2] = "bmw"
splendid_dict[3] = "lada"
splendid_dict[4] = "porsche"
splendid_dict.display()
splendid_dict[1] = "toyota"
splendid_dict[4] = "jeep"
print("-------------------")
splendid_dict.display()



