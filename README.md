# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game in Python. The game is played on a 3x3 board where two players take turns to place their symbols ("X" or "O") on the board. The first player to align three of their symbols in a row, column, or diagonal wins. If all cells are filled without any player achieving this, the game ends in a draw.

## Project Structure

The project consists of a single Python class `Game` that handles the game logic, board management, and player interactions.

### Class: `Game`

- **`__init__` Method:** Initializes the game board and players.
- **`Player` Inner Class:** Represents a player with a name and symbol.
- **`move(symbol)` Method:** Allows a player to make a move by specifying coordinates. Checks if the move is valid before updating the board.
- **`checkCombination()` Method:** Checks if there is a winning combination on the board (rows, columns, or diagonals).
- **`drawBoard()` Method:** Displays the current state of the game board in a human-readable format.
- **`playGame()` Method:** Manages the game loop, takes player names, alternates turns, and checks for a winner or draw.

## How to Run

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd <project-directory>
   ```

3. **Run the Game:**

   ```bash
   python main.py
   ```

   This will start the game and prompt players to enter their names. Players will then take turns making moves until the game ends.

## Usage

1. **Player Input:**
   - When prompted, enter the `x` and `y` coordinates (0, 1, or 2) for your move.
   - Coordinates specify the row and column where you want to place your symbol.

2. **Game Flow:**
   - Players alternate turns.
   - After each move, the board is displayed.
   - The game ends when a player wins or all cells are filled (draw).

## Example

```plaintext
Starting game...
Enter Player 1 name: Alice
Enter Player 2 name: Bob
x coordinate of your move is: 0
y coordinate of your move is: 0
```

The board will be updated and displayed after each move. The game will announce the winner or a draw when the game ends.
