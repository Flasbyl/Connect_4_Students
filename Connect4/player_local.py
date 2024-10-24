

from game import Connect4
from player import Player


class Player_Local(Player):
    """ 
    Local Player (uses Methods of the Game directly).
    """

    def __init__(self, **kwargs) -> None:
        """ 
        Initialize a local player.
            Must Implement all Methods from Abstract Player Class

        Parameters:
            game (Connect4): Instance of Connect4 game passed through kwargs.
        
       
        """
        super().__init__()  # Initialize id and icon from the abstract Player class

       # TODO
        raise NotImplementedError(f"You need to write this code first")

    def register_in_game(self) -> str:
        """
        Register the player in the game and assign the player an icon.

        Returns:
            str: The player's icon.
        """
        # TODO
        raise NotImplementedError(f"You need to write this code first")

    def is_my_turn(self) -> bool:
        """ 
        Check if it is the player's turn.

        Returns:
            bool: True if it's the player's turn, False otherwise.
        """
        # TODO
        raise NotImplementedError(f"You need to write this code first")

    def get_game_status(self):
        """
        Get the game's current status.
            - who is the active player?
            - is there a winner? if so who?
            - what turn is it?
      
        """
        # TODO
        raise NotImplementedError(f"You need to write this code first")

    def make_move(self) -> int:

        """ 
        Prompt the physical player to enter a move via the console.

        Returns:
            int: The column chosen by the player for the move.
        """

        print("It's your turn, which column do you select? [1-8]")

        while True:
            try:
                move = int(input())  # Convert input to integer
                if 1 <= move <= 8:  # Check if move is within the valid range [1-8]
                    break
                else:
                    print('Invalid input! Please enter a number between 1 and 8.')
            except ValueError:
                print('Invalid input! Please enter a number between 1 and 8.')

        return(move)



    def visualize(self) -> None:
        """
        Visualize the current state of the Connect 4 board by printing it to the console.
        """
        # TODO
        raise NotImplementedError(f"You need to write this code first")


    def celebrate_win(self) -> None:
        """
        Celebration of Local CLI Player
        """
        # TODO
        raise NotImplementedError(f"You need to write this code first")