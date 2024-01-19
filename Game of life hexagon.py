#%%

def Find_1s(matrix):
    alive = {}
    for row in range(0,len(matrix)):
        for column in range(0, len(matrix)):
          if matrix[row][column] == 1:
            alive[row, column] = 0
    return alive

def topLeftCoo(i, j, n, matrix):
  if i == 0:
    if j == 0:
      if matrix[l][l] == n:
        return l, l
      else:
        return 0
    else:
      if matrix[l][j-1] == n:
        return l, j-1
      else:
        return 0
  elif j == 0:
    if matrix[i-1][l] == n:
      return i-1, l
    else:
      return 0
  else:
    if matrix[i-1][j-1] == n:
     return i-1, j-1
    else:
     return 0

def topMidCoo(i, j, n, matrix):
  if i == 0:
    if matrix[l][j] == n:
      return l, j
    else:
      return 0
  else:
    if matrix[i-1][j] == n:
     return i-1, j
    else:
      return 0

def topRightCoo(i, j, n, matrix):
  if i == 0:
    if j == l:
      if matrix[l][0] == n:
        return l, 0
      else:
        return 0
    else:
      if matrix[l][j+1] == n:
        return l, j+1
      else:
        return 0
  elif j == l:
    if matrix[i-1][0] == n:
      return i-1, 0
    else:
      return 0
  else:
    if matrix[i-1][j+1] == n:
     return i-1, j+1
    else:
     return 0

def midLeftCoo(i, j, n, matrix):
  if j == 0:
    if matrix[i][l]:
      return i, l
    else:
      return 0
  else:
    if matrix[i][j-1] == n:
     return i, j-1
    else:
      return 0

def midRightCoo(i, j, n, matrix):
  if j == l:
    if matrix[i][0] == n:
      return i, 0
    else:
      return 0
  else:
    if matrix[i][j+1] == n:
     return i, j+1
    else:
     return 0

def botLeftCoo(i, j, n, matrix):
  if i == l:
    if j == 0:
      if matrix[0][l] == n:
        return 0, l
      else:
        return 0
    else:
      if matrix[0][j-1] == n:
        return 0, j-1
      else:
        return 0
  elif j == 0:
    if matrix[i+1][l] == n:
      return i+1, l
    else:
      return 0
  else:
    if matrix[i+1][j-1] == n:
     return i+1, j-1
    else:
     return 0

def botMidCoo(i, j, n, matrix):
  if i == l:
    if matrix[0][j] == n:
      return 0, j
    else:
      return 0
  else:
    if matrix[i+1][j] == n:
      return i+1, j
    else:
      return 0

def botRightCoo(i, j, n, matrix):
  if i == l:
    if j == l:
      if matrix[0][0] == n:
        return 0, 0
      else:
        return 0
    else:
      if matrix[0][j+1] == n:
        return 0, j+1
      else:
        return 0
  elif j == l:
    if matrix[i+1][0] == n:
      return i+1, 0
    else:
      return 0
  else:
    if matrix[i+1][j+1] == n:
     return i+1, j+1
    else:
     return 0

