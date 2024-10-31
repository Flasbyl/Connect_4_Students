from game import Connect4
from player_local import Player_Local

class Coordinator_Local:
    """ 
    Coordinator for two Local players.
    
    This class manages the game flow, player registration, turn management, 
    and game status updates for local players.
    
    Attributes:
        game (Connect4): Instance of a Connect4 game.
        player1 (Player_Local): Local instance of Player 1.
        player2 (Player_Local): Local instance of Player 2.
    """

    def __init__(self) -> None:
        """
        Initialize the Coordinator_Local with a Game and 2 Players.
        """
        self.game = Connect4()

        # Instantiate and register players
        self.player1 = Player_Local(game=self.game)
        self.player2 = Player_Local(game=self.game)
        self.player1.register_in_game()
        self.player2.register_in_game()

        # Set the initial active player to player 1
        self.game.active_player = self.player1.id

    def play(self):
        """ 
        Main function to run the game with two local players.
        
        Handles player registration, turn management, and checks for a winner 
        until the game concludes.
        """
        print("Welcome to Connect 4!")
        self.player1.visualize()  # Show the initial empty board

        while not self.game.winner:
            # Determine the active player
            current_player = self.player1 if self.game.active_player == self.player1.id else self.player2

            # Prompt the player to make a move
            column = current_player.make_move()

            # Place the move on the board if valid
            for row in range(self.game.board.shape[0] - 1, -1, -1):
                if self.game.board[row, column] == " ":
                    self.game.board[row, column] = current_player.icon
                    break

            # Visualize the board after the move
            current_player.visualize()

            # Check for a win
            self.game.winner = self.game._Connect4__detect_win()
            if self.game.winner:
                current_player.celebrate_win()
                break

            # Switch turns
            self.game.active_player = self.player2.id if self.game.active_player == self.player1.id else self.player1.id

if __name__ == "__main__":
    Game = Coordinator_Local()
    Game.play()
