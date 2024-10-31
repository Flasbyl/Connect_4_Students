from game import Connect4
from player import Player


class Player_Local(Player):
    """ 
    Local Player (uses Methods of the Game directly).
    """

    def __init__(self, game: Connect4, **kwargs) -> None:
        """ 
        Initialize a local player.
            Must Implement all Methods from Abstract Player Class

        Parameters:
            game (Connect4): Instance of Connect4 game passed through kwargs.
        """
        super().__init__()  # Initialize id and icon from the abstract Player class
        self.game = game  # Assign the game instance to self

    def register_in_game(self) -> str:
        """
        Register the player in the game and assign the player an icon.

        Returns:
            str: The player's icon.
        """
        # Example of registration: could also use "X" and "O" as icons.
        self.icon = "X" if not self.game.players[0] else "O"
        player_index = 0 if self.icon == "X" else 1
        self.game.players[player_index] = self.id  # Register player ID
        return self.icon

    def is_my_turn(self) -> bool:
        """ 
        Check if it is the player's turn.

        Returns:
            bool: True if it's the player's turn, False otherwise.
        """
        return self.game.active_player == self.id

    def get_game_status(self):
        """
        Get the game's current status.
            - who is the active player?
            - is there a winner? if so who?
            - what turn is it?
        """
        return self.game.get_status()

    def make_move(self) -> int:
        """ 
        Prompt the physical player to enter a move via the console.

        Returns:
            int: The column chosen by the player for the move.
        """
        print("It's your turn, which column do you select? [0-7]")
        while True:
            try:
                move = int(input())  # Convert input to integer
                if 0 <= move <= 7:  # Check if move is within the valid range [0-7]
                    if self.game.check_move(move, self.id):  # Use self.game to validate
                        return move
                    else:
                        print('Invalid move! Column is full or not allowed.')
                else:
                    print('Invalid input! Please enter a number between 0 and 7.')
            except ValueError:
                print('Invalid input! Please enter a number between 0 and 7.')

    def visualize(self) -> None:
        """
        Visualize the current state of the Connect 4 board by printing it to the console.
        """
        board = self.game.get_board()
        print('│  0  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │')
        print('╔═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╗')
        for i in range(13):
            if i % 2:
                print('╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣')
            else:
                for j in range(8):
                    print(f'║  {board[int(i/2), j]}  ', end='')
                print('║')
        print('╚═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╝')

    def celebrate_win(self) -> None:
        """
        Celebration of Local CLI Player.
        """
        print(f"Congratulations, Player {self.icon}! You've won!")
