print("-_------ CALCULATOR--------")
value1=int(input("ENTER THE FIRST VALUE : "))
value2=int(input("ENTER THE SECOND VALUE : "))
symbol=input("WHICH SYMBOL DO YOU WANTED +,-,*,/ :")
if (symbol=="+"):
    add=value1+value2
    print("Result : ",add)
    print("THANK YOU FOR USING")
if (symbol=="-"):
    sub=value1-value2
    print("Result : ",sub)
    print("THANK YOU FOR USING")
if (symbol=="*"):
    multi=value1*value2
    print("Result : ",multi)
    print("THANK YOU FOR USING")
if (symbol=="/"):
    div=value1/value2
    print("Result : ",div)
    print("THANK YOU FOR USING")
