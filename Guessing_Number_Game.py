import random

zahl = int(input("Rate die Zahl zwischen 1 und 100: "))

random_numb = random.randint(0,100)

while random_numb != zahl :
        if zahl < random_numb :
            print("Gesuchte Zahl ist größer")
            
        elif zahl > random_numb :
            print("Gesuchte Zahl ist kleiner")
           
        zahl = int(input("Rate die Zahl zwischen 1 und 100: "))       
           
print("Gewonnen")