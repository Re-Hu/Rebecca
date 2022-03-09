# get the position of first empty (0)
def start(sudoku):
  for x in range(4):
    for y in range(4):
      if sudoku[x][y] == 0:
        return x, y
  return False, False 

# get next empty blank in sudoku
def next(sudoku, x, y):
  for next_y in range(y+1, 4):
    if sudoku[x][next_y] == 0:
      return x, next_y
  for next_x in range(x+1, 4):
    for next_y in range(0, 4):
      if sudoku[next_x][next_y] == 0:
        return next_x, next_y
  return -1, -1
  
def value(sudoku, x, y):
  i = x//2
  j =  y//2
  grid = []
  for m in range(2):
    for n in range(2):
      grid.append(sudoku[i*2+m][j*2+n])
#  print("grid", grid)
    value = set([x for x in range(1,5)]) - set(grid) - set(sudoku[x]) - set(list(zip(*sudoku))[y])
  return list(value)

# try to fill the sudoku
def fill(sudoku, x, y):
 for i in value(sudoku, x, y):
  sudoku[x][y] = i
  next_x, next_y = next(sudoku, x, y)
  if next_y == -1:
   return True
  else:
   finish = fill(sudoku, next_x, next_y)
   if finish:
    return True
   sudoku[x][y] = 0

def solve(sudoku):  
  print("pre", sudoku)
  x, y = start(sudoku)
  fill(sudoku, x, y)
  print("solution", sudoku)
  return sudoku
 
  

     
#if __name__ == "__main__":
# m = [[2, 0, 4, 0], [3, 4, 1, 0], [0, 0, 0, 4], [4, 3, 0, 0]]
#
# solve(m)