def countNeighbours(dictOfAlive, matrix):
  for key in dictOfAlive:
    keyStr = str(key)
    if len(keyStr) == 6:
        i = int(keyStr[1])
        j = int(keyStr[4])
    elif len(keyStr) == 8:
        i = int(keyStr[1] + keyStr[2])
        j = int(keyStr[5] + keyStr[6])
    elif len(keyStr) == 7:
        if keyStr[2] != ',':
            i = int(keyStr[1] + keyStr[2])
            j = int(keyStr[5])
        else:
            i = int(keyStr[1])
            j = int(keyStr[4] + keyStr[5])
    if i%2 == 0:
        if not(topLeftCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(topMidCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(midLeftCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(midRightCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(botLeftCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(botMidCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
    else:
        if not(topMidCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(topRightCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(midLeftCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(midRightCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(botMidCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
        if not(botRightCoo(i, j, 1, A) == 0):
          dictOfAlive[key] += 1
  return dictOfAlive

def zerosNextTo1s(dictOfAlive, matrix):
  dictOfZeros = {}
  for key in dictOfAlive:
    keyStr = str(key)
    if len(keyStr) == 6:
        i = int(keyStr[1])
        j = int(keyStr[4])
    elif len(keyStr) == 8:
        i = int(keyStr[1] + keyStr[2])
        j = int(keyStr[5] + keyStr[6])
    elif len(keyStr) == 7:
        if keyStr[2] != ',':
            i = int(keyStr[1] + keyStr[2])
            j = int(keyStr[5])
        else:
            i = int(keyStr[1])
            j = int(keyStr[4] + keyStr[5])
    if i%2 == 0:
        if not(topLeftCoo(i, j, 0, matrix) == 0):
          if not(topLeftCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[topLeftCoo(i, j, 0, matrix)] = 0
        if not(topMidCoo(i, j, 0, matrix) == 0):
          if not(topMidCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[topMidCoo(i, j, 0, matrix)] = 0
        if not(midLeftCoo(i, j, 0, matrix) == 0):
          if not(midLeftCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[midLeftCoo(i, j, 0, matrix)] = 0
        if not(midRightCoo(i, j, 0, matrix) == 0):
          if not(midRightCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[midRightCoo(i, j, 0, matrix)] = 0
        if not(botLeftCoo(i, j, 0, matrix) == 0):
          if not(botLeftCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[botLeftCoo(i, j, 0, matrix)] = 0
        if not(botMidCoo(i, j, 0, matrix) == 0):
          if not(botMidCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[botMidCoo(i, j, 0, matrix)] = 0
    else:
        if not(topMidCoo(i, j, 0, matrix) == 0):
          if not(topMidCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[topMidCoo(i, j, 0, matrix)] = 0
        if not(topRightCoo(i, j, 0, matrix) == 0):
          if not(topRightCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[topRightCoo(i, j, 0, matrix)] = 0
        if not(midLeftCoo(i, j, 0, matrix) == 0):
          if not(midLeftCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[midLeftCoo(i, j, 0, matrix)] = 0
        if not(midRightCoo(i, j, 0, matrix) == 0):
          if not(midRightCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[midRightCoo(i, j, 0, matrix)] = 0
        if not(botMidCoo(i, j, 0, matrix) == 0):
          if not(botMidCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[botMidCoo(i, j, 0, matrix)] = 0
        if not(botRightCoo(i, j, 0, matrix) == 0):
          if not(botRightCoo(i, j, 0, matrix) in dictOfZeros.keys()):
            dictOfZeros[botRightCoo(i, j, 0, matrix)] = 0
  return dictOfZeros

def nextGeneration1s(matrix, dictOfAlive):
  for key in dictOfAlive:
    keyStr = str(key)
    if len(keyStr) == 6:
        i = int(keyStr[1])
        j = int(keyStr[4])
    elif len(keyStr) == 8:
        i = int(keyStr[1] + keyStr[2])
        j = int(keyStr[5] + keyStr[6])
    elif len(keyStr) == 7:
        if keyStr[2] != ',':
            i = int(keyStr[1] + keyStr[2])
            j = int(keyStr[5])
        else:
            i = int(keyStr[1])
            j = int(keyStr[4] + keyStr[5])
    if dictOfAlive[i, j] < 2:
      matrix[i][j] = 0
    if dictOfAlive[i, j] >= 3:
      matrix[i][j] = 0
  return matrix

def nextGeneration0s(matrix,dictOfZeros):
  for key in dictOfZeros:
    keyStr = str(key)
    if len(keyStr) == 6:
        i = int(keyStr[1])
        j = int(keyStr[4])
    elif len(keyStr) == 8:
        i = int(keyStr[1] + keyStr[2])
        j = int(keyStr[5] + keyStr[6])
    elif len(keyStr) == 7:
        if keyStr[2] != ',':
            i = int(keyStr[1] + keyStr[2])
            j = int(keyStr[5])
        else:
            i = int(keyStr[1])
            j = int(keyStr[4] + keyStr[5])
    if dictOfZeros[i, j] == 3:
      matrix[i][j] = 1
  return matrix

def newDictOf1s(matrix, dictOfAlive, dictOfZeros):
  dictOf1s = {}
  for key in dictOfZeros:
    keyStr = str(key)
    if len(keyStr) == 6:
        i = int(keyStr[1])
        j = int(keyStr[4])
    elif len(keyStr) == 8:
        i = int(keyStr[1] + keyStr[2])
        j = int(keyStr[5] + keyStr[6])
    elif len(keyStr) == 7:
        if keyStr[2] != ',':
            i = int(keyStr[1] + keyStr[2])
            j = int(keyStr[5])
        else:
            i = int(keyStr[1])
            j = int(keyStr[4] + keyStr[5])
    if dictOfZeros[i, j] == 3:
      dictOf1s[i, j] = 0
  for key in dictOfAlive:
    keyStr = str(key)
    if len(keyStr) == 6:
        i = int(keyStr[1])
        j = int(keyStr[4])
    elif len(keyStr) == 8:
        i = int(keyStr[1] + keyStr[2])
        j = int(keyStr[5] + keyStr[6])
    elif len(keyStr) == 7:
        if keyStr[2] != ',':
            i = int(keyStr[1] + keyStr[2])
            j = int(keyStr[5])
        else:
            i = int(keyStr[1])
            j = int(keyStr[4] + keyStr[5])
    if dictOfAlive[i, j] == 2 or dictOfAlive[i, j] == 3:
      dictOf1s[i, j] = 0
  return dictOf1s

def runGame(matrix, matrixOfZeros, nGenerations):
  for i in range(0, len(matrix)):
        if not(i%2 == 0):
            print('  ', end='')
            print(matrix[i])
        else:
            print(matrix[i])
  print()
  for counter in range(0, nGenerations):
    alive = Find_1s(matrix)
    alive = countNeighbours(alive, matrix)
    kids = zerosNextTo1s(alive, matrix)
    kids = countNeighbours(kids, matrix)
    A = nextGeneration1s(matrix, alive)
    A = nextGeneration0s(matrix, kids)
    for i in range(0, len(matrix)):
        if not(i%2 == 0):
            print('  ', end='')
            print(matrix[i])
        else:
            print(matrix[i])
    print()
    if A == matrixOfZeros:
      print('GAME OVER')
      print('All cells are dead!')
      break

def checkFor1s(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] == 1:
                return True
    return False

def runGameGenCount2(matrix):
  counter = 0
  while(True):
    alive = Find_1s(matrix)
    alive = countNeighbours(alive, matrix)
    kids = zerosNextTo1s(alive, matrix)
    kids = countNeighbours(kids, matrix)
    matrix = nextGeneration1s(matrix, alive)
    matrix = nextGeneration0s(matrix, kids)
    if checkFor1s(matrix) == False:
      print(counter)
      return counter
    else:
      if counter%2 == 0:
        matrix_old = matrix
      elif counter%2 != 0:
        if matrix == matrix_old:
          print('lol')
          print(counter)
          return counter


def runGameGenCount(matrix, matrixOfZeros):
  counter = 0
  while(True):
    alive = Find_1s(matrix)
    alive = countNeighbours(alive, matrix)
    kids = zerosNextTo1s(alive, matrix)
    kids = countNeighbours(kids, matrix)
    matrix = nextGeneration1s(matrix, alive)
    matrix = nextGeneration0s(matrix, kids)
    counter += 1
    if matrix == matrixOfZeros:
      break
    if counter == 400:
      print()
      for i in range(0, len(matrix)):
        print(matrix[i])
      return 0
  return counter

'''
A = testGeneration
l = len(A) - 1
alive = {}
kids = {}
runGame(A, matrixOfZeros, 10)
'''

#code for choosing the density of the living cells
import numpy as np
import random

#This is a modified version of the density function that will wwork better with the game of life part of the code
def density_loop(r,z, percent):
  matrix = np.zeros(r*z)
  #makes an array that is one line of continuous zeroes

  list_order = []

  i = 0
  while i < len(matrix):
    list_order.append(i)
    i += 1
  #makes a list of number 0 to however many entries in the matrix there are

  random.shuffle(list_order)
  #randomly orders the number in the list
  init_density = percent
  init_life = init_density/100*len(matrix)
  #takes as input how many of the cells should be initially on
  a = 0
  while a < init_life:
    matrix[list_order[a]] = 1
    a += 1
    
    #takes the numbers from the star of the list and puts a one in those spots of the matrix
  return matrix.reshape(r,z).tolist()

#Dictionary that will store values
results = {}
N_dimensions = 10
gap = 10
Zeros = density_loop(N_dimensions, N_dimensions, 0)

#create entries in the dictionary
#We put increments of 10% on density because the code takes a long time to run
for i in range(0, 100, gap):
  results[i] = 0


#Loop that will loop the game for all densities from 1 to 100 with increments of 10. It will run this 100 times
for counter2 in range(0, 10):
  for dens_percent in range(0, 100,gap):
    A = density_loop(N_dimensions, N_dimensions, dens_percent)
    for i in range(0,N_dimensions):
      for j in range(0, N_dimensions):
        A[i][j] = int(A[i][j])
    l = len(A) - 1
    n = runGameGenCount(A, Zeros)
    if n!=0:
      print(n)
    results[dens_percent] = results[dens_percent] + n

print(results)

import matplotlib.pyplot as plt

x = list(results.keys())
y = list(results.values())

plt.plot(x, y)
