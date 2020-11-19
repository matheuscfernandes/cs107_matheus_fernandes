class Animal:

    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    def __init__(self, name, species):
        self.name = name
        self._species = species

    def __repr__(self):
        return f'{self.name} ({self._species})'
    
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, into):
        assert into in Animal.valid_species, Exception(f'invalid species: {into}')
        self._species = into    

if __name__ == "__main__":
    #EXISTING CLIENT CODE
    def transform(animal, into):
        animal.species = into
        return animal

    #TESTING ORIGINAL
    dog = Animal('Fido', 'dog')
    print(vars(dog))
    print(dog.species)

    #TESTING CHANGING TO VALID VERSION
    dog = transform(dog, 'cat')
    print(vars(dog))
    print(dog.species)

    # #TESTING CHANGING USING . VERSION
    dog.species = 'elf'
    print(vars(dog))
    print(dog.species)

    # #TESTING CHANGING TO INVALID VERSION
    dog.species = 'TheThing'
    print(vars(dog))
    print(dog.species)

