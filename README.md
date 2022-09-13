
## CONNECT4 Artificial Intellgence
## How To Play
Connect4 is a two player zero-sum game board game.
The players choose a color (Black or Red) and take turns dropping their colored disc into the game grid (7 col x 6 rows).
The discs fall down the chosen column to the lowest occupied space. To win the game a player must have 4 connecting discs either horizontally, vertically or diagonally.\
To run game: python3 four_in_a_row.py \
Must have tkinter module installed.
## Modes of play
Player vs. Player, Player vs. AI, AI vs AI. 
 
## A.I opponent simulation
Connect4 is a "solved game" meaning if played perfectly the first player will always win.
\
The A.I opponent has 3 playstyle options: 
* **Minmax**
 * **Minmax with alpha beta pruning**
*  **Expectimax** \
 **Depth options (For all playstyles):** Decision tree depth. (A greater depth = A more calculated opponent) 

## Minmax algorithm implementing alpha beta pruning

 ![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/AB_pruning.svg/1600px-AB_pruning.svg.png)
