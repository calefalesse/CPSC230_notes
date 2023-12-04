

import random

print("Welcome to the game! \n")
print("")

PCname = input("Please enter your name: \n")
print("Hello", PCname, "!")
print("")

fileNameAsk = input("Would you like to name your file transcipt? \nEnter 'Y' to rename or 'N' for default: ")
print("")

while fileNameAsk.upper() != 'Y' and fileNameAsk.upper() != 'N':
    print("That is not a valid input. \n")
    fileNameAsk = input("Would you like to name your file transcipt? \nEnter 'Y' to rename or 'N' for default: ")
if fileNameAsk.upper() == 'Y':
        filename = input("Please enter file name: ")
        print("Thanks", PCname, "\n")

elif fileNameAsk.upper() == 'N':
        filename = "file"


file = open(filename + ".txt", "w")

def SaveAndOutputMessage(file, text):
    file.write(text + "\n")
    print(text)


def dice_roller(sides):
    x = random.randint(0,sides)
    return int(x)

class CharacterType():
    Player = ''
    type = ''
    Health = 0
    AttackMod = 0
    AttackDice = 0
    DodgeDice = 0

    def __init__(self, player, type, health, attackMod, attackDice, dodgeDice):
        self.Player = player
        self.Type = type
        self.Health = health
        self.AttackMod = attackMod
        self.AttackDice = attackDice
        self.DodgeDice = dodgeDice
    
    def damage(self): #attacker is dictionary of PC or NPC
        attack_roll = dice_roller(self.AttackDice)
        total_damage = attack_roll + self.AttackMod
        if attack_roll == self.AttackDice:
            print("Wow", self.Player, "rolled the highest attack number!")
        elif attack_roll == 0:
            print("Uh oh", self.Player, "rolled the lowest attack number!")
        return total_damage 

    def dodge(self):
        dodge_roll = dice_roller(self.DodgeDice)
        if dodge_roll == self.DodgeDice:
            print("Wow", self.Player, "rolled the highest dodge number!")
        elif dodge_roll == 0:
            print("Uh oh", self.Player, "rolled the lowest dodge number!")
        return dodge_roll


Barbarian = CharacterType('Sonic', 'Barbarian', 100, 5, 20, 8)
Druid = CharacterType('Shadow', 'Druid', 100, 6, 15, 12)
Monk = CharacterType('Amy', 'Monk', 100, 3, 25, 10)
Warlock = CharacterType('Tails', 'Warlock', 100, 4, 22, 9)
Wizard = CharacterType('Blaze', 'Wizard', 100, 5, 19, 10)
Ranger = CharacterType('Knuckles', 'Ranger', 100, 4, 23, 11)
Bard = CharacterType('Rogue', 'Bard', 100, 5, 21, 9)
Sorcerer = CharacterType('Eggman', 'Sorcerer', 100, 3, 26, 8)



# choosing character
print("Would you like to \n 1) Choose your character \n or \n 2) Have a random selection ?")
PC_choice = input("Please choose 1 or 2: \n")
print("")

while PC_choice.strip() != "1" and PC_choice.strip() != "2":
        print("Sorry, that is not a valid choice. ")
        print("")
        PC_choice = input("Please choose 1 or 2: \n")

if PC_choice.strip() == "1":
    print("Here are your player options: ", "")
    print("")
    print(Barbarian.Player, "\nHealth level:", Barbarian.Health, "\nAttack Modifier:", Barbarian.AttackMod, "\nAttack Dice:", Barbarian.AttackDice, "\nDodge Dice:", Barbarian.DodgeDice)
    print("")
    print(Druid.Player, "\nHealth level:", Druid.Health, "\nAttack Modifier:", Druid.AttackMod, "\nAttack Dice:", Druid.AttackDice, "\nDodge Dice:", Druid.DodgeDice)
    print("")
    print(Monk.Player, "\nHealth level:", Monk.Health, "\nAttack Modifier:", Monk.AttackMod, "\nAttack Dice:", Monk.AttackDice, "\nDodge Dice:", Monk.DodgeDice)
    print("")
    print(Warlock.Player, "\nHealth level:", Warlock.Health, "\nAttack Modifier:", Warlock.AttackMod, "\nAttack Dice:", Warlock.AttackDice, "\nDodge Dice:", Warlock.DodgeDice)
    print("")
    print(Wizard.Player, "\nHealth level:", Wizard.Health, "\nAttack Modifier:", Wizard.AttackMod, "\nAttack Dice:", Wizard.AttackDice, "\nDodge Dice:", Wizard.DodgeDice)
    print("")

    PC = input("Please choose your player: ")
    while True:
        print("")
        if PC.strip().capitalize() == "Sonic":
            print("You chose Sonic! ")
            PC = Barbarian
            break
        elif PC.strip().capitalize() == "Shadow":
            print("You chose Shadow! ")
            PC = Druid
            break
        elif PC.strip().capitalize() == "Amy":
            print("You chose Amy! ")
            PC = Monk
            break
        elif PC.strip().capitalize() == "Tails":
            print("You chose Tails! ")
            PC = Warlock
            break
        elif PC.strip().capitalize() == "Blaze":
            print("You chose Blaze! ")
            PC = Wizard
            break
        else:
            print("Sorry, that is not a valid character. ")
            PC = input("Please choose your player: \n")

