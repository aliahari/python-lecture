myList = [1, 2, 3, 4, 1]
print(myList)
# myList.remove(1)
# print(myList)
mySet = set(myList)
print(mySet)
smallSet = set([1,2])
print (mySet.issubset(smallSet))
user = input("Please enter the name:")
phoneNuber = myDict.get(user, "is not in my contact list")