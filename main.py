class Game:
    def __init__(self):
        # Initialize the board with space characters indicating empty cells
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Initialize players with default names and symbols
        self.p1 = self.Player("Player 1", "X")  # player 1
        self.p2 = self.Player("Player 2", "O")  # player 2

    # Inner class Player
    class Player:
        def __init__(self, name, symbol):
            self.name = name
            self.symbol = symbol

        def move(self, symbol):
            moved = False

            # Get x and y coordinates from user
            x = int(input("x coordinate of your move is: "))
            y = int(input("y coordinate of your move is: "))

            while(not moved):
                # Check if the move is within bounds and the cell is empty
                if 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == ' ':
                    self.board[x][y] = symbol  # Assuming 1 is for player 1's symbol
                    moved = True
                else:
                    print("Invalid move. Try again.")

    def checkCombination(self):
        """Check for a winning combination."""
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        
        return False

    def drawBoard(self):
        for i in range(3):
            row_str = ''
            for j in range(3):
                row_str += f' {self.board[i][j]} '  # Add cell content
                if j < 2:
                    row_str += '|'
            print(row_str)
            if i < 2:
                print('---+---+---')  # Separator between rows
        print()  # Newline for spacing

    def playGame(self):
        print("Starting game...")

        self.p1.name = input("Enter Player 1 name: ")
        self.p2.name = input("Enter Player 2 name: ")

        for i in range(9):
            if i % 2 == 0:
                self.move(self.p1.symbol)
                currentPlayer = self.p1.name
            else:
                self.move(self.p2.symbol)
                currentPlayer = self.p2.name

            self.drawBoard()
            if self.checkCombination():
                print(f"{currentPlayer} wins!")
                return  # End the game if there's a winner

        print("It's a draw!")

# Start game
game = Game()
game.playGame()  # This will start the game and draw the initial board