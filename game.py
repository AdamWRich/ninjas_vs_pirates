from classes.ninja import Ninja
from classes.pirate import Pirate
import inquirer
import random

# michelangelo = Ninja("Michelanglo")

# jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

class Gameplay:
    if __name__ == "__main__":
        def __init__(self):
            print("\nWelcome to Ninjas vs Pirates!")
            self.player_name = input("\nEnter your player name:\n")
            character_choice = [
                inquirer.List('char',
                            message="Choose your character:",
                            choices=['Ninja', 'Pirate'],)]
            character = inquirer.prompt(character_choice)
            if character['char'] == 'Ninja':
                self.playertype = "Ninja"
                self.enemy = Pirate("Petey")
            else:
                self.playertype = "Pirate"
                self.enemy = Ninja("Gnaryly")
        
        def attack_sequence(self, attacker):
            attack_success = ["hit", "miss", "self"]
            if Ninja1.health > 0:
                attack = [
                    inquirer.List('move',
                                message="What attack move would you like to use?",
                                choices=Ninja.attack_moves,),] 
                move = inquirer.prompt(attack)
                move_accuracy = random.choice(attack_success)
                if move_accuracy == "hit":
                    Ninja.attack(self, attacker, move['move'])
                if move_accuracy == "miss":
                    print(f"Oh no! {self.player_name}'s attack missed!")
                if move_accuracy == "self":
                    Ninja1.health -= 5
                    print(f"Oops! {self.player_name} hurt themsevles!")
                print(f"\nNow it's time for {self.enemy.name} to attack!")
                enemy_move_accuracy = random.choice(attack_success)
                if enemy_move_accuracy == "hit":
                    Pirate.attack(player1, player1.enemy.name, random.choice(Pirate.attack_moves), Ninja1)
                if enemy_move_accuracy == "miss":
                    print(f"Oh no! {attacker.enemy.name}'s attack missed!")
                if enemy_move_accuracy == "self":
                    attacker.enemy.health -= 5
                    print(f"Oops! {attacker.enemy.name} hurt themsevles!")
                Ninja1.show_stats()
                player1.enemy.show_stats()
                if player1.enemy.health > 0:
                    next_move = [
                        inquirer.List('next',
                                message="What would you like to do next?",
                                choices=["Attack","Quit",]),]
                    next = inquirer.prompt(next_move)
                    if next['next'] == "Attack":
                        self.attack_sequence(player1)
                    else:
                        return self
                else:
                    print(f"You defeated {player1.enemy.name}!")
                    return self
            else:
                print("You lost....")
                return self

player1 = Gameplay()
begin_game = [
    inquirer.List('choice',
                message=f"Okay {player1.player_name}, Are you ready to battle against {player1.enemy.name}?",
                choices=['Yes','No' ],),]
begin = inquirer.prompt(begin_game)
if begin['choice'] == 'Yes':
        if player1.playertype == "Ninja":
            Ninja1 = Ninja(player1.player_name)
        if player1.playertype == "Pirate":
            Pirate1 = Pirate(player1.player_name)
else:
    print("Aaargh! We hope you're ready next time....")

if Ninja1:
    player1.attack_sequence(player1)

print("We hope you enjoyed playing Ninjas vs Pirates!")

