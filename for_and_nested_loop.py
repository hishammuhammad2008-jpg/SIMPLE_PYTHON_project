for i in range(5):
    i+=1
    print(i)
# #2)
for i in range (10):
    print("5 *", i, "=", 5 * i)
#3)
for i in range(6):
    print(f"*{"*"*i}\n")

#nesteedloop
#Write a Python program using a nested for loop to print:
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()

#2)

for i in range(5):
    for j in range(1,6):
        print(j,end="")
    print()

#3)
num=[2,4,6]
for i in num:
    for k in range(i):
        print('*',end="")

    print()