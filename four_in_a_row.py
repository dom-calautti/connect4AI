# use math library if needed
import math,random
def get_child_boards(player, board):
    """
    Generate a list of succesor boards obtained by placing a disc 
    at the given board for a given player
   
    Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the player that will place a disc on the board
    board: the current board instance

    Returns
    -------
    a list of (col, new_board) tuples,
    where col is the column in which a new disc is placed (left column has a 0 index), 
    and new_board is the resulting board instance
    """
    res = []
    for c in range(board.cols):
        if board.placeable(c):
            tmp_board = board.clone()
            tmp_board.place(player, c)
            res.append((c, tmp_board))
    return res


def evaluate(player, board):
    """
    This is a function to evaluate the advantage of the specific player at the
    given game board.

    Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the specific player
    board: the board instance
    
    Returns
    -------
    score: float
        a scalar to evaluate the advantage of the specific player at the given
        game board
    """
    adversary = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
    # Initialize the value of scores
    # [s0, s1, s2, s3, --s4--]
    # s0 for the case where all slots are empty in a 4-slot segment
    # s1 for the case where the player occupies one slot in a 4-slot line, the rest are empty
    # s2 for two slots occupied
    # s3 for three
    # s4 for four
    score = [0]*5
    adv_score = [0]*5
    # Initialize the weights
    # [w0, w1, w2, w3, --w4--]
    # w0 for s0, w1 for s1, w2 for s2, w3 for s3
    # w4 for s4
    weights = [0, 1, 4, 16, 1000]

    # Obtain all 4-slot segments on the board
    seg = []
    invalid_slot = -1
    left_revolved = [
        [invalid_slot]*r + board.row(r) + \
        [invalid_slot]*(board.rows-1-r) for r in range(board.rows)
    ]
    right_revolved = [
        [invalid_slot]*(board.rows-1-r) + board.row(r) + \
        [invalid_slot]*r for r in range(board.rows)
    ]
    for r in range(board.rows):
        # row
        row = board.row(r) 
        for c in range(board.cols-3):
            seg.append(row[c:c+4])
    for c in range(board.cols):
        # col
        col = board.col(c) 
        for r in range(board.rows-3):
            seg.append(col[r:r+4])
    for c in zip(*left_revolved):
        # slash
        for r in range(board.rows-3):
            seg.append(c[r:r+4])
    for c in zip(*right_revolved): 
        # backslash
        for r in range(board.rows-3):
            seg.append(c[r:r+4])
    # compute score
    for s in seg:
        if invalid_slot in s:
            continue
        if adversary not in s:
            score[s.count(player)] += 1
        if player not in s:
            adv_score[s.count(adversary)] += 1
    reward = sum([s*w for s, w in zip(score, weights)])
    penalty = sum([s*w for s, w in zip(adv_score, weights)])
    return reward - penalty


def minimax(player, board, depth_limit):
    """
    Minimax algorithm with limited search depth.

    Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the player that needs to take an action (place a disc in the game)
    board: the current game board instance
    depth_limit: int
        the tree depth that the search algorithm needs to go further before stopping
    max_player: boolean

    Returns
    -------
    placement: int or None
        the column in which a disc should be placed for the specific player
        (counted from the most left as 0)
        None to give up the game
    """
    max_player = player
    placement = None
    
### Please finish the code below ##############################################
###############################################################################

    def value(player, board, depth_limit):
        if depth_limit == 0 or board.terminal():
            return {"column" : 0 , "score" : evaluate(max_player, board) }
        if player == max_player:
            return max_value(player, board, depth_limit)
        if player != max_player:
            return min_value(player, board, depth_limit)
        
        
    def max_value(player, board, depth_limit):
        next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
        # collects all valid move options
        moves = get_child_boards(player, board)
        
        # set score to minimum and best_move to default first move
        score = -math.inf
        best_move = moves[0]

        for move in moves:
            move_tuple = move
            column = move_tuple[0]
            board_copy = move_tuple[1]
            #compare previous score with new score
            max_score = max(score, value(next_player, board_copy, depth_limit-1)["score"])
            if max_score > score :
                best_move = column
                score = max_score
        
        #all move paths are traversed, return best_move and its score 
        return {"column" : best_move, "score" : score}
        
    
    def min_value(player, board, depth_limit):
        next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
        # list of tuples containing column, and board_copy (for all valid moves)
        moves = get_child_boards(player, board)
        # set score to maximum and best_move to default first move
        score = math.inf
        best_move = moves[0]
        
        for move in moves:
            move_tuple = move
            column = move_tuple[0]
            board_copy = move_tuple[1]
            
            #compare previous score with new score
            min_score = min(score, value(next_player, board_copy , depth_limit-1)["score"])
            if min_score < score :
                best_move = column
                score = min_score
        
        #all move paths are traversed, return best_move its score
        return {"column" : best_move, "score" : score}
        
    #returns column of best move
    placement = value(max_player, board, depth_limit)["column"]
###############################################################################
    
    return placement


