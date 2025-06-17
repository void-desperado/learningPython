def buildPerson(firstName,lastName):
    return {
        'First name':firstName.title(),
        'Last name':lastName.title()
              }
    
print(buildPerson("satvik","miglani"))