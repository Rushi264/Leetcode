import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val):
        if val in self.dict:
            # Move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # Delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self):
        return random.choice(self.list)
