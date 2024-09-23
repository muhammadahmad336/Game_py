import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move(self, steps):
        self.position += steps
        if self.position > 29:  
            self.position = 29  
        print(f"{self.name} is now at position {self.position}")

def ludo_game():
    player1 = Player("Ahmad")
    player2 = Player("Usman")
    
    while player1.position < 29 and player2.position < 29:
        for player in [player1, player2]:
            input(f"{player.name}, press Enter ")
            steps = player.roll_dice()
            print(f"{player.name} rolled a {steps}")
            player.move(steps)

    winner = player1 if player1.position >= 29 else player2
    print(f"{winner.name} wins!")

if __name__ == "__main__":
    ludo_game()
