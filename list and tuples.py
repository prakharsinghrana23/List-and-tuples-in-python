#LIST 
friends=["Apple","Banana","Aakash","Palak","Ojit",5,345.06,False]

print(friends[0])
friends[0]="Grapes"
print(friends[0])
print(friends[1:4])
friends.append("Prakhar") # append means add
print(friends)

l1=[1,34,56,89,2,6,8,10,78]
l1.sort() # use for sorting the list like in ascending order
print(l1)
l1.reverse()# use for reversing aur backward
print(l1)
l1.insert(3,34456) # use for inserting anything in between the list (first enter the index where to  insert, then insert what to insert )
print(l1)
value=l1.pop(3)
print(value)
print(l1)
l1.remove(34)
print(l1)

# TUPPLE
a=(1,45,32,67,False,"Rohan","Prakhar","Palak") # Tupple can not be changed 
print(a)
print(type(a))
number=a.count(45) #use for the counting of number repeated in tupple 
print(number)

i=a.index(45)
print(i)

i2=a.index(67)
print(i2)

print(len(a)) # for more functions check Chat GPT  