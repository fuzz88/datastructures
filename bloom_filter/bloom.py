from hashlib import sha256


class Bloom(object):
    def __init__(self, size, hash_count):
        self.size = size
        self.bit_array = [0] * size
        self.hash_count = hash_count

    def hash_generate(self, value):
        hashes = []
        digest = int(sha256(value.encode('utf-8')).hexdigest(), 16)
        for i in range(self.hash_count):
            hashes.append(digest / (i + 1) % 2147483657 % self.size)
        return hashes

    def insert(self, value):
        hashes = self.hash_generate(value)
        for _hash in hashes:
            self.bit_array[int(_hash)] = 1

    def find(self, value):
        hashes = self.hash_generate(value)
        for _hash in hashes:
            if self.bit_array[int(_hash)] == 0:
                return False
        return True
