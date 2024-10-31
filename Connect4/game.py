import uuid
import random

from scipy.ndimage import convolve
import numpy as np


class Connect4:
    """
    Connect 4 Game Class

        Defines rules of the Game
            - what is a win
            - where can you set / not set a coin
            - how big is the playing field

        Also keeps track of the current game  
            - what is its state
            - who is the active player?

        Is used by the Coordinator
            -> executes the methods of a Game object
    """
    
    def __init__(self) -> None:
        #self.board = np.full((Player.board_height, Player.board_width), " ")
        self.board = np.full((7, 8), " ")
        self.players = [None, None]
        self.turn = [0]
        self.winner = False
        self.active_player = None


    """
    Methods to be exposed to the API later on
    """
    def get_status(self):
        """
        Get the game's status.
            - active player (id or icon)
            - is there a winner? if so who?
            - what turn is it?
        """
        return self.active_player, self.winner, self.turn
        # TODO
        #raise NotImplementedError(f"You need to write this code first")

    def register_player(self, player_id:uuid.UUID)->str:
        """ 
        Register a player with a unique ID
            Save his ID as one of the local players
        
        Parameters:
            player_id (UUID)    Unique ID

        Returns:
            icon:       Player Icon (or None if failed)
        """
        # TODO
        raise NotImplementedError(f"You need to write this code first")


    def get_board(self)-> np.ndarray:
        """ 
        Return the current board state (For Example an Array of all Elements)

        Returns:
            board
        """
        
        return self.board
        # TODO
        #raise NotImplementedError(f"You need to write this code first")


    def check_move(self, column:int, player_Id:uuid.UUID) -> bool:
        """ 
        Check move of a certain player is legal
            If a certain player can make the requested move

        Parameters:
            col (int):      Selected Column of Coin Drop
            player (str):   Player ID 
        """
                
        if self.get_board()[0,column] == ' ':
            return(True)
        else:
            return(False)
        
    """ 
    Internal Method (for Game Logic)
    """
    def __update_status(self):
        """ 
        Update all values for the status (after each successful move)
            - active player
            - active ID
            - winner
            - turn_number
        """
        """self.active_player = 
        self.active_ID =
        self.winner =
        self.turn =
        """
        # TODO
        raise NotImplementedError(f"You need to write this code first")
    

    def __detect_win(self)->bool:
        """ 
        Detect if someone has won the game (4 consecutive same pieces).
        
        Returns:
            True if there's a winner, False otherwise
        """
        # Define convolution kernels for detecting a win condition
        horizontal_group = np.array([[1, 1, 1, 1]])
        vertical_group = np.array([[1], [1], [1], [1]])
        diag_down_group = np.eye(4, dtype=int)  # Top-left to bottom-right
        diag_up_group = np.flipud(diag_down_group)  # Bottom-left to top-right

        # Check for each player if there's a winning condition
        for player in [1, 2]:
            player_board = (self.board == player).astype(int)
            print(f"player_{player}'s board:")
            print(player_board)
            print('----')

            # Check all directions using convolution for 4 in a row
            if (convolve(player_board, horizontal_group, mode="constant", cval=0) == 4).any():
                return True
            if (convolve(player_board, vertical_group, mode="constant", cval=0) == 4).any():
                return True
            if (convolve(player_board, diag_down_group, mode="constant", cval=0) == 4).any():
                return True
            if (convolve(player_board, diag_up_group, mode="constant", cval=0) == 4).any():
                return True

        # Return False if no win condition is found for either player
        return False
        # TODO
        #raise NotImplementedError(f"You need to write this code first")