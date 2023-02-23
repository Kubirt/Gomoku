##
## EPITECH PROJECT, 2022
## B-AIA-500-NAN-5-1-gomoku-arthur.richard
## File description:
## protocol
##

import random
import sys
from src.naive_ai import naive_ai

class CommandHandler():
  command: str
  boardSize: int = 0
  boardTab: list[int] = []
  ai: naive_ai = naive_ai()

  def print_board(self):
    for i in range(0, ((self.boardSize) * (self.boardSize))):
      if (i % (self.boardSize) < self.boardSize - 1):
        print(f'{self.boardTab[i]}', end=" ")
      else:
        print(f'{self.boardTab[i]}')

  def info(self):
    return

  def place_stone(self, x: int, y: int, player: int) -> int:
    try:
      if (x > len(self.boardTab) / self.boardSize or
        y > len(self.boardTab) / self.boardSize or
        player != 1 and player != 2):
        print("err: you must provide correct coordinates or player id.", flush=True, file=sys.stderr)
        return -1
      targeted_coordinates = self.boardTab[self.boardSize * y + x]
      if (targeted_coordinates == 0):
        self.boardTab[self.boardSize * y + x] = player
      else:
        return -1
    except ValueError:
        print("err: you must provide corrects coordinates format (must be numbers).", flush=True, file=sys.stderr)
    return 0

  def start(self):
    tempBoardSize = 0
    try:
      if (" " not in self.command):
        print("ERROR you must provide a size.", flush=True)
        return
      tempBoardSize = int(self.command.split(" ", maxsplit=1)[1])
    except ValueError:
      print("ERROR you must provide a single number argument.", flush=True)
      return
    if (tempBoardSize < 5):
      print("ERROR Size must be at least of 5.", flush=True)
      return
    self.boardSize = tempBoardSize + 2
    for i in range(0, (self.boardSize) * (self.boardSize)):
      if ((i >= 0 and i < self.boardSize) or (i > ((self.boardSize) * (self.boardSize) - (self.boardSize + 1))) or (i % (self.boardSize) == 0) or (i % (self.boardSize) == (self.boardSize - 1))):
        self.boardTab.append(-1)
      else:
        self.boardTab.append(0)
    print("OK", flush=True)

  def end(self):
      exit(0)
  
  def turn(self):
    coordinates = []
    try:
      if (" " not in self.command):
        print("err: you must provide coordinates.", flush=True, file=sys.stderr)
        return
      coordinates = self.command.split(" ", maxsplit=1)[1].split(",", maxsplit=1)
      coordinate_x = coordinates[0]
      coordinate_y = coordinates[1]
      if (self.place_stone(int(coordinate_x) + 1, int(coordinate_y) + 1, 2) == 0):
        self.ai.outstanding_move(self.boardTab, self.boardSize)
    except ValueError:
      print("err: you must provide a single number argument.", flush=True, file=sys.stderr)
      return

  def board(self):
    coordinates = []
    if (self.boardSize == 0):
      return
    while(True):
      self.command = input()
      if (self.command == "DONE"):
        self.begin()
        return
      coordinates = self.command.split(',')
      if (len(coordinates) != 3):
        print("err: you must provide correct coordinates format (pos X, PosY, Player id).", flush=True, file=sys.stderr)
        continue
      self.place_stone(int(coordinates[0]) + 1, int(coordinates[1]) + 1, int(coordinates[2]))
  
  def begin(self):
    self.ai.outstanding_move(self.boardTab, self.boardSize)
  
  def handleCommand(self):
    while (True):
      try:
        self.command = input()
      except EOFError:
        exit(0)
      functionDict = {"START": self.start, "END": self.end, "TURN": self.turn, "BOARD": self.board, "PB":self.print_board, "BEGIN": self.begin, "INFO": self.info}
      commandHead = self.command.split(" ", maxsplit=1)[0]
      if (commandHead != "START" and commandHead != "END" and self.boardSize == 0):
        print("You must give a board size. Try START \'wanted_size\'", flush=True, file=sys.stderr)
        continue
      if commandHead not in functionDict.keys():
        print("err: you must provide a correct command.", flush=True, file=sys.stderr)
        continue
      functionDict[commandHead]()