"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    if x_count == o_count:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i, j))
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy = initial_state()
    for i in range(3):
        for j in range(3):
            copy[i][j] = board[i][j]
    copy[action[0]][action[1]] = player(board)
    return copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking rows
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]
    # checking columns
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]
    # checking diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if EMPTY in board[0] or EMPTY in board[1] or EMPTY in board[2]:
        return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    return calculate(board)[1]


def calculate(board):
    if terminal(board):
        return (utility(board), None)
    if player(board) == X:
        return maxCalc(board)
    else:
        return minCalc(board)


def maxCalc(board):
    max = -(math.inf)
    current_action = []
    for action in actions(board):
        # print('max')
        # print(board)
        child_board = result(board, action)
        # print(child_board)
        current = calculate(child_board)[0]
        if current > max:
            current_action = action
            max = current
    return (max, current_action)


def minCalc(board):
    min = (math.inf)
    current_action = []
    for action in actions(board):
        # print("min")
        # print(board)
        child_board = result(board, action)
        # print(child_board)
        current = calculate(child_board)[0]
        if current < min:
            current_action = action
            min = current
    return (min, current_action)