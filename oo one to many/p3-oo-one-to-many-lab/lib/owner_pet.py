class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all_pets = []

    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        Pet.all_pets.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self  # Assign owner attribute to the pet
            self.pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets, key=lambda x: x.name)
