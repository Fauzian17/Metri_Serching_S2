class HasTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key , data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                                self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
    def hashfunction(self,key,size):
        return key%size
    def rehash(self, oldhash,size):
        return (oldhash+1)%size
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                            not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True

        return data
    def __getitem__(self,key):
        return self.get(key)
    def __setitem__(self, key , data):
        self.put(key,data)

h = HasTable()
h[54]='cat'
h[26]='dog'
h[93]='lion'
h[17]='tiger'
h[77]='bird'
h[31]='cow'
h[44]='goat'
h[55]='pig'
h[20]='chiken'
print(h.slots)
print(h.data)
print(h[17])
h[20]='duck'
print(h[20])
print(h[99])