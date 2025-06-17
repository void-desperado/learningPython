myAlien={'color':'green','points':5}
print(myAlien)
print(myAlien['color'])
print(myAlien['points'])

myAlien['xCoordinates']=0
myAlien['yCoordinayes']=0
print(myAlien)

myAlien['xCoordinates']=25
print(myAlien)

myAlien['speed']='slow'
if (myAlien['speed']=='slow'):
    xIncrement=2
elif (myAlien['speed']=='medium'):
    xIncrement=3
elif (myAlien['speed']=='fast'):
    xIncrement=5

myAlien['xCoordinates'] += xIncrement
print(myAlien)

del myAlien['xCoordinates']
del myAlien['yCoordinayes']
print(myAlien)