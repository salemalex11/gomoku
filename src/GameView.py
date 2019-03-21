# Define imports
import pygame
from pygame import *

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class View:
    """Class responsible for visually representing the game state stored in Model."""
    
    
    def __init__(self, model): 
        """Initialize a graphical representation of the given game board stored in Model."""
        
        # Initialize pygame
        pygame.init()        
        
        # Create a window
        window = [575, 575]       
             
        # Change the title of the window
        pygame.display.set_caption ("Connect Sqrt(25)")  
        
        # Set the pygame screen to be displayed in window
        self.screen = pygame.display.set_mode(window)         
                     
        self.model = model
        self.tile_size = 25     # Default tile size
        self.tile_margin = 5    # Default tile margin
        
        self.player_list = model.get_player_list()
        self.num_players = model.get_num_players()
        
        # Initialize the graphical representation
        self.update()           
        
    def get_tile_size(self):
        """Return the size of a tile for graphical representation"""
        return self.tile_size
    
    def get_tile_margin(self):
        """Return the size between tiles for graphical representation"""
        return self.tile_margin
    
    def get_model(self):
        """Return the GameModel used by GameView for graphical representation"""
        return self.model
    
    def update(self):
        """Update the graphical representation of the game"""
        
        # Reset the screen
        self.screen.fill(BLACK)
        
        for row in range(19):
            for column in range(19):
                
                # Check if empty tile
                if self.model.get_board()[row][column] == 0:
                    color = WHITE
                    
                else :   
                    for player in range(1, self.num_players + 1):
                        if self.model.get_board()[row][column] == player:
                            color = self.player_list.get(player)
                
                # Find the x coordinate of the tile
                x_coord = self.tile_margin + (
                    (self.tile_size + self.tile_margin) * column)
                
                # Find the y coordinate of the tile
                y_coord = self.tile_margin + (
                    (self.tile_size + self.tile_margin) * row)
                
                # Draw square tiles
                pygame.draw.rect(self.screen, color, 
                    [x_coord, y_coord, self.tile_size, self.tile_size])
         
        # Update pygame display
        pygame.display.flip()