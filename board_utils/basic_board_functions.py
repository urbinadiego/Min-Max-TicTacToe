#Receives board-2D collection as param
def draw_board(board) -> None:
    for row in board:
        print(row)

#Receives board-2D collection as para,
def clean_board(board) -> None:
    for row in board:
        for i in range(3):
            row[i] = "-"