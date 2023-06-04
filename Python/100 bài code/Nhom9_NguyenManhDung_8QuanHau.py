
# Kiểm tra vị trí
def check(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
 
# thử vị trí
def solve(board, row):
    if row == len(board):
        return True
    for col in range(len(board)):
        if check(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
    return False
 
#  in ra bàn cờ
def print_board(board):
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
 
board = [-1] * 8
solve(board, 0)
print_board(board)