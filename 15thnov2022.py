# def countX(lst,x):
#     count = 0 
#     for ele in lst:
#         if (ele == x):
#             count = count + 1
#     return count    # calling the function      
lis = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']
occurrence = {item :lis.count(item) for item in lis}
print(occurrence)


# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
# h1 = Human("sherlock", 6 )
# # adding to numbers 

# n1 =int( input("enter the number"))#it will return the string values
# n2 =int( input("enter the number"))
# n1 + n2 # adding to values 
# result = n1 + n2 
# print(result) 



# import os 


# Development = "development"
# Production = "production"
# Staging = "staging"
# code_space = "code space"
# local = "local"

# current_env = os.environ.get("env_name",Development)

# if current_env == Development:
#     print("developemnt environment")
# elif current_env == Production:
#     print("production ")    

names = ["john","paul","george","ringo"]

ages = [20,21,22,23]

john = names[0]
paul = names[1]

john_paul = names[:2]
george_ringo = names[2:]
reverse= names[::-1]
every_other = names[::2]

print(sum(ages))
print(min(ages))
print(max(ages))
print(john_paul)
print(george_ringo)
print(reverse)

# scope and indentations 
# code  block  or unit of code block is executed 
# if true:
# print("this is caode block ")
# print("this is the same code block")

# else:
# print("this is a new code block ")
# print("this is the same code block")

# def my_function():
#     greet = "hello"
#     return greet
# print(my_function()) 
# print(my_function())   

# greet = "helllo world"

# extend_grt = "hello world" + "this is long string "

# name = "john "
# intruption = f"hello {name}" 

# greet_format = "hello{}"

# formatted = greet_format,format(name)

# print(intruption, formatted )

# print(formatted .upper())
# print(formatted.lower())
# print(formatted.replace("john", "paul"))

# names = ["john", "paul", "jacob", "vishal"]

# ages = [20,21,23,24,25,26]

# john = names[0]
# paul = names[1]

# import random 

# n = random .randrange(1,10)
# guess = int(input("enter any number"))
# while n!= guess:
#     if guess < n : 
#         print("too low")
#         guess = int(input("enter number again")) 
#     elif guess > n :
#         print("too high")
#         guess = int(input("enter number again"))
#     else: 
#         break
# print("you guessed it right")           


# import random 

# n = random.randrange(1,10)
# guess = int(input("enter any number"))

# while n != guess:
#     if guess < n :
#         print( " too low ")
#     elif guess >n:
#         print("too high")
#         guess = int(input("enter number again"))
#     else:
#         break
# print("you guessed it right ")       
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)