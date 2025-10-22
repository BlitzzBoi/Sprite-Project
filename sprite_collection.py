from my_sprite import my_sprite

class sprite_collection:
    def __init__(self):
        self._sprites = []

    def __getitem__(self, index):
        return self._sprites[index]

    def __setitem__(self, index, value):
        if not isinstance(value, my_sprite):
            raise TypeError("Only my_sprite objects can be added.")
        self._sprites[index] = value

    def __len__(self):
        return len(self._sprites)

    def __repr__(self):
        return "[" + ", ".join(repr(s) for s in self._sprites) + "]"

    def __str__(self):
        return "[" + ", ".join(repr(s) for s in self._sprites) + "]"

    def add(self, sprite):
        if not isinstance(sprite, my_sprite):
            raise TypeError("Only my_sprite objects can be added.")
        self._sprites.append(sprite)

    def get_collection(self):
        return self._sprites

    def search(self, target):
        if not isinstance(target, my_sprite):
            raise TypeError("Can only search for my_sprite objects.")
        result = []
        for s in self._sprites:
            if s == target and all(s is not r for r in result):
                result.append(s)
        return result
