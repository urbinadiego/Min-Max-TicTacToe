def check_for_winner(arr) -> bool:
    if arr[0] == arr[1] and arr[0] == arr[2]:
        return True
    return False

def check_diagonals(board) -> bool:
    #From right to left
    win = []
    for i in range(3):
        win.append(board[i][i])
    if check_for_winner(win):
        return win[0]
    win.clear()
    #from left to right
    win.append(board[0][2])
    win.append(board[1][1])
    win.append(board[2][0])
    if check_for_winner(win):
        return win[0]
    return None

def check_board(board) -> str:
    #First check both diagonals
    winner = check_diagonals(board)
    if winner:
        return winner
    return None
