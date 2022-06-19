import random


class Pirate:
    attack_moves = ["hook", "sword", "peg-leg pound"]
    
    
    def __init__( self , name ):
        self.name = f"{name} Pirate"
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"\nName: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, target, move):
        if move == Pirate.attack_moves[0]:
            print(f"\n{target.name} used {Pirate.attack_moves[0]}!")
            target.health -= 10
            return self 
        if move == Pirate.attack_moves[1]:
            print(f"\n{target.name} used {Pirate.attack_moves[1]}!")
            target.health -= 20
            return self
        if move == Pirate.attack_moves[2]:
            print(f"\n{target.name} used {Pirate.attack_moves[2]}!")
            target.health -= 15
        print(f"\n{target.name}'s health is now {target.health}")
        return self
