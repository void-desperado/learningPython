def describePet(petName,animalType="dog"):
    print(f"It is a {animalType} with name {petName.title()}.")

describePet('willie')
describePet(pet_name='willie')

describePet('harry', 'hamster')
describePet(pet_name='harry', animal_type='hamster')
describePet(animal_type='hamster', pet_name='harry')