prompt="Enter the topping(enter 'quit' to finish): "
active=True
while active:
    topping=input(prompt)
    if(topping=='quit'):
        break
    else:
        print(f"Added {topping}")