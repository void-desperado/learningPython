def formatName(firstName,lastName,middleName=None):
    if middleName:
        return f"{firstName.title()} {middleName.title()} {lastName.title()}"
    return f"{firstName.title()} {lastName.title()}"

print(formatName('satvik','miglani'))