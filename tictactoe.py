"""
Tic Tac Toe Player
"""

import math
import copy

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
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1

    if board == initial_state():
        return X
    if count % 2 == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                actions.add((i,j))
    if actions is None:
        return None
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    moves = actions(board)
    if action not in moves:
        raise Exception("Wrong move!")
    play = player(board)
    if play == "X":
        new_board[action[0]][action[1]] = "X"
    elif play == "O":
        new_board[action[0]][action[1]] = "O"
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (
    board[0] == ["X", "X", "X"] or
    board[1] == ["X", "X", "X"] or
    board[2] == ["X", "X", "X"] or
    [board[0][0], board[1][0], board[2][0]] == ["X", "X", "X"] or
    [board[0][1], board[1][1], board[2][1]] == ["X", "X", "X"] or
    [board[0][2], board[1][2], board[2][2]] == ["X", "X", "X"] or
    [board[0][0], board[1][1], board[2][2]] == ["X", "X", "X"] or
    [board[0][2], board[1][1], board[2][0]] == ["X", "X", "X"]
    ):
        return "X"

    elif (
    board[0] == ["O", "O", "O"] or
    board[1] == ["O", "O", "O"] or
    board[2] == ["O", "O", "O"] or
    [board[0][0], board[1][0], board[2][0]] == ["O", "O", "O"] or
    [board[0][1], board[1][1], board[2][1]] == ["O", "O", "O"] or
    [board[0][2], board[1][2], board[2][2]] == ["O", "O", "O"] or
    [board[0][0], board[1][1], board[2][2]] == ["O", "O", "O"] or
    [board[0][2], board[1][1], board[2][0]] == ["O", "O", "O"]
    ):
        return "O"
    else:
        return None


    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        if None in row:
            return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "O":
        return -1
    elif winner(board) == "X":
        return 1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]
    

def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]