def alphabeta(player, board, depth_limit):
    """
    Minimax algorithm with alpha-beta pruning.

     Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the player that needs to take an action (place a disc in the game)
    board: the current game board instance
    depth_limit: int
        the tree depth that the search algorithm needs to go further before stopping
    alpha: float
    beta: float
    max_player: boolean


    Returns
    -------
    placement: int or None
        the column in which a disc should be placed for the specific player
        (counted from the most left as 0)
        None to give up the game
    """
    max_player = player
    placement = None

### Please finish the code below ##############################################
###############################################################################

    def value(player, board, depth_limit, alpha, beta):
        if depth_limit == 0 or board.terminal():
            return {"column" : 0 , "score" : evaluate(max_player, board) }
        if player == max_player:
            return max_value(player, board, depth_limit, alpha, beta)
        if player != max_player:
            return min_value(player, board, depth_limit, alpha, beta)
        
        
    def max_value(player, board, depth_limit, alpha, beta):
        next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
        # collects all valid move options
        moves = get_child_boards(player, board)
        
        # set score to minimum and best_move to default first move
        score = -math.inf
        best_move = moves[0]

        for move in moves:
            move_tuple = move
            column = move_tuple[0]
            board_copy = move_tuple[1]
            #compare previous score with new score
            max_score = max(score, value(next_player, board_copy, depth_limit-1, alpha, beta)["score"])
            if max_score > score :
                best_move = column
                score = max_score
            #alpha pruning
            alpha = max(max_score, alpha)
            if alpha >= beta:
                break
        #all move paths are traversed, return best_move and its score 
        return {"column" : best_move, "score" : score}
        
    
    def min_value(player, board, depth_limit, alpha, beta):
        next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
        # list of tuples containing column, and board_copy (for all valid moves)
        moves = get_child_boards(player, board)
        # set score to maximum and best_move to default first move
        score = math.inf
        best_move = moves[0]
        
        for move in moves:
            move_tuple = move
            column = move_tuple[0]
            board_copy = move_tuple[1]
            
            #compare previous score with new score
            min_score = min(score, value(next_player, board_copy , depth_limit-1, alpha, beta)["score"])
            if min_score < score :
                best_move = column
                score = min_score
            #beta pruning
            beta = min(min_score, beta)
            if beta <= alpha:
                break
        #all move paths are traversed, return best_move its score
        return {"column" : best_move, "score" : score}
        
    #returns column of best move
    placement = value(max_player, board, depth_limit, alpha = -math.inf, beta = math.inf)["column"]
###############################################################################
    return placement


def expectimax(player, board, depth_limit):
    """
    Expectimax algorithm.
    We assume that the adversary of the initial player chooses actions
    uniformly at random.
    Say that it is the turn for Player 1 when the function is called initially,
    then, during search, Player 2 is assumed to pick actions uniformly at
    random.

    Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the player that needs to take an action (place a disc in the game)
    board: the current game board instance
    depth_limit: int
        the tree depth that the search algorithm needs to go before stopping
    max_player: boolean

    Returns
    -------
    placement: int or None
        the column in which a disc should be placed for the specific player
        (counted from the most left as 0)
        None to give up the game
    """
    max_player = player
    placement = None

### Please finish the code below ##############################################
###############################################################################

    def value(player, board, depth_limit):
        if depth_limit == 0 or board.terminal():
            return {"column" : 0 , "score" : evaluate(max_player, board) }
        if player == max_player:
            return max_value(player, board, depth_limit)
        if player != max_player:
            return min_value(player, board, depth_limit)
        
        
    def max_value(player, board, depth_limit):
        next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
        # collects all valid move options
        moves = get_child_boards(player, board)
        
        # set score to minimum and best_move to default first move
        score = -math.inf
        best_move = moves[0]

        for move in moves:
            move_tuple = move
            column = move_tuple[0]
            board_copy = move_tuple[1]
            #compare previous score with new score
            max_score = max(score, value(next_player, board_copy, depth_limit-1)["score"])
            if max_score > score :
                best_move = column
                score = max_score
        
        #all move paths are traversed, return best_move and its score 
        return {"column" : best_move, "score" : score}
        
    
    def min_value(player, board, depth_limit):
        next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
        # list of tuples containing column, and board_copy (for all valid moves)
        moves = get_child_boards(player, board)
        # set score to 0 and random_move to default first move
        average_score = 0
        random_move = random.choice (moves)
        probability = 1/len(moves) 
        print(probability)
        for move in moves:
            move_tuple = move
            column = move_tuple[0]
            board_copy = move_tuple[1]
            
            #compare previous score with new score
            average_score = average_score + (value(next_player, board_copy , depth_limit-1)["score"] * probability)
        
        #all move paths are traversed, return best_move its score
        return {"column" : random_move, "score" : average_score}
        
    #returns column of best move
    placement = value(max_player, board, depth_limit)["column"]
###############################################################################
    return placement


if __name__ == "__main__":
    from game_gui import GUI
    import tkinter

    algs = {
        "Minimax": minimax,
        "Alpha-beta pruning": alphabeta,
        "Expectimax": expectimax
    }

    root = tkinter.Tk()
    GUI(algs, root)
    root.mainloop()
