weight_in_pound=input("ENTER THE WEIGHT OF PERSON IN POUND : ")
temp=float(weight_in_pound)#we use float becauce weight contain fractional part like eg:157.4
kg_convert=temp*0.454 #So, one pound approximately 0.454 kg.
print(weight_in_pound," POUND IN ",kg_convert," kg")