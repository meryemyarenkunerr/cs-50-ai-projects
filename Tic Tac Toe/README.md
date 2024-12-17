# CS50's Introduction to AI with Python Week 0
## Project 2 - Tic Tac Toe

This project involves implementing an AI to play Tic-Tac-Toe optimally using the Minimax algorithm. The goal is to create a game where you can play against the AI, and the AI will make the best possible move to either win or tie the game.

The Tic-Tac-Toe board is represented as a 3x3 grid using a list of lists. Each element of the grid can be either `X`, `O`, or `EMPTY`.

![alt text](https://cs50.harvard.edu/ai/2024/projects/0/tictactoe/images/game.png)

## Getting Started

The required files for the project must be downloaded, and the `pygame` library should be installed. There are two main files in the project: `runner.py` (runs the graphical interface) and `tictactoe.py` (contains the game logic and AI moves). All the necessary functions should be implemented in `tictactoe.py`.

## Understanding

First, variables such as `X`, `O`, and `EMPTY` are defined. The `initial_state` function returns the starting state, and the game board is represented as a 3x3 list.

## Specification

- `player(board)`: Returns which player's turn it is. Initially, `X` starts.
- `actions(board)`: Returns all valid moves that can be made on the board.
- `result(board, action)`: Applies the given move and returns a new board state.
- `winner(board)`: Determines the winner of the game.
- `terminal(board)`: Checks if the game is over.
- `utility(board)`: Returns the utility value of a terminal board (1, -1, 0).
- `minimax(board)`: Returns the optimal move using the Minimax algorithm.

Once all functions are correctly implemented, running `python runner.py` will start the game. The AI will always play optimally, and if both players play their best moves, the game will end in a tie.

! Not Finished
