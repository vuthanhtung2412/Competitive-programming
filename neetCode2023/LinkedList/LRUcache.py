import traceback
import sys
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.occ = 0
        # key : [value, prev, next]
        self.d = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.d:
            if key != self.head:
                if key != self.tail:
                    self.d[self.d[key][1]][2] = self.d[key][2]
                else:
                    self.tail = self.d[self.tail][2]
                self.d[self.d[key][2]][1] = self.d[key][1]
                self.d[self.head][2] = key
                self.d[key][1] = self.head
                self.d[key][2] = None
                self.head = key
            return self.d[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key][0] = value
            if key != self.head:
                if key != self.tail:
                    self.d[self.d[key][1]][2] = self.d[key][2]
                else:
                    self.tail = self.d[self.tail][2]
                self.d[self.d[key][2]][1] = self.d[key][1]
                self.d[self.head][2] = key
                self.d[key][1] = self.head
                self.d[key][2] = None
                self.head = key
        else:
            if self.occ == 0:
                self.tail = key
                self.head = key
                self.d[key] = [value, None, None]
                self.occ += 1
            elif self.occ == self.cap:
                self.d[self.head][2] = key
                self.d[key] = [value, self.head, None]
                if self.head == self.tail:
                    self.d[key][1] = None
                self.head = key
                tmp = self.tail
                self.tail = self.d[self.tail][2]
                self.d[self.tail][1] = None
                del self.d[tmp]
            elif self.occ < self.cap:
                self.occ += 1
                self.d[self.head][2] = key
                self.d[key] = [value, self.head, None]
                self.head = key


# Test 1
lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(1, 1)
lRUCache.put(2, 3)
lRUCache.put(4, 1)
lRUCache.get(1)
lRUCache.get(2)

# Test 2
lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)

commands = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put",
            "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get",
            "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put",
            "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put",
            "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put",
            "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put",
            "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put",
            "put", "put", "put", "put", "put", "put"]

values = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
          [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
          [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
          [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
          [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29],
          [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27],
          [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7],
          [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

lRUCache = LRUCache(values[0][0])
p = 0
g = 0
for i in range(len(commands) - 1):
    print(commands[i + 1])
    print(values[i + 1])
    try:
        if commands[i + 1] == "put":
            p += 1
            lRUCache.put(values[i + 1][0], values[i + 1][1])
        else:
            g += 1
            lRUCache.get(values[i + 1][0])
    except Exception as e:
        print(lRUCache.d)
        print(lRUCache.tail)
        print(lRUCache.head)
        print("puts : %s" % p)
        print("gets : %s" % g)
        print(traceback.format_exc())

        break
