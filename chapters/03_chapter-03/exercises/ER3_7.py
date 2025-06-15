guests=["Newton","Oppenheimer","Einstein"]
print(f"Invite {guests[0]}")
print(f"Invite {guests[1]}")
print(f"Invite {guests[2]}")

print(f"{guests[1]} can't make it")
guests[1]="Linus"
print(f"Invite {guests[0]}")
print(f"Invite {guests[1]}")
print(f"Invite {guests[2]}")

print("Found a bigger table")

guests.insert(0,"Dennis")
guests.insert(2,"Brian")
guests.append("Python")

print(f"Invite {guests[0]}")
print(f"Invite {guests[1]}")
print(f"Invite {guests[2]}")
print(f"Invite {guests[3]}")
print(f"Invite {guests[4]}")
print(f"Invite {guests[5]}")

print("Can invite only two people")

guests.pop()
guests.pop()
guests.pop()
guests.pop()

print(f"Invite {guests[0]}")
print(f"Invite {guests[1]}")

del guests[1]
del guests[0]

print(guests)