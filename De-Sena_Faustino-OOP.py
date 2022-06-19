# CC223-M: Applications Development and Emerging Technologies
# Activity 3: Python - Object oriented Programming
# Name: James Leonard M. De Sena (JamesDeSena - Owner)
#       Ron Dominic E. Faustino  (RonDominic - Collaborator)
# Section: BSIS - 2AB

import os

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

    def setCustomization(self):                     # printing of output
        print("\t  Character Type: " + self.character)   # printing of selected character
        print("\t  Weapon: " + self.cWeapon)           # printing of selected weapon
        print("\t  Ability 1: " + self.charAbility1)    # printing of selected ability 1
        print("\t  Ability 2: " + self.charAbility2)    # printing of selected ability 2

class Character:
    character = {                   #list of characters
        1: 'Wizard',
        2: 'Knight',
        3: 'Archer',
        4: 'Assasin',
    }

    def getCharacter(self):
        for key in self.character.keys():  # getting the menu_options.keys
            # display the menu_option
            print("\t      [{}] {}".format(key, self.character[key]))

        while 1:
            option = int(input("\n  Choose character: "))     #selecting of character

            if option >= 1 and option <= 4:
                return option, self.character[option]
            else:
                print("Invalid Input! Try again!")        #invalid selected character


class cWeapon:
    cWeapon = {                     # listing of character weapons
        1: 'Wizard Staff',
        2: 'Sword',
        3: 'Bow & Arrow',
        4: 'Katar',
    }

    def getcWeapon(self):
        for key in self.cWeapon.keys():
            print("\t    [{}] {}".format(key, self.cWeapon[key]))

        while 1:
            option = int(input("\n  Enter Weapon: "))              #selecting of weapon

            if option >= 1 and option <= 4:
                return self.cWeapon[option]
            else:
                print("Invalid Input! Try again!")              #invalid selected weapon


class Ability:                                          
    ability = {                                                                     # listing of ability
        1: ["Energy Ball", "Dragons Breath", "Crown of Flame", "Hail Storm"],
        2: ["Fire Slash", "Power Slash", "Gigantic Storm", "Chaotic Disaster"],
        3: ["Take Aim", "Quick Shot", "Blazing Arrow", "Frost Arrow"],
        4: ["Cloaking", "Enchant Posion", "Sonic Acceleration", "Meteor Assault"],
    }

    def getAbility(self, ch):
        j = 1

        for i in self.ability.get(ch):              # for loop for selecting 2 abilities
            print("\t    [{}] {}".format(j, i))
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
    print("*"*40)
    print(" Welcome to Miscrits World of Adventure")
    print("*"*40)

# Main
PersonList = []
i = 0

while i < 2:                        # while loop for 2 characters
    printLayout()
    characterObject = Character()
    cWeaponObject = cWeapon()
    abilityObject = Ability()

    ch = characterObject.getCharacter()
    os.system("cls")
    printLayout()
    wp = cWeaponObject.getcWeapon()
    os.system("cls")
    printLayout()
    ab = abilityObject.getAbility(ch[0])
    os.system("cls")

    PersonList.append(Customization(ch[1], wp, ab[0], ab[1]))
    i += 1

i = 1
os.system("cls")
printLayout()
for user in PersonList:
    print("  Character Number {}".format(i))
    user.setCustomization()
    i += 1