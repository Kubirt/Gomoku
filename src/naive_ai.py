#!/usr/bin/env python3.10
##
## EPITECH PROJECT, 2022
## openAI
## File description:
## main
##
import random

class naive_ai():
  
  boardSize: int = 0
  boardTab: list[int]
  RIGHT: int = 1
  LEFT: int = -1
  TOP: int
  BOTTOM: int
  UPPER_RIGHT: int
  UPPER_LEFT: int
  BOTTOM_LEFT: int
  BOTTOM_RIGHT: int
  OWN: int = 1
  OPPONENT: int = 2

  def get_stones(self, field: int):
    stones = []
    for i in range(0, self.boardSize * self.boardSize):
      if (self.boardTab[i] == field):
        stones.append(i)

    return stones

  def check_dir(self, stone, field, dir):
    n = 0
    blank = 0

    stone += dir
    while (self.boardTab[stone] != -1 and n < 3):
      if (blank >= 2):
        return 0
      if (self.boardTab[stone] == field):
        n += 1
      elif (self.boardTab[stone] == 0):
        blank += 1
      else:
        return 0
      stone += dir

    if (self.boardTab[stone] != 0 and blank == 0):
      return 0

    return n

  def check_stones(self, stone, field: int):
    directions = [self.TOP, self.UPPER_RIGHT, self.RIGHT, self.BOTTOM_RIGHT, self.BOTTOM, self.BOTTOM_LEFT, self.LEFT, self.UPPER_LEFT]

    for dir in directions:
      if (self.check_dir(stone, field, dir) == 3):
        stone += dir
        while (self.boardTab[stone] != 0):
          stone += dir
        self.boardTab[stone] = 1
        print(f"{(stone) % self.boardSize - 1},{int((stone) / self.boardSize - 1)}", flush=True)
        return True

    return False

  def check_final_move(self, stones, field):
    for stone in stones:
      if (self.check_stones(stone, field) == True):
        return True

    return False

  def try_place_stone(self, stone):
    directions = [self.TOP, self.UPPER_RIGHT, self.RIGHT, self.BOTTOM_RIGHT, self.BOTTOM, self.BOTTOM_LEFT, self.LEFT, self.UPPER_LEFT]

    for dir in directions:
      if (self.boardTab[stone + dir] == 0):
        self.boardTab[stone + dir] = 1
        print(f"{(stone + dir) % self.boardSize - 1},{int((stone + dir) / self.boardSize - 1)}", flush=True)
        return True

    return False

  def reach_obstacle(self, dir, stone, opponentField):
    while((self.boardTab[stone + dir] != opponentField) and (self.boardTab[stone + dir] != -1)):
      if ((self.boardTab[stone + dir] == 0 and self.boardTab[stone + 2 * dir] == 0)):
        return stone
      stone += dir
    if (self.boardTab[stone + dir] == opponentField):
      return stone + dir
    return stone

  def get_possibilities(self, stones) -> list[int]:
    directions = [self.TOP, self.UPPER_RIGHT, self.RIGHT, self.BOTTOM_RIGHT, self.BOTTOM, self.BOTTOM_LEFT, self.LEFT, self.UPPER_LEFT]
    possibilities: list[int] = []
    for stone in stones:
      for direction in directions:
        if (self.boardTab[stone + direction] == 0):
          possibilities.append(stone + direction)
    return list(set(possibilities))
  
  def analyse_specific_case(self, fieldStones, opponentStones) -> float:
    if (opponentStones == 0):
      if (fieldStones == 1):
        return 2
      if (fieldStones == 2):
        return 4
      if (fieldStones == 3):
        return 10
    elif (opponentStones > 0):
      if fieldStones == 1 and opponentStones == 1:
        return 1
      if fieldStones == 2 and opponentStones == 1:
        return 1.3
      if fieldStones == 3 and opponentStones == 1:
        return 3.3
      if fieldStones == 1 and opponentStones == 2:
        return 0
      if fieldStones == 2 and opponentStones == 2:
        return 0
      if fieldStones == 3 and opponentStones == 2:
        return 0
    return 0

  def eval(self, possibilities, field, opponentField):
    directions: list[int] = [self.TOP, self.LEFT, self.UPPER_RIGHT, self.UPPER_LEFT]
    directions_opposed:dict[int, int] = {self.TOP:self.BOTTOM, self.LEFT:self.RIGHT, self.UPPER_RIGHT:self.BOTTOM_LEFT, self.UPPER_LEFT:self.BOTTOM_RIGHT}
    values: dict = {}
    fieldStones = 0
    opponentStones = 0

    for poss in possibilities:
      value = 0
      start_stone = 0
      for dir in directions:
        fieldStones = 0
        opponentStones = 0
        start_stone = self.reach_obstacle(dir, poss, opponentField)
        while((self.boardTab[start_stone + directions_opposed[dir]] != opponentField) and (self.boardTab[start_stone + directions_opposed[dir]] != -1)):
          if (self.boardTab[start_stone] == field):
            fieldStones += 1
          if (self.boardTab[start_stone] == opponentField):
            opponentStones += 1
          if ((self.boardTab[start_stone + directions_opposed[dir]] == 0 and self.boardTab[start_stone + 2 * directions_opposed[dir]] == 0)):
            break
          start_stone += directions_opposed[dir]
        value += self.analyse_specific_case(fieldStones, opponentStones)
      values[poss] = value
    return values
      
  def impressive_move(self, my_stones, opponent_stones, field, opponentField):
    pos = 0
    ai_eval: dict = {}
    opponent_eval: dict = {}
    my_possibilities = self.get_possibilities(my_stones)
    opponent_possibilities = self.get_possibilities(opponent_stones)


    if (len(my_stones) == 0 and self.boardTab[(int((self.boardSize) / 2) + (int((self.boardSize) / 2) * (self.boardSize)))] == 0):
      pos = (int((self.boardSize) / 2) + (int((self.boardSize) / 2) * (self.boardSize)))
      self.boardTab[pos] = 1
      print(f"{(pos) % self.boardSize - 1},{int((pos) / self.boardSize - 1)}", flush=True)
      return self.boardTab
    elif (len(my_stones) == 0):
      pos = random.randint(0, (self.boardSize) * (self.boardSize))
      while (self.boardTab[pos] != 0):
        pos = random.randint(0, (self.boardSize) * (self.boardSize))
      self.boardTab[pos] = 1
      print(f"{(pos) % self.boardSize - 1},{int((pos) / self.boardSize - 1)}", flush=True)
      return self.boardTab

    ai_eval = self.eval(my_possibilities, field, opponentField)
    opponent_eval = self.eval(opponent_possibilities, opponentField, field)

    for i in opponent_eval.keys():
      if (i not in ai_eval.keys()):
        ai_eval[i] = opponent_eval[i]
      else:
        ai_eval[i] += opponent_eval[i]
    ai_eval = {k: v for k, v in sorted(ai_eval.items(), key=lambda item: item[1], reverse=True)}
    self.boardTab[list(ai_eval.keys())[0]] = 1
    print(f"{int(list(ai_eval.keys())[0] % self.boardSize - 1)},{int(list(ai_eval.keys())[0] / self.boardSize - 1)}", flush=True)


    return self.boardTab

  def outstanding_move(self, board: list[int], size: int):
    self.boardSize = size
    self.boardTab = board

    self.TOP = -(self.boardSize)
    self.BOTTOM = +(self.boardSize)
    self.UPPER_RIGHT = -self.boardSize + 1
    self.UPPER_LEFT = -self.boardSize - 1
    self.BOTTOM_LEFT = self.boardSize - 1
    self.BOTTOM_RIGHT = self.boardSize + 1

    my_stones = self.get_stones(self.OWN)
    opponent_stones = self.get_stones(self.OPPONENT)
    if (self.check_final_move(my_stones, self.OWN) == True):
      return board
    elif (self.check_final_move(opponent_stones, self.OPPONENT) == True):
      return board
    else:
      board = self.impressive_move(my_stones, opponent_stones, self.OWN, self.OPPONENT)
    return board
