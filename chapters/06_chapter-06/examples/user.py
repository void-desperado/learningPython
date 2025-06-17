user0={
    'username':'efermi',
    'firstName':'enrice',
    'lastName':'fermi'
}

for key in user0.keys():
    print(key,"\n")

for value in user0.values():
    print(value,"\n")

for key,value in user0.items():
    print(f"key: {key}")
    print(f"value: {value}\n")