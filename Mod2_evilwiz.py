
# Base Character class creator, added heal counter for potions and parameters for when a character cant heal and cant attack
class Character:
    import random
    def __init__(self, name, health, attack_power, healcnt, cantheal, cantatt):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.healcnt = healcnt
        self.cantheal = bool(cantheal) 
        self.cantatt = bool(cantatt)
#Main attack function 
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
#This function holds the Wizards attacks, uses a random int in the battle function
    def sp_attack(self, opponent, sp_att_int):
        if sp_att_int == 1:
            sp_val = 15
            print(f'{self.name} attacks with Sweeping Flames across the battlefield')
        if sp_att_int == 2:
            sp_val = 20
            print(f'{self.name} CRITICAL STRIKE ON {opponent.name}')
        if sp_att_int == 3:
            sp_val = 5
            print(f'{self.name} casts a piercing Ice Spike into {opponent.name} preventing healing!')
            opponent.cantheal = True
        if sp_att_int == 4:
            sp_val = 10
            print(f'{self.name} attacks with poison orbs that infect the player!') 
        
        sp_attack = (self.attack_power + sp_val)
        opponent.health -= sp_attack
        print(f"{self.name} attacks {opponent.name} with a special attack for {sp_attack} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
#function prevents a attack when conditions are met, removes attack power
    def cantatt(self, oppenent, player):
        self.cantatt = False
        cantatt = False
        self.opponent = oppenent
        self.player = player
        if cantatt == True:
            self.attack_power -= self.attack_power
            (f'{self.name} cant attack!')
#display stats    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
#heal function to restore health 
    def heal(self, player):
        if player.cantheal == False:
            if player.healcnt > 0:
                player.healcnt -= 1            
                player.health += 25
                print(f'{self.name} heals for 10 health, {self.healcnt} potions left')
                pass
            elif player.healcnt < 0:
                print('YOU HAVE NO HEALS LEFT')
                pass     


#MARK: CLASS WARRIOR
#Warrior class is a basic power up and attack playstyle
class Warrior(Character):
    def __init__(self, name):
        self.sp_name_1 = 'Spirt Strike'
        self.sp_name_2 = 'Rally Cry'
        super().__init__(name, health=150, attack_power=35, healcnt=5, cantheal= False, cantatt= False)
#Attack w extra power    
    def sp_attack_1(self, opponent, sp_name):
        self.sp_name = sp_name
        sp_name = 'SpirtStrike'
        sp_attack = self.attack_power + 10
        opponent.health -= sp_attack
        print(f"{self.name} attacks {opponent.name} with a {sp_name} for extra damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
##Rally Cry boost attack power and grants a heal based on the wiz health level     
    def sp_attack_2(self, opponent, sp_name):
        import random
        self.sp_name = sp_name
        sp_name = 'Rally'
        self.attack_power += 2
        self.health += 10
        print(f"{self.name} gets STRONGER! +5 attack power  Current health: {self.health}")
        if opponent.health <= 200:
            opponent.attack_power -= 2
            self.attack_power += random.randint(0,5)
            print(f"{self.name} intimidates {opponent.name} with a {sp_name} cry! {opponent.name} loses attack power, and {self.name} gets a attack boost")
        elif opponent.health <= 100:
            opponent.attack_power -= 3
            print(f"{self.name} intimidates {opponent.name} with a {sp_name} cry! {opponent.name} loses attack power")
        elif opponent.health <= 50:
            opponent.attack_power -= 5
            print(f"{self.name} intimidates {opponent.name} with a {sp_name} cry! {opponent.name} loses attack power")
                
#MARK: CLASS Mage
#mage is a effect playstyle to alter the battle instead of fighting thru it, usues a mana bank that must be charged 
class Mage(Character): #all mage attacks carry chip dmg 
    def __init__(self, name, mana=100,):
        self.mana = mana
        self.sp_name_1 = 'Spellcast'
        self.sp_name_2 = 'Mana Charge'
        super().__init__(name, health=125, attack_power=25, healcnt=3, cantheal= False, cantatt= False,)
        pass
#Spellcast uses mana and causes effects to wiz status 
    def sp_attack_1(self, opponent, sp_name,):
        self.sp_name = sp_name
        sp_name = 'SpellCast'
        print('select your attack, 1,2,or 3')
        print('1. Flame Bolt Spell - burn dmg prevents healing')
        print('2. Frost Bite Spell - wizard cant attack next round')
        print('3. Enchancement - raises attack power, but no attack')
        sc_pick = input('Choose a attack: ')
        sc_bonus = int(0)
        if self.mana <= 0:
            print('NO MANA, MUST RECHARGE')
        else:
            if sc_pick == "1":
                spellname = 'Flame Bolt'
                print (f'{spellname} used, {opponent.name} takes {self.attack_power + sc_bonus} damage and cant heal this turn')
                sc_bonus + 5
                opponent.cantheal = True 
                self.mana -= 25
                print(f'Mana Level is {self.mana}')
            elif sc_pick == "2":
                spellname = 'Frost Bite'
                print (f'{spellname} used, {opponent.name} takes {self.attack_power + sc_bonus} damage and reduced attack power, and cant attack')
                opponent.attack_power -= 5
                opponent.cantatt = True
                self.mana -= 50
                print(f'Mana Level is {self.mana}')
                sc_bonus + 5 
            elif sc_pick == "3":
                spellname = "Enchancement"
                print (f'{spellname} used, {self.name} gains some attack power, but can\'t attack this turn!')
                self.mana -= 10
                self.attack_power + 3
                self.cantatt = True
                print(f'Mana Level is {self.mana}')
            else:
                print('Invalid Selection, Choose again')        
            opponent.health -= (self.attack_power + sc_bonus)
            print(f"{self.name} attacks {opponent.name} with a {spellname}")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
    
    def sp_attack_2(self, opponent, sp_name):
        self.sp_name = sp_name
        sp_name = 'Mana Charge'
        self.mana += 50
        print(f"{self.name} recharges Mana levels, ")
       

#MARK: CLASS Fool
#Glass canon and randomness playstyle, 
class Fool(Character): #has better crit chances 
    def __init__(self, name):
        self.sp_name_1 = 'Weapon Swap'
        self.sp_name_2 = 'Top Hat'       
        super().__init__(name, health=125, attack_power=20, healcnt=5, cantheal= False, cantatt= False)

    def sp_attack_1(self, opponent, sp_name):
        self.sp_name = sp_name
        import random #fool has 3 weapons to pull from, weapons are randomly cycled
        sp_name = 'Weapon Swap'
        weapick = int(random.randint(1,3))
        print(weapick)
#Musket runs a random int and adds that to attack power         
        if weapick == 1:
            weapick = 'Musket'
            weapwr = 2*random.randint(0,6)
            print (f'{self.name}\'s {weapick} used, {opponent.name} takes {self.attack_power + weapwr} damage!')
            opponent.health -= (self.attack_power + weapwr)
#Club is a more straightforward attack 
        elif weapick == 2:
            weapick = 'Jester Club'
            weapwr = 10
            print (f'{self.name}\'s {weapick} used, {opponent.name} takes {self.attack_power + weapwr} damage!')
            opponent.health -= (self.attack_power + weapwr)
#horn is the effect style attack that randomizes 2 diff songs 
        elif weapick == 3:
            weapick = 'Horn'
            song = random.randint(0,2)
            if song == 1:
                print(f'{self.name} uses {weapick} and plays a intimidating melody, {opponent.name} loses attack power!')
                opponent.attack_power -= 2
            elif song == 2:
                print(f'{self.name} uses {weapick} and plays a soothing melody to gain health!')
                self.health += 20
            pass
#attack based random int and wiz attack power
    def sp_attack_2(self, opponent, sp_name): 
        import random
        self.sp_name = sp_name 
        sp_name = "Top Hat"
        top_hat_attack = self.attack_power + (random.randint(0,3) % opponent.attack_power)
        opponent.health -= int(top_hat_attack)
        print(f'{self.name} pulls a trick out of his hat! {top_hat_attack} damage to the {opponent.name}!')
        

#MARK: CLASS Tank
#larger health pool and damage mitigation/storage traits 
class Tank(Character):
    def __init__(self, name, absorb=0):
        self.sp_name_1 = 'Offload'
        self.sp_name_2 = 'Bunker'
        self.absorb = absorb
        if self.absorb > 0:
            self.absorb - 5
        super().__init__(name, health=200, attack_power=30, healcnt=3, cantheal= False, cantatt= False)

    def sp_attack_1(self, opponent, sp_name): #does dmg based on health level  
        self.sp_name = sp_name
        sp_name = "Offload"
        absorb_dmg = (opponent.attack_power % .5)
        opponent.health -= ((absorb_dmg + self.absorb) + self.attack_power)
        print(f'{self.name} attacks {opponent.name} with a {sp_name} attack from stored damage inflicted in battle! {self.absorb} damage added!')
        pass

    def sp_attack_2(self, opponent, sp_name):
        sp_name = 'Bunker'
        if opponent.attack_power >= 1:
            self.absorb += (opponent.attack_power) #next attack from wiz value is stored in absorb
            print(f'{self.name} uses {sp_name} down for next attack from {opponent.name}')        
        pass

#MARK: CLASS Evil Wizard
#Wizard function, 
class EvilWizard(Character,):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=15, healcnt=0, cantheal= False, cantatt= False)
    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

#MARK: Chr Create
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Fool") 
    print("4. Tank")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Fool(name)
    elif class_choice == '4':
        return Tank(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
#MARK: Battle
def battle(player, wizard):
    import random
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print(f'\n{player.name} current health = {player.health}'.title())
        print('\n-----------------')
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")
#battle choices live here
        if choice == '1': #simple attack
            player.attack(wizard)
        elif choice == '2': #special attacks
            print(player.sp_name_1)
            print(player.sp_name_2)
            spec_attack = input('Choose Special Attack 1 or 2: ')
            if spec_attack == '1':
                player.sp_attack_1(wizard,"")
            elif spec_attack == '2':
                player.sp_attack_2(wizard,"")
            pass 
        elif choice == '3': #healing 
            if player.cantheal == True:
                    print('player cant heal')
                    player.cantheal == False
                    continue
            elif player.cantheal == False:
                player.heal(player)
            pass  
        elif choice == '4': #show stats
            player.display_stats()
            continue
        else:
            print("Invalid choice. Try again.")
            continue
#wizard value checks 
        if wizard.health > 0:
            if wizard.cantheal is True:
                print('WIZARD CANT HEAL')
                wizard.cantheal = False
                continue
            if wizard.cantatt is True:
                print('WIZARD CANT ATTACK THIS ROUND')
                wizard.cantatt = False
                continue
            else:
                wizard.regenerate()
                wizattack = random.randint(1,4)
                if wizattack == 1:
                    wizard.attack(player)
                if wizattack == 2:
                    wizard.sp_attack(player, 1)
                if wizattack == 3:
                    wizard.sp_attack(player, 2)
                if wizattack == 4:
                    wizard.sp_attack(player, 3)
                    player.cantheal = True
                    print('player cant heal')
                    player.cantheal = False
        wizard.cantheal = False
        wizard.cantatt = False
         



        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()

