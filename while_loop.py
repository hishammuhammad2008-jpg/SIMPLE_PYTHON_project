#1)
# i=1
# while i<=5:
#     f=('*'*i)
#     print(f)
#     i+=1

#2)gussing game
# max_guess=3
# guss_count=0
# secret_pass=9
# while guss_count<max_guess:
#     guss_count+=1
#     input_value=int(input("GUESSNUMBER FROM 1 TO 10 : "))
#     if(input_value==secret_pass):
#         print("YOU WIN!!")
#         break
# else:
#     print("try again")       

# #3)car race

# first_point=str(input(">"))
# if first_point.lower()=="help":
#     print("start-to start the car \n","stop- to stop the car \n","quit- to exit \n")
# else:
#     print("I don't understand!!")
# while i<3:
#     second_point=str(input(">"))
#     if second_point.lower()=="start":
#         print("CAR STARTED")
#     elif second_point.lower()=="stop":
#         print(" car is stopped ")
#     elif second_point.lower()=="quiet":
#         print("quieting")
#         break 
# # or
# condition=""
# started=False
# while True:
#     condition=input(">").lower()
#     if condition=="start":
#         if started:
#             print("CAR IS ALREADY STARTED ...")
#         else:
#             started=True
#             print("CAR START ....")
#     elif condition=="stop":
#         if not started:
#             print("CAR IS ALREADY STOPED")
#         else:
#             started=False
#             print("CAR STOPED...")
#     elif condition=="help":
#         print("""
# start-- start the car 
# stop-- stoping the car 
# quiet--quit the game""")
#     elif condition=="quiet":
#        break
#     else:
#         print("I DON'T UNDERSTAND ...")
#4)Write a Python program using a while loop to print numbers from 1 to 10
# num=1
# while num<=10:
#     print(num)
#     num+=1

 #5)
num=0
# while num<20:
    # num+=2
    # print(num)
#5)
# num=0
# sum=0
# while num<10:
#     sum+=num
#     num+=1
# print(sum)
