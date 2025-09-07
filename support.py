Cup = str
Mug = str
Piece = Cup | Mug # | here means 'or'
Board = list[list[Cup | Mug | None]]

CONNECT_NUMBER = 3
MIN_SIZE = 4
MAX_SIZE = 9

COLUMN_DISPLAY_WIDTH = 5
GRID_BORDER_CORNER = '+'
GRID_HORIZONTAL_LINE = '-'
GRID_VERTICAL_SEPARATOR = '|'

HELP_COMMAND = 'help'
QUIT_COMMAND = 'quit'
DROP_COMMAND = 'drop'

CUPS = "Cups"
MUGS = "Mugs"

WELCOME_MESSAGE = "Welcome to Mug Drop!"
COMMAND_PROMPT = ("Choose a column and a piece size"
                  " to drop your piece (Enter `help` for help message): ")

MOVE_MESSAGE = " to move."
PIECES_MESSAGE = "Available to place: "

INVALID_MOVE_MESSAGE = 'Invalid move. Please try again.'
INVALID_FORMAT_MESSAGE = 'Invalid command. Enter `help` for command format.'
INVALID_INTEGERS_MESSAGE = ('Invalid move format. Column & piece size '
                          'need to be positive single digits.')
INVALID_COLUMN_MESSAGE = 'Invalid column. Please try again.'
INVALID_SIZE_MESSAGE = 'Invalid piece size. Please try again.'
ILLEGAL_MOVE_MESSAGE = 'This move is not legal. Please try again.'

PIECE_NUM_PROMPT = "Enter the number of pieces for each player: "
BOARD_SIZE_PROMPT = "Enter the board size: "
INVALID_GAME_SETTING_MESSAGE = ("Invalid number. Enter a digit from "
                                f"{MIN_SIZE} to {MAX_SIZE}.")

HELP_MESSAGE = ('- Enter `help` to obtain help message\n'
                '- Enter `quit` to quit the game\n'
                '- To make a move, enter a column & piece size in the format: '
                '`drop {column} {size}`')

GAME_OVER_MESSAGE = "Game over, "
WIN_MESSAGE = "Win!"
DRAW_MESSAGE = "it is a draw!"

REPLAY_PROMPT = "Do you want to play again? (y/n): "