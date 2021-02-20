#progam to make simple calcuator using fuctions
#define the  fuctions

def add (x,y):
#This function adds 2 numbers
    return x + y

def substarct (x,y):
#This function substarcts  2 numbers
    return x - y

def multiply (x,y):
#This function  multiplys 2 numbers
   return x*y

def devide  (x,y):
#This function devides  2 numbers
    return x / y

def power  (x,y):
#This give power
  return pow (x,y)

#take input from user
print ("Select opration.")
print ("1.Mdd")
print ("1.Substarct")
print ("1.Multiply")
print ("1.Devide")
print ("1.Power")
choice=input("Enter choice (1/2/3/4/5):")
num1=int(input("Enter first number:"))
num2=int(input("Enter the seconde  number:"))

if choice =="1":
    print (num1, "+", num2,"=", add ( num1,num2))
elif choice =="2":
    print(num1, "-", num2, "=", substract(num1,num2))
elif choice =="3":
    print(num1, "*", num2, "=", multiply(num1,num2))
elif choice =="4":
    print(num1, "/", num2, "=", devide(num1,num2))
elif  choice =="5":
     print(num1, "^", num2, "=", power(num1,num2))
else:
    print("Invalid input")


