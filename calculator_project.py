print("-_------ CALCULATOR--------")
value1=int(input("ENTER THE FIRST VALUE : "))
value2=int(input("ENTER THE SECOND VALUE : "))
symbol=input("WHICH SYMBOL DO YOU WANTED +,-,*,/ :")
if (symbol=="+"):
    add=value1+value2
    print("Result : ",add)
if (symbol=="-"):
    sub=value1-value2
    print("Result : ",sub)
if (symbol=="*"):
    multi=value1*value2
    print("Result : ",multi)
if (symbol=="/"):
    div=value1/value2
    print("Result : ",div)