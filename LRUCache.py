# LRU  cache implementation
import collections

class LRUCache:
    
    def __init__(self, capacity):
        self.capacity=capacity
        self.cache=collections.OrderedDict()

    def get(self, key):
        if self.cache.get(key)!=None:
            temp=self.cache[key]
            self.cache.move_to_end(key)
            return temp 
        else:

            return -1

    def put(self, key, value):
        if key not in self.cache :
            if len(self.cache)<self.capacity:
               self.cache[key]=value 
        
            else: 
                self.cache.popitem(last=False)
                self.cache[key]=value   
        else:
           del self.cache[key]
           self.cache[key]=value
     
            

c=LRUCache(2)
print(c.get(2))
print(c.put(2,6))
print(c.get(1))
print(c.put(1,5))
print(c.put(1,2))
print(c.get(1))
print(c.get(2))