elif PC_choice.strip() == "2":
    PC = random.randint(1,5)
    if PC == 1:
        PC = Barbarian
    elif PC == 2:
        PC = Druid
    elif PC == 3:
        PC = Monk
    elif PC == 4:
        PC = Warlock
    elif PC == 5:
        PC = Wizard
    print("Your character is ", PC.Player, "\nHealth level:", PC.Health, " Attack Modifier:", PC.AttackMod, " Attack Dice:", PC.AttackDice, "Dodge Dice:", PC.DodgeDice)  
else:
    print("Sorry, that is not a valid choice. ")
    PC_choice = input("Please choose 1 or 2: ")
    


print("Good choice", PCname, "!")
print("")

# choosing opponent 
print("Now would you like to \n 1) Choose your opponent \n or \n 2) Have a random selection ?")
NPC_choice = input("Please choose 1 or 2: \n")

while NPC_choice.strip() != "1" and NPC_choice.strip() != "2":
        print("Sorry, that is not a valid choice. ")
        print("")
        NPC_choice = input("Please choose 1 or 2: \n")

if NPC_choice.strip() == "1":
    print("Here are your opponent options: \n")
    print(Ranger.Player, "\n", "Health level:", Ranger.Health, "\nAttack Modifier:", Ranger.AttackMod, "\nAttack Dice:", Ranger.AttackDice, "\nDodge Dice:", Ranger.DodgeDice)
    print(Bard.Player, "\n", "Health level:", Bard.Health, "\nAttack Modifier:", Bard.AttackMod, "\nAttack Dice:", Bard.AttackDice, "\nDodge Dice:", Bard.DodgeDice)
    print(Sorcerer.Player, "\n", "Health level:", Sorcerer.Health, "\nAttack Modifier:", Sorcerer.AttackMod, "\nAttack Dice:", Sorcerer.AttackDice, "\nDodge Dice:", Sorcerer.DodgeDice)
    NPC = input("Please choose your player: ")
    while True:
        print("")
        if NPC.strip().capitalize() == "Knuckles":
            print("You chose Knuckles! ")
            NPC = Ranger
            break
        elif NPC.strip().capitalize() == "Rogue":
            print("You chose Rogue! ")
            NPC = Bard
            break
        elif NPC.strip().capitalize() == "Eggman":
            print("You chose Eggman! ")
            NPC = Sorcerer
            break
        else:
            print("Sorry, that is not a valid character. ")
            NPC = input("Please choose your opponent: \n")

elif NPC_choice.strip() == "2":
    NPC = random.randint(1,3)
    if NPC == 1:
        NPC = Ranger
    elif NPC == 2:
        NPC = Bard
    elif NPC == 3:
        NPC = Sorcerer
    print("")
    print("Your opponent is", NPC.Player, "\nHealth level:", NPC.Health, "\nAttack Modifier:", NPC.AttackMod, "\nAttack Dice:", NPC.AttackDice, "\nDodge Dice:", NPC.DodgeDice)   

else:
    print("Sorry, that is not a valid choice. ")
    NPC_choice = input("Please choose 1 or 2: ")


# start of the game
print("")
SaveAndOutputMessage(file,"Your opponent is "+ NPC.Player+ " and you are "+ PC.Player+ "\n")
SaveAndOutputMessage(file,"Both players start at Health level 100. \n")
print("")

