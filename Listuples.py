#Lists
#Lists

marks = [1,2,3,4,5]
print(marks)
print(type(marks))
#print with index
print("Index 0", marks[0])
print("Index 1", marks[1])
print("Length",len(marks))

#we can store multiple  types of data in  single Lists

student = ["Sarang", 95.4, 18, "Karachi"]

print("List with Different types Value\n", student)
#lists  are  mutable in python not like strings
#we  can access the string by index but cannot change
#we  can change the list by Index

student[0] = "Jazib"
print("List after change of value\n", student)

#slicing is possible in string and list due to both have indexes
#list_name[starting_idx : ending_idx]
marks = [0,1,2,3,4]
print("Slicing", marks[1:4]) #it will print from 1 index to  3 indexes
print("Slicing", marks[:3]) #it will print from 0(start) index to  3 indexes
print("Slicing", marks[3:]) #it will print from 3 index to  4(end) indexes

#negative indexing is also possible
print(marks[-3:-1]) #it will print index 2 and 3 negative index starts from right sidde  of the lists

#List Methods

list = [2,1,3]
list.append(4) #add the passed element 4 in list at the last
print(list.append(4)) #sort method will return None.
print(list)

list.sort()
print(list) #will sort the list in ascending order
list.sort(reverse = True)
print(list) #will sort the list in descending order
#sort method will return None.
print(list.sort())

#sorting also work on strings
list = ["banana","lichi", "apple"]
print(list.sort())
print(list)

#Reverse Method
list = ['a','b','e','c','f','h']
list.reverse() #reverse the complete list
print(list)

#insert method
list = [1,2,3,4]
list.insert(1,50) #insert the value  50  at index 1
print(list)

#Remove method
list.remove(50) #removes the value 50
print(list)

#pop Method
list.pop(0) #remove the index 0 value
print(list)

#TUPLES
#are immutable we can change the value of tuple
tup = (1,1,2,3)
print (tup.index(1)) #returns the inddex of value 1
print(tup.count(1))
