import numpy

lines = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

class Board:
    def __init__(self, lines):
        self.board = []
        for line in lines:
            x = [int(line[i*3:i*3+2]) for i in range(5)]
            self.board.append(x)

    def mark(self, num):
        for x in range(5):
            for y in range(5):
                if self.board[x][y] == num:
                    self.board[x][y] = -1
                    return

    def win(self):
        for x in range(5):
            sum = 0
            for y in range(5):
                sum += self.board[x][y]
            if sum == -5:
                return True

        for y in range(5):
            sum = 0
            for x in range(5):
                sum += self.board[x][y]
            if sum == -5:
                return True

        return False

    def score(self):
        sum = 0
        for x in range(5):
            for y in range(5):
                val = self.board[x][y]
                if val > 0:
                    sum += val
        return sum

lines = open('data', 'r').read()
lines = lines.split('\n')
draw = [int(x) for x in lines[0].split(',')]
lines = lines[2:]

boards = []
while len(lines) >= 5:
    b = Board(lines[:5])
    boards.append(b)
    lines = lines[6:]

def play(boards):
    for num in draw:
        for b in boards:
            b.mark(num)
        for b in boards:
            if b.win():
                score = b.score()
                print(num, score, num*score)
                return b

while len(boards) > 0:
    b = play(boards)
    boards.remove(b)
