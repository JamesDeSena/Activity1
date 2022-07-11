# CC223-M: Applications Development and Emerging Technologies
# Activity 4: Python - Object oriented Programming Game Character
# Name: James Leonard M. De Sena (JamesDeSena - Owner)
#       Ron Dominic E. Faustino  (RonDominic - Collaborator)
# Section: BSIS - 2AB

import os
import csv

class Customization:

    character = ""
    cWeapon = ""
    charAbility1 = ""
    charAbility2 = ""
    
    def __init__(self, character, cWeapon, charAbility1, charAbility2):
        self.character = character
        self.cWeapon = cWeapon
        self.charAbility1 = charAbility1
        self.charAbility2 = charAbility2

        header = ['Character', 'Weapon', 'Ability1', 'Ability2']
        data = [character, cWeapon, charAbility1, charAbility2]

        with open('CharacterInfo.csv', 'a', newline='') as file:       
            writer = csv.writer(file) 
            file.seek(0, 2)

            if file.tell() == 0:
                writer.writerow(header)

            writer.writerow(data)

    def setCustomization(item):                     # printing of output

        with open('CharacterInfo.csv', 'r') as filex:
            reader = csv.DictReader(filex)
            for item in reader['Character']:
                #print(item[0], item[1], item[2], item[3])
                print("\t Character Type: " + item['Character'])   # printing of selected character
                print("\t Weapon: " + item['Weapon'])           # printing of selected weapon
                print("\t Abilities: " + item['Ability1'] + " and " + item['Ability2'])    # printing of selected ability 1 and ability 2     

class Character:
    character = {}                                  #declaring character as dictionary

    with open('character.csv', 'r') as file:        #opening of csv file
        reader = csv.reader(file)                           #declaring reader as csv reader
        character = {row[0]:row[1] for row in reader}       #get rows of column 0 and column 1 and put in dictionary
        #print(character)
    
    def getCharacter(self):
        for key in self.character.keys():  # getting the menu_options.keys
            # display the menu_option
            print("\t\t      [{}] {}".format(key, self.character[key]))

        while 1:
            option = input("\n  Choose character: ")     #selecting of character

            if option >= '1' and option <= '4':
                return option, self.character[option]
            else:
                print("Invalid Input! Try again!")        #invalid selected character

class cWeapon:
    cWeapon = {}                                    #declaring cWeapon as dictionary
    
    with open('weapon.csv', 'r') as file:           #opening of csv file
        reader = csv.reader(file)                   #declaring reader as csv reader
        cWeapon = {row[0]:row[1] for row in reader}         #get rows of column 0 and column 1 and put in dictionary
        #print(cWeapon)             

    def getcWeapon(self):
        for key in self.cWeapon.keys():
            print("\t\t     [{}] {}".format(key, self.cWeapon[key]))

        while 1:
            option = input("\n  Enter Weapon: ")                #selecting of weapon

            if option >= '1' and option <= '4':
                return self.cWeapon[option]
            else:
                print("Invalid Input! Try again!")              #invalid selected weapon

class Ability:                                          
    ability = {}                        #declaring ability as dictionary

    with open('abilities.csv', 'r') as file:        #opening of csv file
        reader = csv.reader(file)                   #declaring reader as csv reader
        for row in reader:                          #checking rows in csv
            ability[row[0]] = [row[1], row[2], row[3], row[4]]  #get rows of column 0 and column 1,2,3,4 and put in dictionary
    #print(ability)

    def getAbility(self, ch):
        j = 1

        for i in self.ability.get(ch):              # for loop for selecting 2 abilities
            print("\t\t     [{}] {}".format(j, i))
            j += 1

        while 1:
            option = int(input("\n  Enter Ability 1: "))          #selecting of ability 1

            if option >= 1 and option <= 4:
                while 1:
                    option1 = int(input("  Enter Ability 2: "))    #selecting of ability 2
                    if option1 >= 1 and option1 <= 4:
                        if option == option1:
                            print("Choose another skill! Try again!") #invalid if selected ability is twice
                        else:
                            return self.ability.get(ch)[option-1], self.ability.get(ch)[option1-1]
                    else:
                        print("Invalid Input! Try again!")
            else:
                print("Invalid Input! Try again!")      #invalid selected input


def printLayout():
    os.system("cls")    #clears screen/terminal interface
    print("*"*60)
    print("\t     Welcome to Miscrits World of Adventure")
    print("*"*60)

# Main
PersonList = []
i = 1

while True:                        # while loop for characters until false
    printLayout()                   #calls printlayout def
    characterObject = Character()   #declares variable for Character function
    cWeaponObject = cWeapon()       #declares variable for cWeapon function
    abilityObject = Ability()       #declares variable for Ability function

    ch = characterObject.getCharacter()     #gets selected character from dictionary
    os.system("cls")
    printLayout()
    wp = cWeaponObject.getcWeapon()         #gets selected weapon from dictionary
    os.system("cls")
    printLayout()
    ab = abilityObject.getAbility(ch[0])    #gets selected ability iterated from 0 to 1 from dictionary
    os.system("cls")

    PersonList.append(Customization(ch[1], wp, ab[0], ab[1]))       #calls function to get combined strings
    i += 1

    i = 1
    os.system("cls")
    printLayout()
    for user in PersonList:      
        print("  Character Number {}".format(i))
        user.setCustomization()
        i += 1
    while True:     #while loop if blank message repeat
        gotcha = input("\n  Would you like to continue? (0|1): ")
        if gotcha != "":
            break       #breaks the loop if user input 0 or 1
        else:
            continue
    if gotcha == '0':
            break       #exits program if user input 0
    else:               #repeats the whole character selection
        os.system("cls")    