import random



class Ninja:
    attack_moves = ["jab", "bicycle kick", "ninja-star", "meditate"]
    attack_success = ["hit", "miss", "self"]
            

    def __init__(self, name):
        self.name = f" Ninja {name}"
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats(self):
        print(f"\nName:{self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def attack(self, attacker, move):
        if move == Ninja.attack_moves[0]:
            print(f"\n{attacker.player_name} used {Ninja.attack_moves[0]}!")
            attacker.enemy.health -= 10
        if move == Ninja.attack_moves[1]:
            print(f"\n{attacker.player_name} used {Ninja.attack_moves[1]}!")
            self.enemy.health -= 20
        if move == Ninja.attack_moves[2]:
            print(f"\n{attacker.player_name} used {Ninja.attack_moves[2]}!")
            attacker.enemy.health -= 15
        if move == Ninja.attack_moves[3]:
            print(f"\n{self.player_name} used {Ninja.attack_moves[2]}!")
            attacker.speed += 5
            print(f"\n{attacker.player_name}'s speed is now {attacker.speed}!")
        print(f"\n{attacker.enemy.name}'s health is now {attacker.enemy.health}")
        return

