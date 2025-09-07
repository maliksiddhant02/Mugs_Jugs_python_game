# DO NOT modify or add any import statements
from support import *

# Name: Siddhant Malik
# Student Number: 49899155
# Favorite Tree: Apple Tree
# -----------------------------------------------------------------------------

# Define your classes and functions here


def main() -> None:
    pass

if __name__ == "__main__":
    main()

def num_hours() -> float:
    HoursSpend = 9.5
    return HoursSpend

def get_size(piece: Piece) -> int:
    if piece==None:
        return -1
    else:
        actual_size=""
        for char in piece:
            if char not in  ["(",")","/","\\"]:
                actual_size+=char
        return int(actual_size)

def generate_initial_pieces(num_pieces: int) -> tuple[list[Cup], list[Mug]]:
    Cup=[]
    Mug=[]
    all_pieces=[]
    if num_pieces!=0:
        for num in range(num_pieces):
                x=num+1
                cup_item=f"/{x}\\"
                Cup.append(cup_item)
                mug_item=f"({x})"
                Mug.append(mug_item)
    all_pieces.append(Cup)
    all_pieces.append(Mug)
    return tuple(all_pieces)

def get_piece(pieces: list[Piece], desired_size: int) -> Piece | None:
    cup_search=f"/{desired_size}\\"
    mug_search=f"({desired_size})"
    for piece in pieces:
        if piece == cup_search or piece == mug_search:
            return piece
        
def generate_initial_board(board_size: int) -> Board:
    Board=[]
    for n in range(board_size):
        rows=[None]*board_size
        Board.append(rows)
    return Board

def can_place(board: Board, column: int, piece: Piece) -> bool:
        num_piece=get_size(piece)           
        ans=True
        for chosen_column in board[::-1]:
             if chosen_column[column]==None:
                  ans=True
                  break
             else:
                 num_below = get_size(chosen_column[column])                 
                 if int(num_below)>=int(num_piece):
                      ans=False
                 else:
                      ans=True
        return ans

def drop_piece(board: Board, column: int, piece: Piece) -> None:
     if can_place(board, column, piece) == True:
        stopper=0
        num_piece=get_size(piece)   
        for chr in board[::-1]:
             if chr[column]==None and stopper == 0:
                chr[column]=piece
                
                break
             else:
                num_below = get_size(chr[column])
                if int(num_below)<int(num_piece) and stopper == 0:
                     chr[column]=piece
                     stopper+=1
                elif int(num_below)<int(num_piece):
                     chr[column]=None

def display_board(board: list[list[str]]):
    rows = 0
    for _ in board:
        rows += 1
    cols = 0
    for _ in board[0]:
        cols += 1
    print(" " + "+-----"*cols + "+")

def get_game_settings() -> tuple[int, int]:
    while True:
        num_piece=(input("Enter the number of pieces for each player: "))
        if num_piece not in ("4","5","6","7","8","9"):
            print("Invalid number. Enter a digit from 4 to 9.")
        else:
            break
    while True:
        board_size=(input("Enter the board size: "))
        if board_size not in ("4","5","6","7","8","9"):
            print("Invalid number. Enter a digit from 4 to 9.")
        else:
            break
    ans=(int(num_piece),int(board_size))
    return ans

def to_lowercase(s: str) -> str:
    lower_map={"A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g","H":"h","I":"i","J":"j","K":"k","L":"l","M":"m","N":"n","O":"o","P":"p","Q":"q","R":"r","S":"s","T":"t","U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}
    result=""
    for ch in s:
        if ch in lower_map:
            result+=lower_map[ch]
        else:
            result+=ch
    return result


def get_player_command(board: Board, available_pieces: list[Piece]) -> str:
    while True:
        user_input=input("Choose a column and a piece size to drop your piece (Enter `help` for help message): ")
        lowered=to_lowercase(user_input)
        if lowered == "help":
            return "help"
        elif lowered =="quit":
            return "quit"
        



        