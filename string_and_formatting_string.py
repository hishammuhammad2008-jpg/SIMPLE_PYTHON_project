# 1)Replace "Java" with "Python" in "I like Java".
first_name="I LOVE JAVA"
second1_name="muhammed"
temp=first_name.replace("JAVA","python")
print(temp)

#2)Check whether "Python" exists in "I am learning Python".
item="  i am learrning python "
temp="python" in item
print("Python" exists in "I am learning Python : ",temp)

#3)Remove extra spaces from " Hello_Python ".
item="  Hello_Python  "
temp=item.strip()
print(temp)

#4)Split "apple,banana,orange" into a list.
item="apple","banana","orange"
temp=list(item)
print(temp)

#5)Join the list ["Python", "is", "fun"] into one string.
item=["Python", "is", "fun"]
print(" ".join(item))

#6)Create variables name = "Hisham" and age = 20. Print: "My name is Hisham and I am 20 years old."
name="Hisham"
age=20
print(f"my name is {name} and i am {age} years old")

#7)Ask the user for their name, age, and city, then display:
user_name=input("ENTER YOUR NAME : ")
user_age=input("ENTER YOUR AGE : ")
user_city=input("ENTER YOUR CITY NAME :" )
print(f"My name is {user_name} . I am {user_age} years old I live in {user_city}")

#8)Ask the user for a product name and price. Display the price with exactly 2 decimal places.
product_name=str(input("ENTER YOUR PRODUCT NAME : "))
product_name1=product_name.upper()
product_price=float(input("ENTER YOUR PRODUCT PRICE : "))
print(f"THE PRODUCT NAME {product_name1}  AND  IT'S PRICE {product_price:.2f}")

  