from player.selection_error import SelectionOutOFBoundsError
#This file contains player related functions

def get_row() -> int:
    try:
        row = int(input("Select a row (1:3) -> "))
        if row < 0 or row > 3:
            raise SelectionOutOFBoundsError("Invalid selection,"
            "row value must be lower than 3 and higher than 0")
        return row - 1
    except SelectionOutOFBoundsError as invalid_move:
        print(invalid_move)
    except ValueError:
        print("Invalid input!")
    except Exception:
        print("Something went wrong...")

def get_col() -> int:
    try:
        col = int(input("Select a column (1:3) -> "))
        if col < 0 or col > 3:
            raise SelectionOutOFBoundsError("Invalid selection,"
            "column value must be lower than 3 and higher than 0")
        return col - 1
    except SelectionOutOFBoundsError as invalid_move:
        print(invalid_move)
    except ValueError:
        print("Invalid input!")
    except Exception:
        print("Something went wrong...")

def get_coords() -> int:
    row_coord = get_row()
    col_coord = get_col()
    return row_coord, col_coord