RoundNumber = 0
while int(PC.Health) > 0 and int(NPC.Health) > 0:
    RoundNumber += 1
    SaveAndOutputMessage(file, "Round " + str(RoundNumber))
    print("")

    PCmove = input("Please choose to attack or dodge: \n")
    if PCmove.strip().capitalize() != "Attack" and PCmove.strip().capitalize() != "Dodge":
        SaveAndOutputMessage(file, "That is not a valid move. ")
        print("")
        RoundNumber -= 1
        continue


    SaveAndOutputMessage(file,"You chose " + PCmove.strip().capitalize())
    print("")
    
    NPCmove = random.randint(0,1)
    if NPCmove == 0:
        SaveAndOutputMessage(file,NPC.Player+ " dodged! ")
        print("")
    elif NPCmove == 1:
        SaveAndOutputMessage(file,NPC.Player+ " attacked! ")
        print("")

    if NPCmove == 0 and PCmove.strip().capitalize() == "Attack":
        # Computer dodges and Player attacks
        PC_damage = PC.damage() 
        NPC_dodge = NPC.dodge() 
        damageDone = PC_damage - NPC_dodge
        if NPC_dodge > PC_damage:
            damageDone = 0
        SaveAndOutputMessage(file,"Your attack roll was "+ str(PC_damage))
        SaveAndOutputMessage(file,NPC.Player+ " dodge was "+ str(NPC_dodge))
        print("")
        NPC.Health = int(NPC.Health) - int(damageDone)
        SaveAndOutputMessage(file,PC.Player+ " took 0 damage and "+ NPC.Player+ " took "+ str(round((damageDone),1))+ " damage.")

    elif NPCmove == 1 and PCmove.strip().capitalize() == "Attack":
        # Computer attacks and Player attacks
        NPC_damage = NPC.damage()
        PC_damage = PC.damage()
        SaveAndOutputMessage(file,"Your attack roll was "+ str(PC_damage))
        SaveAndOutputMessage(file,NPC.Player+ " attack roll was "+ str(NPC_damage))
        print("")
        NPC.Health = int(NPC.Health) - (PC_damage)
        PC.Health = int(PC.Health) - (NPC_damage)
        SaveAndOutputMessage(file,PC.Player+ " took "+ str(NPC_damage)+ " damage and "+ NPC.Player+ " took "+ str(PC_damage)+ " damage.")

    elif NPCmove == 0 and PCmove.strip().capitalize() == "Dodge":
        # Computer dodges and player dodges
        SaveAndOutputMessage(file,PC.Player+ " took 0 damage and "+ NPC.Player+ " took 0 damage. ")

    elif NPCmove == 1 and PCmove.strip().capitalize() == "Dodge":
        # Computer attacks and player dodges
        NPC_damage = NPC.damage()
        PC_dodge = PC.dodge()
        damageDone = NPC_damage - PC_dodge
        if PC_dodge > NPC_damage:
            damageDone = 0
        SaveAndOutputMessage(file,NPC.Player+ " attack roll was "+ str(NPC_damage))
        SaveAndOutputMessage(file,"Your dodge was "+ str(PC_dodge))
        print("")
        PC.Health = int(PC.Health) - (damageDone)
        SaveAndOutputMessage(file,PC.Player+ " took "+ str(round((damageDone),1))+ " damage and "+ NPC.Player+ " took 0 damage.")
    if int(PC.Health) < 0:
        PC.Health = 0
    elif int(NPC.Health) < 0:
        NPC.Health = 0
    SaveAndOutputMessage(file,PC.Player+ " health level is at "+ str(PC.Health)+ " and "+ NPC.Player+ " health level is at "+ str(NPC.Health)+ "\n")

if int(PC.Health) <= 0:
    SaveAndOutputMessage(file,NPC.Player+ " wins!")
    SaveAndOutputMessage(file,"Nice try "+ PCname+ "!")
elif int(NPC.Health) <= 0:
    SaveAndOutputMessage(file,PC.Player+ " wins!")
    SaveAndOutputMessage(file,"Congrats "+ PCname+ "!")
elif int(PC.Health) <= 0 and int(NPC.Health) <= 0:
    SaveAndOutputMessage(file,"Tie!")
    SaveAndOutputMessage(file,"Good game "+ PCname+ "!")    
else:
    SaveAndOutputMessage(file,"Error")

file.close()