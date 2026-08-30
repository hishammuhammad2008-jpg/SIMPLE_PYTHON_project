#1)if name is less than 3 character long name must be at least 3 characters otherwise if it's more than 50 characters long name can be a maximum of 50 characters  otherwise name look good!
name=str(input("ENTER YOUR NAME :"))
if len(name)<3:
    print("OOP'S !!! ,NAME MUST ATLEAST THREE CHARACTERS ")
elif len(name)>50:
    print("OOP'S!!! ,NAME CAN BE MAXIMUM OF %) CHARACTERS ")
else:
    print("NAME LOOKS GOOD ")
#2) weigth converter
current_weight=float(input("ENTER YOUR WEIGHT : "))
scale=input(" (L)bs or (K)g : ")
if scale.upper()=="L":
    temp=current_weight*0.453592
    print(f"RESUIT :  {temp:.2f} kg")
elif scale.upper()=="K":
    temp=current_weight*2.20462
    print(f"RESUIT :  {temp:.2f} lbs")
else:
    print("SOMTHING GONE WRONG, try again!!!")
#3)Write a program that takes age and citizenship as input.
A person can vote only if:
Age is 18 or above
Citizenship is "Indian"
age=int(input("ENTER YOUR AGE : "))
citizenship=str("ENTER YOUR CITIZENSHIP : ")
if age>=18 and citizenship.lower()=="indian":
    print("HE ELIGIBLE FOR VOTING ")
else:
    print("NOT ELIGIBLE")

#4)Take three numbers and check whether:
# The first number is greater than the second and
# The second number is greater than the third.
value1=int(input("ENTER THE VALUE 1: "))
value2=int(input("ENTER THE VALUE 2: "))
value3=int(input("ENTER THE VALUE 3 : "))
if value1>value2 and value1>value3:
    print("GRETER NUMBER IS ",value1)
elif value2>value1 and value2>value3:
    print("GRETER NUMBER IS ",value2)
else:
      print("GRETER NUMBER IS ",value3)