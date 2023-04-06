# HashMap Creating Class
# Referenced the "Let's Go Hashing" video/PDF in the supplemental resources

class HashMap:
    # Make a bunch of lists (buckets) so that we can avoid collisions
    def __init__(self, objects = 40):
        self.table = []
        for i in range(objects):
            self.table.append([])

    def __str__(self):
        return str(f"{self.table}")

    # Inserting items
    def insert(self, key, item):
        hash_value = hash(key) % len(self.table)
        #print(f"Key: {key}, Insert Value: {hash_value}")
        bucket_items = self.table[hash_value]

        # If exists, update
        for pair in bucket_items:
            if pair[0] == key:
                pair[1] = item
                return True

        # If not, add
        bucket_items.append([key, item])

    # Returning Package Object
    def lookup(self, id):
        hash_value = hash(id) % len(self.table)
        #print(f"Lookup Value: {hash_value}")
        bucket_items = self.table[hash_value]
        #print(bucket_items)

        for kv in bucket_items:
            #print(f"KV: {kv}")
            if kv[0] == id:
                #print(f"Table: {bucket_items}")
                #print(f"Package: {kv[1]}")
                return kv[1]
        else:
            return f"Lookup term {id} not found"

    # Removing items
    def remove(self, key):
        hash_value = hash(key) % len(self.table)
        bucket_items = self.table[hash_value]

        for kv in bucket_items:
            if kv[0] == key:
                bucket_items.remove([kv[0], kv[1]])
        else:
            return f"Lookup term {key} not found"
