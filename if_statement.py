# 1)
climate=str(input("IS THE CLIMATE IS HOT,COLD OR WARM : "))
temp=climate.lower()
if temp=="hot":
    print("it's a hot day \n","Drink plenty of water")
elif temp=="cold":
    print("it's a cold day \n","Wear warm cloth ")
else:
    print("it is lovely day!!")

# 2)Write a program to check whether a number is positive.
num=int(input("ENTER A NUMBER : "))

if num<0:
    print("NEGATIVE VALUE")
elif num>0:
    print("POSITIVE VALUE ")
else:
    print("IT IS ZERO")

#3)Check whether a person is eligible to vote.
age=int(input("ENTER YOUR AGE : "))

if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible ")

#4)Check whether a number is even or odd.
num=int(input("ENTER A NUMBER : "))
temp=num%2
if temp==0:
    print("IT's EVEN NUMBER")
else:
    print("IT IS ODD NUMBER")

#5)Take a person's age and print:
Child if age is below 13
Teenager if age is 13–19
Adult if age is 20 or above
age=int(input("ENTER YOUR  AGE : "))
if age<13:
    print("Child")
elif age<=19:
    print("Teeenager")
else:
    print("Adult")

#6)Create a simple login system:
print("-----Login Page-----")
current_username = "admin"
current_password = "1234"
temp_username=input("ENTER YOUR USER NAME : ")
temp_password=input("ENTER YOUR PASSWORD : ")
if temp_username==current_username:
    print("CORRECT USRNAME")
    if temp_password==current_password:
        print("CORRECT PASSWORD")
    else:
        print("INCORRECT PASSWORD! Try again!!!")
else:
    print("USERNAME IS INCORRECT !!!! ")
#7)Take three numbers from the user and find the largest number using if statements.
num1=int(input("ENTER A NUMBER 1 : "))
num2=int(input("ENTER A NUMBER 2 : "))
num3=int(input("ENTER A NUMBER 3 : "))
if num1>num2 and num1>num2:
    print("THE HIGHST NUMBER IS ",num1)
elif num2>num1 and num2>num3:
    print("THE HIGHST NUMBER IS ",num2)
else:
    print("THE HIGHST NUMBER IS ",num3)
