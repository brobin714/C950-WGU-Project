# Brandon Robinson
# ChainingHashTable.py
# C950 Assessment
#
# Hash Table class to store package data
#
# Important caveat
# SOURCE CODE CITATION: C950 - Webinar-1 - Let's Go Hashing: W-1_ChainingHashTable_zyBooks_Key-Value.py
#
# Obective A:
#   Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the following components as input and inserts the components into the hash table:
#
#       package ID number
#       delivery address
#       delivery deadline
#       delivery city
#       delivery zip code
#       package weight
#       delivery status (e.g., delivered, en route)

class ChainingHashTable:
    # constructor
    # includes optional initial capacity parameter
    # assigns all buckets with an empty list
    # O(N) linear
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    # O(1) constant average
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # O(1) constant average
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    # O(1) constant average
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])