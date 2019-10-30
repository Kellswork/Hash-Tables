# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # takes a key and value
        # save the value in the array
        # run hash function with key
        # save the value that is returned by the hash in the storage
        # check if the key is already available before hashing
        #
        index = self._hash_mod(key)

        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
        else:
            old_key = self.storage[index]
            while old_key and old_key.key != key:
                prev, old_key = old_key, old_key.next

            if old_key:
                old_key.value = value

            else:
                prev.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # set the value at the index to null
        # hash key to get the index
        # lookup index on storage
        # set it to null
        hashed_key = self._hash_mod(key)

        old_key = self.storage[hashed_key]
        prev_node = old_key
        if (old_key is not None):
            if (old_key.key == key):
                self.storage[hashed_key] = old_key.next
                return
            while old_key and old_key.key != key:
                prev_node = old_key
                old_key = old_key.next

            if old_key:
                prev_node.next = old_key.next
        else:
            print('could not find key')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # retrieve value for the array
        # to get value, we run the hash function on the key to get the address in the array
        # retrieve the value using the index returned by the hash function

        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key]:
            old_key = self.storage[hashed_key]
            while old_key.key != key:
                old_key = old_key.next
            return old_key.value
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_storage = [None] * (self.capacity * 2)

        for i in range(len(self.storage)):
            new_storage[i] = self.storage[i]

        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
