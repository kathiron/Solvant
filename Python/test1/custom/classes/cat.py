from .animals import Animal

class Cat(Animal):
    def soundslike(self):
        self.mysound = 'Meow'
        super().soundslike()
        # print(f"{self.name} {f"the {self.breed} " if self.breed else "" }says: Meow!")