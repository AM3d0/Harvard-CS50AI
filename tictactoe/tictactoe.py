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
    
    # if board is already terminal state, return any return value
    if terminal(board):
        return None
    
    # if board is empty, return X
    if board == initial_state():
        return X
    
    # calculate sum of X and O's to determine which turn is it    
    sum_x = sum(row.count(X) for row in board)
    sum_o = sum(row.count(O) for row in board)
    
    # if sum of the two are equal, then its x's turn
    if sum_x <= sum_o:
        return X
    # if sum of x is bigger than 0 then its o's turn
    else:
        return O
        
                 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # contains all possible actions
    actions = set()
    
    # iterating through complete board and once a col is empty, thats a possible action
    for i, row in enumerate(board):
        for j,col in enumerate(row):
            if col == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    # deep copy of given board
    copied_board = copy.deepcopy(board) 
    
    # check if action is an invalid move
    if copied_board[i][j] != EMPTY:
        raise Exception
    
    # get current players turn
    players_turn = player(board)
    
    
    # place x or o (depending on player turn) at the correct position
    copied_board[i][j] = players_turn

    # return updated (copy)board
    return copied_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # checking row for completion
    for row in board: 
        if row.count(X) == 3:
            return X
    for row in board: 
        if row.count(O) == 3:
            return O
        
    # checking cols for completion
    for col in range(3): # first, second and third col
        if all(board[row][col] == X for row in range(3)):
            return X
        if all(board[row][col] == O for row in range(3)):
            return O
        
    # checking diagonals for completion
    if all(board[i][i] == X for i in range(3)):
        return X
    if all(board[i][i] == O for i in range(3)):
        return O
    if all(board[i][2-i] == X for i in range(3)):
        return X
    if all(board[i][2-i] == O for i in range(3)):
        return O
    
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # if there is a winner, return true
    if winner(board) is not None:
        return True
    
    # if winner(board) is None, either tie or game not finished
    else:
        # if game not finished
        for row in board:
            if EMPTY in row:
                return False
        # else game is a tie
        return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    # if X has won the game
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    # current player
    current_player = player(board)
    
    # check, if we reached terminal state
    if terminal(board):
        return None
         
    # else, depending on which players turn it is,
    # choose either max_value or min_value function 
    
    #if X players turn, then call max_value function
    if current_player == X:
        _, best_action = maxValue(board)
    else:
        _, best_action = minValue(board)
    return best_action

def maxValue(board):
    v = -math.inf
    best_action = None
    
    # base case
    if terminal(board):
        return utility(board), None
    
    # checking all possible actions
    for action in actions(board):
        min_val, _ = minValue(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action
            
    return v, best_action
    
def minValue(board):
    v = math.inf
    best_action = None
    
    # base case
    if terminal(board):
        return utility(board), None
    
    # checking all possible actions
    for action in actions(board):
        max_val, _ = maxValue(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action
            
    return v, best_action