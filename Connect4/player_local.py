

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
        #raise NotImplementedError(f"You need to write this code first")

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

        print("It's your turn, which column do you select? [0-7]")

        while True:
            try:
                move = int(input())  # Convert input to integer
                if 0 <= move <= 7:  # Check if move is within the valid range [0-7]
                    break
                else:
                    print('Invalid input! Please enter a number between 0 and 7.')
                    
                if Connect4.check_move(move, self.id):
                    break
                else:
                    print('Invalid move!')
            except ValueError:
                print('Invalid input! Please enter a number between 0 and 7.')

        return(move)



    def visualize(self) -> None:
        """
        Visualize the current state of the Connect 4 board by printing it to the console.
        """
        board = Connect4.get_board()
        
        print('│  0  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │')
        
        print('╔═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╗')

        for i in range(13):
            if i % 2:
                print('╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣')
            
            else:
                for j in range(8):
                    print(f'║  {board[int(i/2) ,j]}  ', end ='')
                print('║')
                
        print('╚═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╝')


    def celebrate_win(self) -> None:
        """
        Celebration of Local CLI Player
        """
        # TODO
        raise NotImplementedError(f"You need to write this code first")