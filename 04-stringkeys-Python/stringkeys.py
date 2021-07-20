"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

from attr import has


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        # hashvalue = self.calculate_hash_value(string)
        # if self.table[hashvalue] != None:
        #     print("hi")
        #     self.table[hashvalue] = (string)
        #     print(self.table)
        # else:
        #     self.table[hashvalue] = [string]
        # # print(hashvalue)
        # return hashvalue
        hashvalue = self.calculate_hash_value(string)
        self.table.insert(hashvalue, string)
        return -1

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        # hashvalue = self.calculate_hash_value(string)
        # print(hashvalue)
        # print(self.table)
        # print(hash)
        # print(self.table[hashvalue])
        # print(string)
        # if string in self.table[hashvalue]:
        #     return hashvalue
        # return -1
        hash = self.calculate_hash_value(string)
        if(self.table[hash] == None or self.table[hash]!=string):
            return -1
        else:
            return hash

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        # hashvalue = ord(string[0])*100 + ord(string[1])
        # # print(hashvalue)
        # return hashvalue
        Hashvalue = (ord(string[0])*100)+ ord(string[1])
        return Hashvalue

# print(HashTable('UDACITY'))

