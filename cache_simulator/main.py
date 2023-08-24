class CacheLine:
    def __init__(self):
        self.valid = False
        self.tag = None
        self.data = None
        


class DirectMappedCache:
    def __init__(self, size):
        self.cache = [CacheLine() for _ in range(size)] # Create  a list of CacheLine objects
        self.hits = 0
        self.misses = 0
        
    def get_index_and_tag(self, address):
    # Assuming a 16-bit address and 7 bits for the index
        index_bits = 7
        mask = (1 << index_bits) - 1  # Create a mask with 7 bits set to 1
        index = address & mask  # Bitwise AND to get the last 7 bits for index
        tag = address >> index_bits  # Shift right to get the tag
        return index, tag
    
    def access(self, address):
        index, tag = self.get_index_and_tag(address)
        if self.cache[index].valid and self.cache[index].tag == tag:
            self.hits += 1
            print(f"Cache hit!")
            return self.cache[index].data
        else:
            self.misses += 1
            print(f"Cache miss!")
            # Here we simulate fetching data from memory. For simplicity, let's say data = address.
            data = address//5
            self.cache[index].valid = True
            self.cache[index].tag = tag
            self.cache[index].data = data
            for i in range (1,6):
                other_index, other_tag = self.get_index_and_tag(address+i)
                self.cache[other_index].valid = True
                self.cache[other_index].tag = other_tag
                self.cache[other_index].data = (address+i)//5
            for i in range (1,6):
                if address-i >= 0:
                    other_index, other_tag = self.get_index_and_tag(address-i)
                    self.cache[other_index].valid = True
                    self.cache[other_index].tag = other_tag
                    self.cache[other_index].data = (address-i)//5
            return data

    def hit_rate(self):
        return self.hits / (self.hits + self.misses)

# Create a cache of size 128
cache = DirectMappedCache(128)

# Simulate some accesses
for addr in range (0,129):
    print(f"Accessing address {addr}, data: {cache.access(addr)}","")

print(f"Hit rate: {cache.hit_rate() * 100:.2f}%")
