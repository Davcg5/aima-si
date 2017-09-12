#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from games import (GameState,Game, query_player, random_player, 
                    alphabeta_player,alphabeta_search, 
                    alphabeta_full_search,play_game)

#_______________________________________________________________________________
# Auxiliary functions,

class BlobsBoard(object):
    """Blobs game class to generate and manipulate boards"""
    def __init__(self):
		#~ "creates a new random 6x6 board with 12 red and 12 green Blobs"
		# board limits
	    self.left_border = 0
	    self.right_border = 7
	    self.top_border = 0
	    self.bottom_border = 7
	    self.red_blobs = None
	    self.green_blobs = None
	    self.new_random_board()

    def new_random_board(self):
        "generate 12 random positions for each Blob color on the board"
        positions = [(row,col) for row in range(1, 7) for col in range(1, 7)]
        random.shuffle(positions)
        self.red_blobs = set(positions[0:12])
        self.green_blobs = set(positions[12:24])
    
    #~ def display(self):
        #~ print("displays the board")
        #~ for row in range(1, 7):
            #~ for col in range(1, 7):
                #~ position = (row, col)
                #~ if row <= self.top_border or row >= self.bottom_border or col <= self.left_border or col >= self.right_border:
                    #~ print('o'," ")
                #~ elif position in self.red_blobs: print('R',' ')
                #~ elif position in self.green_blobs: print('G',' ')
                #~ else: print('.',' ')
            #~ print()
            
    def display(self):
        for row in range(1,7):
            blobs = []
            for col in range(1,7):
                position = (row, col)
                if row <= self.top_border or row >= self.bottom_border or\
				        col <= self.left_border or col >= self.right_border:
                   blobs.append('o')
                elif position in self.red_blobs: blobs.append('O') #red
                elif position in self.green_blobs: blobs.append('X') #green
                else: blobs.append('.')
            print(blobs)
				

    def update_borders(self):
        "update the positions of the board borders"
        # update left border: moves right on left empty columns
        # update right border: moves left on right empty columns
        # update top border: moves down on top empty rows
        # update bottom border: moves up on bottom empty rows
        raise NotImplementedError
    
    def move(self, color, direction):
        "moves all the blobs of a color in a direction"
        # move blobs of the specified color eliminating those that fall out of the board
        # eliminate corresponding blobs of the opponent
        # update borders
        raise NotImplementedError

    # other methods???
        
class Blobs(Game):
    """Play Blobs on an 6 x 6 board, with Max (first player) playing the red
    Blobs with marker 'R'.
    A state has the player to move, a cached utility, a list of moves in
    the form of the four directions (left 'L', right 'R', up 'U', and down 'D'),
    and a board, in the form of a BlobsBoard object.
    Marker is 'R' for the Red Player and 'G' for the Green Player. An empty
    position appear as '.' in the display and a 'o' represents an out of the
    board position."""

    def __init__(self):
        self.initial = GameState(to_move='R', utility=0,
                                 board=BlobsBoard(), moves=['L','R','U','D'])
        print(self.initial)

    def actions(self, state):
        "Legal moves are always all the four original directions."
        
        "Move right","Move left","Move up","Move down"
        if state.to_move == "R":
            self.result(state,(1,0))
            return
        elif state.to_move == "L":
            self.result(state,(-1,0))
            return
      
        elif state.to_move == "U":
            self.result(state,(0,1))
            return  
        else:
            self.result(state,(0,-1))
            return   
        
        #~ raise NotImplementedError

    def result(self, state, move):
        "returns the result of applying a move to a state"
        aux_tuple = []
        
        "If right, evaluate blobs disappered to the rigth side"
        if move == 'R':
            tuple_r = (0,1)
            aux_tuple = [tuple(map(lambda x, y: x + y, blob, tuple_r)) for blob in state ]
        print(aux_tuple)
        "If left, evaluate blobs disappered to the left side"
        "If up, evaluate blobs disappered to the up side"
        "If down, evaluate blobs disappered to the down side"
        raise NotImplementedError

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        "If player 1 has not left red blobs, return -1"
        "If player 2 has not green red blobs, return 1"
        
        
        raise NotImplementedError

    def terminal_test(self, state):
        "A state is terminal if it is won or there are no empty squares."
        raise NotImplementedError

    def display(self, state):
        "Displays the current state"
        raise NotImplementedError

## YOU ALSO NEED TO CREATE AN EVAL_FN AND A PLAYER FOR YOUR GAME THAT USE
## ALPHABETA_SEARCH INSTEAD OF ALPHABETA_FULL_SEARCH.
## YOU DO NOT NEED A CUTOFF_TEST BECAUSE I WILL USE DEPTHS FOR CUTTING THE
## LOOK-AHEAD SEARCH.
def main():
	juego = BlobsBoard()
	print()
	

if __name__ == "__main__":
    main()


