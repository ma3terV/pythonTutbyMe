# #functions

#without any return statement
# def fun(num):
#     print(num)
    
# fun(9)  (calling of the function )




# def check(num):
#     if(num%2==0):
#         print("even")
#     else:
#         print("odd")
# num=int(input())        
# check(num)



#with return statement
#def checkeven(list):
#     list1=[]
    
#     for i in list:
#         if(i%2==0):
#             list1.append(i)
    
#     return list1

# list=[2, 4, 5 ,8, 3]
# list1=checkeven(list)
# print(list1)



#pass statement
# def addition(a,b):
#     pass
# addition(2,10)


# x=10
# def fun():
#     print(x)
    
# fun()

# def palinChecker(num):
#     n=num
#     sum=0
#     while n>0:
#         rem=n%10
#         sum=(sum*10)+rem
#         n=n//10
#     if(sum==num):
#         return 1
#     else:
#         return 0
    

# k=palinChecker(1341)
# if(k==1):
#     print("palin")
# else:
#     print("Not palin")


#global variables
# global x
# x=10
# print(x)
# def fun():
#     x=15
# fun()
# print(x)    
