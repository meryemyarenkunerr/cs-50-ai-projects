"""
Tic Tac Toe Player
"""

import math
from copy import copy

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
    playerX = 0
    playerO = 0

    for row in board:
        playerX += board.count(X)
        playerO += board.count(O)

    # we know that player X moves first
    if playerX > playerO:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row_index in range(3):
        for row_item_index in range(3):
            if board[row_index][row_item_index] == None:
                possible_actions.add((row_index, row_item_index))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)
    new_board = copy(board)

    row, column = action

    if board[row][column] != None:
        raise Exception
    else:
        new_board[row][column] = player_move


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for turn in (X, O):
        # check vertical
        for row in board:
            if row == [turn] * 3:
                return turn

        # check horizontal
        for col in range(3):
            column = [board[row][col] for row in range(3)]
            if column == [turn] * 3:
                return turn

        # check diagonal
        if [board[i][i] for i in range(3)] == [turn] * 3:
            return turn

        if [board[i][~i] for i in range(3)] == [turn] * 3:
            return turn
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # is there any winner?
    if winner(board) != None:
        return True

    # are there any possible moves?
    for row in board:
        if EMPTY in row:
            return False

    # no possible moves
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
