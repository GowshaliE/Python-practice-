# n = int(input("enter the number"))
# if(n %2)!= 0 :
#     print("it is Weird")
#     if(n %2)==0  and n>2 and n<=5:
#        print("It is not weird") 
#     if(n %2)==0  and n>6 and n <=20:
#             print("It is weird")  
#     elif(n %2 )==0 and n >20:
#                 print("it is not weird")     

# n = int(input("enter the number"))
# if(n %2)!= 0 :
#     print("Weird")
# if(n %2)==0  and n>2 and n<=5:
#     print("not weird") 
# elif(n %2)==0  and n>6 and n <=20:
#      print("weird")  
# elif(n %2 )==0 and n >20:
#     print("not weird")     

# n = int(input("enter the number"))
# if(n %2)!= 0 :
#     print("Weird")
#     if(n %2)==0  and n>2 and n<=5:
#        print("It is not weird")
# elif(n %2)==0  and n>6 and n <=20:
#             print("It is weird")
# elif(n %2 )==0 and n >20:
#         print("it is not weird")

# n = int(input("enter the number"))
# if(n %2)!= 0 :
#     print("it is Weird")
#     if(n %2)==0  and n>2 and n<=5:
#         print("It is not weird")
#     elif(n %2)==0  and n>6 and n <=20:
#         print("It is weird")
#     elif(n %2 )==0 and n >20:
#         print("it is not weird") 
# write a function to get grade based percentage input
# 1. Get only grade A (91-100) and grade D (60-70)
# # 2. Remaining below 60 print fail and above 70 print pass
# def get_grade():
#     marks = int(input("enter the mark"))
#     if marks >90 and marks <=100:
#         print("your grade is A")
#     elif marks > 60 and marks <=70:
#         print("your grade is D")
#     elif marks <60:
#         print("your grade is fail")
#     elif marks >70:
#         print("your grade is pass")  
#     return marks            
# get_grade()   

# Write a function to get duration between to dates based on post added date to current date
# 1. cur.date and post date is same print today.
# 2. post date is yesterday print yesterday
# 3. remaining all should print like how many days ag/o

# import datetime
# from datetime import date,datetime

# def getduration():
# #     currentdate= date.today()
# #     postdate= datetime.datetime.today() - datetime.timedelta(days=1)
    
# #     if currentdate == postdate:
# #         print("its today")
# #     else:
# #         print("postdate is yesterday")    
# # getduration()    

# str_d1 = '2021/10/20'
# str_d2 = '2022/2/20'

# # convert string to date object
# d1 = datetime.strptime(str_d1, "%Y/%m/%d")
# d2 = datetime.strptime(str_d2, "%Y/%m/%d")

# # difference between dates in timedelta
# delta = d2 - d1
# print(f'Difference is {delta.days} days')
# l1 = [1,5,2,8,4,0,3,9]
# length = len(l1)-1
# for l in range(length):
#     i =0 
#     for m in range(length):
#         if l1[i] > l1[i +1]:
#             temp = l1[i+1]
#             l1[i+1]=l1[i]
#             l1[i]=temp
#         i +=1
# print(l1)
l1 = [1,5,2,8,4,0,3,9]
for l in l1:
    i =0 
  
    print('start',l1)# start
    for m in range(len(l1)-1):
        print(i)
        if l1[i] < l1[i+1]:
            temp = l1[i+1]
            l1[i+1]= l1[i]
            l1[i]=temp
        i +=1
        print('second',l1)
print(l1)
# def divde_or_square(number):

#    num= num*num

#    return num


# divide_or_square(number)     





