from .animals import Animal

class Dog(Animal):
    def soundslike(self):
        self.mysound = 'Woof'
        super().soundslike()
        # print(f"{self.name} {f"the {self.breed} " if self.breed else "" }says: Woof!")