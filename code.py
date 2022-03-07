#ask about python, ask about C, ask about universal truth
#make interactive ask about the operators

#operators
print(2+3)
print(7/2)
#but here we are getting floating point, lot of times we need but if we do not need that
#we can do
print(7//2)
#follows BODMAS
print(8+2*3)
print(2**3)
print(10%3)

#variables

x=2
y=8
#variable-why variables, because we can change values
x=5
print(x+y)



#list

nums=[234,56,5787,4747]

#functions of list
print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)

nums.append(45)
print(nums)
nums.insert(3,46)
print(nums)
nums.remove(56)
print(nums)
nums.pop(1)
print(nums)


#tuple
#immutable


#dictionaries
dict={1:"Name1", 2:"Name2", 3:"Name3", 4:"Name4"}
print(dict)
print(dict[3])
#print(dict[5]) #error


#data types

'''None==NULL in other programming languages (no values)
Numeric =int,float, complex, bool
list
tuple
set
String
range -->will be using in for loop
Dictionary
type()

#type converions
b=int(a)
'''
print(int(True))
print(int(False))

#if else
#when we have to go this way or that way

a=5
b=3
if a+b==8:
    print("Yay")
else:
    print("Noi")
    
t=56
if t==54:
    print("heo")
elif t==56:
    print("neo")
else:
    print("leo")
print("afa") 

#you can also write nested loops as many times

#write a program to check if a number is odd or even

#while loop
# print("Vasu")
# print("Vasu")
# print("Vasu")

# we can do this using while loops
# to do this we need a counter

i=1
while i<=5:
    print("Vasu")
    i+=1
print("BREAK")    
# for loop

#geerally we use for over while
for i in range(5): #last excluded starting from 0
    print(i)
print("BREAK")    
for i in range(1,4): #first included last excluded
    print(i)
    print("Vasu")
print("BREAK")    
for i in range(0,10,2):#breaks
    print(i)
    
#iterating a string or a list
x='VASU'
for i in x:
    print(i)
print("BREAK")    
#example of if in for
for i in range(10):
    if i%2==0:
        print(i)


print("ENDED")
print("\n")
#break and continue
#break
for i in range(0,11):
    if(i>5):
        break
    else:
        print(i)
#continue
for i in range(1,10):
    if(i%3==0):
        continue
    else:
        print(i)

#swapping
a=67
b=76
a,b=b,a
print(a)
print(b)
        
#taking input
x=input("Enter the value: ")
print(x)   

    