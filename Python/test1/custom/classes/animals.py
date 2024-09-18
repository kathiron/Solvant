from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, breed = None, mysound = None):
        self.name = name
        self.breed = breed
        self.mysound = mysound

    @abstractmethod
    def soundslike(self):
        print(f"{self.name} {f"the {self.breed} " if self.breed else "" }says: {self.mysound}!")