prompt="Enter your age(enter 'quit' to exit): "
active=True
while active:
    age=input(prompt)
    if(age=='quit'):
        break
    elif(int(age)<3):
        print('free')
    elif(int(age)>=3 and int(age)<12):
        print('10')
    elif(int(age)>=12):
        print('15')