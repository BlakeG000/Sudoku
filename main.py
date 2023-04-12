class Sudoku:

    def __init__(self, boardText):
        self.board = []
        if boardText is not None:
            self.parse(boardText)
        else:
            self.parse(
                ".........\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n.........")

    def __repr__(self):
        out_string = ""
        for row in self.board:
            for cell in row:
                if cell is None:
                    out_string += "."
                if cell in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    out_string += str(cell)
            out_string += "\n"
        
        out_string = out_string[:-1]
        return out_string

    def parse(self, board):
        def process_char(c):
            try:
                if int(c) in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    return int(c)
                else:
                    return None
            except ValueError:
                return None

        board = board.split('\n')

        self.board = []
        for line in board:
            self.board.append([process_char(c) for c in line])

    def poss(self,i, j):

      rowPoss = set(self.board[j])
      columnPoss = set([row[i] for row in self.board])
      e = (i//3)*3
      r = (j//3)*3
      boxPoss = set(self.board[r][e:e+3]+self.board[r+1][e:e+3]+self.board[r+2][e:e+3])
          
            
      return ((({1,2,3,4,5,6,7,8,9} - rowPoss)-columnPoss)-boxPoss)


        
    #lists start at 0
        
    def naive_solve(self):
      changed = True
      while changed:
        changed = False
        for y in range(9):
          for x in range(9):
            if self.board[y][x] is None:
              i = self.poss(x,y)
              if len(i) == 1:
                self.board[y][x] = i.pop()
                changed=True
    def solved(self):
      for y in range(9):
        for x in range(9):
          if self.board[y][x] is None:
            return False
      return True

    def unsolvable(self):
      for y in range(9):
        for x in range(9):
          if self.board[y][x] is None:
            i = self.poss(x,y)
            if len(i) == 0:
              return True
      return False
    def solver(self):
      self.naive_solve()
      if self.unsolvable() == True:
        return False
      
      if not self.solved():
        for y in range(9):
          for x in range(9):
            
            o = self.poss(x,y)
            if len(o) == 2 and self.board[y][x] is None:
              e = Sudoku(self.__repr__())
              r = Sudoku(self.__repr__())
              e.board[y][x] = o.pop()
              r.board[y][x] = o.pop()
              v = e.solver()
              if v == False:
                l = r.solver()
                self.board = l
              else:
                self.board = v
              return self.board
  
      return self.board
    
              
        
          
        
      
          

      
def main():
    testBoard = Sudoku(testBoard1)
    print(testBoard)
    #testBoard.naive_solve()
    #print(testBoard.solved())
    #print(testBoard.unsolvable())
    testBoard.solver()
    print(testBoard)


testBoard1 = """.........
456......
.2...39.1
...4..5..
.......1.
6..5.....
......8.3
.......2.
..27..4.."""

if __name__ == '__main__':
    main()