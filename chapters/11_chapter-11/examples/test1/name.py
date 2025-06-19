def formattedName(first,last):
    return f"{first.title()} {last.title()}"

print("Type 'q' at any time to exit")
while True:
    firstName=input("Enter the first name: ")
    if(firstName=='q'):
        break

    lastName=input("Enter the last name: ")
    if(lastName=='q'):
        break

    name=formattedName(firstName,lastName)
    print(f"Formatted Name: {name}")

