#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# RandomPlayer makes a move using random library in our moves list
class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))

    def learn(self, my_move, their_move):
        pass


# HumanPlayer gets manuel input from the prompt
# and check if it's in the moves list
# if true, we return it
# if not, ask the user to enter a correct move
class HumanPlayer(Player):
    def move(self):
        human_move = input("What's your move?\n Rock, Paper or Scissors? ")
        human_move = human_move.lower()
        while True:
            if human_move in moves:
                return human_move
            if human_move not in moves and human_move != 'quit':
                human_move = input(f"\nInvalid move!\nRock? Paper? Scissors? "
                                   f"or quit?")
            if human_move == 'quit':
                exit()

    def learn(self, my_move, their_move):
        pass


# Reflect player remembers what move the other player played
# last round and plays that move this round.
class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = ''

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.their_move == '':
            return (random.choice(moves))
        else:
            return self.their_move


# Cycle player remembers what move played last round, and
# cycles through the different moves.
class CyclePlayer(Player):
    def __init__(self):
        self.previous_move = ''

    def move(self):
        if self.previous_move == '':
            move = Player.move(self)

        else:
            if self.previous_move == moves[0]:
                move = moves[1]
            elif self.previous_move == moves[1]:
                move = moves[2]
            elif self.previous_move == moves[2]:
                move = moves[0]
        self.previous_move = move
        return move

    def learn(self, my_move, their_move):
        pass


# This is where we define players
# scores,winning condition
# and display it
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.wins = 0
        self.losses = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"Player 1 selects: {move1} \nPlayer 2 selects: {move2}")

        if self.beats(move1, move2):
            self.wins += 1
            print("--Player 1 Wins!--")
            print(f"Score:\nP1: {self.wins} -"
                  f" P2: {self.losses} \n")
        elif self.beats(move2, move1):
            self.losses += 1
            print("--Player 2 Wins!--")
            print(f"Score:\nP1: {self.wins} -"
                  f" P2: {self.losses} \n")
        else:
            print("--It's a Draw!--")
            print(f"Score:\nP1: {self.wins} -"
                  f" P2: {self.losses} \n")

        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

    def play_game(self):
        print("Welcome to 'Rock, Paper and Scissors'\n"
              "Select your move or type 'quit' to leave the game!\n")
        for round in range(5):
            print(f"Round {round+1}:")
            self.play_round()
        print(f"\nGame Over!\nPlayer 1: {self.wins} -"
              f" Player 2: {self.losses} ")
        if self.wins > self.losses:
            print("Winner: Player 1\n")
        elif self.wins < self.losses:
            print("Winner: Player 2\n")
        else:
            print("Winner: Sportmanship :)\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
