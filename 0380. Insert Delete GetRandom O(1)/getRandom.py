from random import *


class RandomizedSet:

    def __init__(self):
        self.bag = set()

    def insert(self, val: int) -> bool:
        if val in self.bag:
            return False
        else:
            self.bag.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.bag:
            self.bag.remove(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        temp = list(self.bag)
        return temp[randint(0, len(temp) - 1)]

# online solution
class RandomizedSet2:

    def __init__(self):
        """ Initialize your data structure here. """
        self.list = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        """ Inserts a value to the set. Returns true if the set did not already contain the specified element. """
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """ Removes a value from the set. Returns true if the set contained the specified element. """
        if val not in self.dic:
            return False
        last, idx = self.list[-1], self.dic[val]
        self.list[idx], self.dic[last] = last, idx
        del self.list[-1]
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        """ Get a random element from the set. """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.remove(0))
    print(obj.remove(0))
    print(obj.insert(0))
    print(obj.getRandom())
    print(obj.remove(0))
    print(obj.insert(0))



