my_list = ['ameya','orange','fruits','cherry','watermelon']
print(my_list)
# list items are indexed and you can access them using index number 
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) 
print(thislist[-1])
# range of indexed 
# you can specify a range of indexes by specifying where to start and where to end the range 
# when specifying a range the return value will be new lsit with the specified items 
# range in the list 
this_list = ["apple","banana","cherry","berry","strawberry","kiwi","avocado"]
print(this_list[2:6])
# check if item exists in the list 
this_list = ["apple","banana","cherry"]
if "apple" in thislist:
    print("yes,'apple' is in the fruits list")

# to determine how many item list has use the len())
this_list = ["apple","orange","cherry"]
print(len(this_list))    
# list type 
list1 = ["abc",34,True,20,"male"]
print(list1)
type(list1)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])# this item give the cherry and till end 
print(thislist[-4:-1])

# check if item exists 
thislist = ["apple","banana","cherry"]
if "apple" in thislist:
    print("yes,'apple' is in the fruits list")
# change the values "banana" and "cherry" with tthe values "blackcurrent" and "watermelon" 
thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrent","watermelon"]
print(thislist) 

# change the second value by replacing it with 2 values 
thislist = ["apple","banana","cherry"]
thislist[1:2] = ["blackcurrent","watermelon"]
print(thislist)

# change the second and third value by replacing it with one value 
thislist = ["apple","banana","cherry"]
thislist[1:3] = ["watermelomn"]
print(thislist)

# insert items into tthe list 
# insert()
thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

# append method 
# using the appendmethod to append the item 
l1 = ["book", "phone","cellphone","marker","stainless ste"]
l1.append("apple")
print(l1)
# loop through alist 
stationary = ["apple", "banana","cherry"]
for x in stationary:
    print(x)
    print(type(x))

# loop through the index     
stationary = ["apple","banana","cherry"]
for i in range(len(stationary)):
    print(stationary[i])
# list comprehensions
# python list comprehension prvides a much more short syntax for creating a newlist from the exisiting list 
#newlist = [expression(element)for element in oldlist if condition is true ]
#
       
l = [5,4,100,1.1,'a',2,'','1.5','1','.']

for row in l:
    print(row)
if l is not str:
    print(" it is not string")
    print(l)


    
l3 = {1,1,2,6,7,7.5,7,7.5,6.5,6.5}
l4=[4,3,4.5]
l3.append(l4)

            
#