from classes.ninja import Ninja
from classes.pirate import Pirate
import inquirer
import random
import time

# michelangelo = Ninja("Michelanglo")

# jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

class Gameplay:
    attack_success = ["hit", "miss", "self"]
    character_choice = [
                inquirer.List('char',
                            message="Choose your character:",
                            choices=['Ninja', 'Pirate'],)]
            

    if __name__ == "__main__":
        def __init__(self):
            print("\nWelcome to Ninjas vs Pirates!")
            self.player_name = input("\nEnter your player name:\n")

            

    def attack_sequence(self, attacker):
        attack = [
            inquirer.List('move',
                        message="What attack move would you like to use?",
                        choices= attacker.char.attack_moves,),] 
        move = inquirer.prompt(attack)
        move_accuracy = random.choice(Gameplay.attack_success)
        if move_accuracy == "hit":
            attacker.char.attack(attacker.enemy, move['move'])
        if move_accuracy == "miss":
            print(f"Oh no! {self.player_name}'s attack missed!")
        if move_accuracy == "self":
            attacker.char.health -= 5
            print(f"Oops! {self.player_name} hurt themsevles!")
        time.sleep(2)
        attacker.enemy_attack(attacker)
        


    def enemy_attack(self, target):
        print(f"\nNow it's time for {self.enemy.name} to attack!")
        time.sleep(3)
        enemy_move_accuracy = random.choice(Gameplay.attack_success)
        if enemy_move_accuracy == "hit":
            target.enemy.attack(target.char, random.choice(target.enemy.attack_moves))
        if enemy_move_accuracy == "miss":
            print(f"\nOh no! {target.enemy.name}'s attack missed!")
        if enemy_move_accuracy == "self":
            target.enemy.health -= 5
            print(f"\nOops! {target.enemy.name} hurt themsevles!")
            time.sleep(3)
        player1.next_turn(player1)

    def next_turn (self, player):
        if player1.char.health > 0:
            player1.char.show_stats()
            time.sleep(2)
            if player1.enemy.health > 0:
                player1.enemy.show_stats()
                next_move = [
                    inquirer.List('next',
                            message="What would you like to do next?",
                            choices=["Attack","Quit",]),]
                time.sleep(2)
                next = inquirer.prompt(next_move)
                if next['next'] == "Attack":
                    player.attack_sequence(player1)
                else:
                    return self
            else:
                print(f"You defeated {player1.enemy.name}!")
                return self
        else:
            print("You lost...")
            return self


    @classmethod 
    def characters(cls, player):
        character = inquirer.prompt(cls.character_choice)
        if character['char'] == 'Ninja':
            player.playertype = "Ninja"
            player.char = Ninja(player1.player_name)
            player.enemy = Pirate("Petey")
        else:
            player.playertype = "Pirate"
            player.char = Pirate(player1.player_name)
            player.enemy = Ninja("Gnarly")

player1 = Gameplay()
player1.characters(player1)
begin_game = [
    inquirer.List('choice',
                message=f"Okay {player1.player_name}, Are you ready to battle against {player1.enemy.name}?",
                choices=['Yes','No' ],),]
begin = inquirer.prompt(begin_game)
if begin['choice'] == 'Yes':
    player1.attack_sequence(player1)
else:
    print("Aaargh! We hope you're ready next time....")

print("We hope you enjoyed playing Ninjas vs Pirates!")

