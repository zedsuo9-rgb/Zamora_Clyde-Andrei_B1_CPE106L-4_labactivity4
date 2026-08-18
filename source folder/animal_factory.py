# animal_factory.py

class Animal:
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

class Bird(Animal):
    def speak(self) -> str:
        return "Tweet!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        animal_type = animal_type.lower()
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        elif animal_type == "bird":
            return Bird()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

if __name__ == "__main__":
    factory = AnimalFactory()
    
    for i in range(1, 4):
        print(f"case {i}:")
        user_input = input("Enter an animal type: ")
        try:
            pet = factory.create_animal(user_input)
            print(f"Case {i}: Created a {pet.__class__.__name__} that says: {pet.speak()}\n")
        except ValueError as e:
            print(f"Case {i}: Error - {e}\n")