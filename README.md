# CONNECT4 Artificial Intelligence

Connect4 is a captivating two-player zero-sum board game. Players choose a color (Black or Red) and strategically drop their colored discs into the 7x6 game grid, taking turns. Discs descend to the lowest occupied space within the chosen column. Victory requires connecting four discs either horizontally, vertically, or diagonally.

## Getting Started
Ensure that the tkinter module is installed.
To run the game, use the following command:
python3 four_in_a_row.py
## Modes of Play

- Player vs. Player
- Player vs. AI
- AI vs. AI

## AI Opponent Simulation

Connect4 is a "solved game," meaning optimal play guarantees the first player's victory. The A.I opponent offers three distinct playstyle options:
### Minimax

Minimax is a decision-making algorithm used in two-player zero-sum games, such as Connect4. The goal is to choose a move that minimizes the maximum possible loss for a worst-case scenario. In the context of Connect4 AI, Minimax evaluates all possible future moves by simulating the game to a certain depth, creating a decision tree. It then selects the move that leads to the best outcome or least unfavorable result.

### Alpha-Beta Pruning

Alpha-Beta Pruning is an optimization technique applied to the Minimax algorithm to reduce the number of nodes evaluated in the search tree. It maintains two values, alpha and beta, representing the minimum score the maximizing player is assured and the maximum score the minimizing player is assured, respectively. The algorithm prunes branches of the tree that cannot influence the final decision, thus significantly improving the efficiency of the search process.

### Expectimax
Expectimax is a variation of the Minimax algorithm designed for games with elements of chance or uncertainty, where the outcome depends not only on the player's actions but also on random events. Connect4, being a deterministic game, doesn't inherently involve chance, but Expectimax can be adapted for scenarios where uncertainty or probabilistic elements are introduced.

In Expectimax, instead of considering the worst-case scenario for each move as in Minimax, the algorithm evaluates moves based on their expected values, considering the probability distribution of possible outcomes. This makes Expectimax suitable for games with chance elements, such as those involving random events or incomplete information.

## Depth Options (for all playstyles)

Fine-tune the decision tree depth for a more calculated opponent.

## Usage

Clone the repository and execute the game with the provided command.

## Contributing

If you'd like to contribute to the project, please follow the standard GitHub workflow:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## Minmax algorithm implementing alpha beta pruning

 ![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/AB_pruning.svg/1600px-AB_pruning.svg.png)
