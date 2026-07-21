class MyHashSet:

    def __init__(self): 
        self.storage = []
    

    def add(self, key: int) -> None:
        if key not in self.storage:
            self.storage.append(key)

    def remove(self, key: int) -> None:
        if key in self.storage:
            self.storage.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.storage


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)