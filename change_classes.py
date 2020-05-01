class Pet:
    kind = "mammal"
    n_pets = 0  # number of pets
    pet_names = []  # list of names of all pets

    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4
# erzeugt 3 Instanzen der Klasse Pet
tom = Pet("cat", "Tom")
avocado = Pet("dog", "Avocado")
ben = Pet("goldfish", "Benjamin")
print('Pet', Pet.n_pets)
print('Tom: ', tom.n_pets)
print('avocado', avocado.n_pets)
print('ben', ben.n_pets)
# für das Klassen Attribut n_pets werden 3 hinzugefügt
Pet.n_pets += 3
print('Pet', Pet.n_pets)
print('Tom: ', tom.n_pets)
print('avocado', avocado.n_pets)
print('ben', ben.n_pets)

