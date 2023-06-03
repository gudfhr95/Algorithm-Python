class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        for e in self.hashset:
            if e == key:
                return

        self.hashset.append(key)

    def remove(self, key: int) -> None:
        if (self.contains(key)):
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        for e in self.hashset:
            if e == key:
                return True

        return False
