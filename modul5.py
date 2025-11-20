
#gennomgång
"""name = zace"""



"""print(len(name))

for i in range(len(name)):
    print(i+1, end="")"""


"""print(name.upper())
print(name.lower())

choice = input("vill du fortsätta (J)ja (N)nej")

if choice.upper() == "L":
#lägg till
elif choice.lower() =="E"
"""
#start av min egna kod
import random
import os
os.system("cls")

#välkomsprogram
name = input("Vad heter du?  ")
print(f"""
Välkomen {name.upper()}
visste du att det är {len(name)} bokstäver i nament {name.lower()}    """)

#inspiration av Erik botander(Att välja vilket program man vill köra)
task = input("Vilken upgift vill du köra? 1-4: ")





#1
while task == "1":
    number0 = input("skriv ett numer: ")
    if number0.isdigit() == True:
        print("bra jobbat!!!")
        break
    elif number0.isdigit() == False:
        print("Du måste skriva siffror!!!")
        
    


#2
while task == "2":

    print("Välkomen till Högre/Lägre telet spelet! skriv q när som helst under spelet omgång för att stoppa spelet")
    while True:

        number1 = random.randint(1,13)
        print(f"Nummer1 = {number1}")

        gues = input("""Tror du att nästa numer är högre eller lägre
                    skriv h för högre och l för lägre : """)
        if gues == "q":
            print("stänger av spelet")
            break

        number2 = random.randint(1,13)
        print(f"Nummer2 = {number2}")
    
        try:
            if gues == "h" and number2 > number1:
                print(f"Rätt... Andra numret = {number2} och är högre än Första numret som var = {number1}")
            elif gues == "l" and number2 < number1:
                print(f"Rätt... Andra numret = {number2} och är lägre än Första numret som var = {number1}")
            else:
                if gues == "h" and not number2 > number1:
                    print("fel... det var lägre")
                elif gues == "l" and not number2 < number1:
                    print("fel... det var högre ")
        except:
            print("Du måste välja högre(h) eller lägre(l)!!!!")
    break

#3
while task == "3":
    words = len(input("Skriv något: "))
    print(f"Du skrev {words} antal bokstäver/numer")
    break

#4
while task =="4":
    player_input = input("skriv något långt: ")
    max_length = 5

    if len(player_input) > max_length:
        player_input = player_input[:max_length] + "..."
        print(player_input)
        break
    else:
        print(player_input)
        break

