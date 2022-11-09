from board_utils import basic_board_functions
from player.player_utils import get_coords

#Tic Tac Toe - urbinadiego
#Structure of the game still under review
#No Min-Max algorithm implemented as of now

#2D array
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
turn: int = 0
winner: int = 0
PLAYER1_SYMBOL: str = "X"
PLAYER2_SYMBOL: str = "O"
player_turn: int = 1 #1 by default


def start() -> None:
    global board, winner, turn, player_turn
    curr_symbol: str = ""
    while winner == 0 and turn < 9:
        basic_board_functions.draw_board(board)
        #Verify which is the player making the row, col choice
        if player_turn == 1:
            print("Player 1 turn")
            player_turn += 1
            curr_symbol = PLAYER1_SYMBOL
        else:
            print("Player 2 turn")
            player_turn -= 1
            curr_symbol = PLAYER2_SYMBOL
        #Let the player choose
        row, col = get_coords()
        board[row][col] = curr_symbol
        