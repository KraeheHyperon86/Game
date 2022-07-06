import random

zahl = int(input("Ratte die Zahl zwischen 1 und 100: "))
print("\n")
random_numb = random.randint(0,100)

while random_numb != zahl :
        if zahl < random_numb :
            print("Gesuchte Zahl ist groesser als " + str(zahl) )
            print("\n")
        
        elif zahl > random_numb :
            print("Gesuchte Zahl ist kleiner als " + str(zahl))
            print("\n")
           
        zahl = int(input("Ratte die Zahl, zwischen 1 und 100: "))       
           



print("Gewonnen")