class Customer:
    def __init__(self, name, age, city, id = 0):
        self.id = id
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Customer(id={self.id}, name='{self.name}', age={self.age}, city='{self.city}')"

    def to_dict(self):
        return self.to_json()
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "city": self.city
        }
