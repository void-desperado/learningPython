responses = {}

polling_active = True
while polling_active:

    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response
    repeat = input("Would another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")