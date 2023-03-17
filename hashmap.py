# Hash Map
# Large credit goes to the outline shown in https://www.youtube.com/watch?v=9HFbhPscPU0
class HashMap:
    def __init__(self):
        self.size = 64
        self.map = [None] * self.size

    # Iterates over characters in the key value and hashes based on the order
    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    # Adds a key-value pair to the hash table after hashing the key
    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Returns a given hash table item based upon the given key (ID)
    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Removes a key value pair from the hash table
    def delete(self, key):
        key_hash = self.get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    # Prints a string version of the hash table
    def print(self):
        print("----Hashmap----")
        for item in self.map:
            if item is not None:
                print(str(item))



