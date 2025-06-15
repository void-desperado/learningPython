myList=["pizza","coffee","burger"]
myList2=myList[:]

myList.append("chai")
myList2.append("cake")

[print(i) for i in myList]
[print(i) for i in myList2]