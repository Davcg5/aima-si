import random

from games import (GameState, Game, query_player, random_player, 
                    alphabeta_player, play_game,
                    alphabeta_full_search, alphabeta_search)

#_______________________________________________________________________________
# Auxiliary functions

class BlobsBoard(object):
    """Blobs game class to generate and manipulate boards"""
    def __init__(self):
        "creates a new random 6x6 board with 12 red and 12 green Blobs"
        # board limits
        self.left_border = 0
        self.right_border = 7
        self.top_border = 0
        self.bottom_border = 7
        self.red_blobs = None
        self.green_blobs = None
        self.deleted_blobs = 0
        self.eaten_blobs = 0
        self.blobs_deleted = 0
        self.new_random_board()

    def new_random_board(self):
        "generate 12 random positions for each Blob color on the board"
        positions = [(row,col) for row in range(1, 7) for col in range(1, 7)]
        random.shuffle(positions)
        self.red_blobs = set(positions[0:12])
        self.green_blobs = set(positions[12:24])

    def display(self):
        "displays the board"
        for row in range(1, 7):
            for col in range(1, 7):
                position = (row, col)
                if row <= self.top_border or row >= self.bottom_border or \
                   col <= self.left_border or col >= self.right_border:
                    print('o', end=' ')
                elif position in self.red_blobs: print('R', end=' ')
                elif position in self.green_blobs: print('G', end=' ')
                else: print('.', end=' ')
            print()

    def update_borders(self):
        "update the positions of the board borders"
        # update left border: moves right on left empty columns
        # update right border: moves left on right empty columns
        # update top border: moves down on top empty rows
        # update bottom border: moves up on bottom empty rows
        width = self.right_border-self.left_border-1
        hight = self.bottom_border-self.top_border-1
        index = [hight,width,hight,width] #index variable, revisar definicion
        union = self.red_blobs.union(self.green_blobs)
        print(union)
        print(index)
        for row in range(self.top_border+1,self.bottom_border): #1
            position = (row,self.left_border+1)
            if position in union:
                break
            else:
                index[0] -= 1
        for row in range(self.top_border+1,self.bottom_border): #3
            position = (row,self.right_border-1)
            if position in union:
                break
            else:
                index[2] -= 1
        for colum in range(self.left_border+1,self.right_border): #4
            position = (self.top_border+1,colum)
            if position in union:
                break
            else:
                index[3] -= 1
        for colum in range(self.left_border+1,self.right_border): #2
            position = (self.bottom_border-1,colum)
            if position in union:
                break
            else:
                index[1] -= 1
                print(index[1])
                
        if index[0] == 0:
            self.left_border += 1
        if index[1] == 0:
            self.bottom_border -= 1
        if index[2] == 0:
            self.right_border -= 1
        if index[3] == 0:
            self.top_border += 1

        print("Blobs eaten: ", self.eaten_blobs)
        print("Blobs deleted: ",self.blobs_deleted)               
        return


			
    
    def move(self, color, direction):
        "moves all the blobs of a color in a direction"
        # move blobs of the specified color eliminating those that fall out of the board
        # eliminate corresponding blobs of the opponent
        # update borders
        self.deleted_blobs = 0
        self.eaten_blobs = 0        
        if color == 'G':
            blobs_turn = self.green_blobs
            blobs_opponent = self.red_blobs
        else:
            blobs_turn = self.red_blobs
            blobs_opponent = self.green_blobs
            
        blobs_aux=set()
		
        for blob in blobs_turn:
            new_tuple = tuple(map(lambda x, y: x + y, blob, direction))
            if new_tuple[0]<self.right_border and \
                       new_tuple[0]>self.left_border and \
							   new_tuple[1]<self.bottom_border and \
							         new_tuple[1]>self.top_border:
                blobs_aux.add(new_tuple)
            else:
                self.blobs_deleted += 1
                
        for blob in blobs_aux:
            if blob in blobs_opponent:
                self.eaten_blobs += 1
                blobs_opponent.discard(blob)
         
        print(blobs_opponent)
        print(blobs_aux) 
        if color == 'G':
            self.green_blobs = blobs_aux
            self.red_blobs = blobs_opponent 
        else:
            self.red_blobs = blobs_aux
            self.green_blobs = blobs_opponent
        self.update_borders()
        return
        
        
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

    def actions(self, state):
        "Legal moves are always all the four original directions."
        for move in state.moves:
            if move == "R":
                print("Right","Color: ", state.to_move)
                state.board.move(state.to_move,(0,1))
            elif move == "L":
                print("Left","Color: ", state.to_move)
                state.board.move(state.to_move,(0,-1))
            elif move == "U":
                print("Up","Color: ", state.to_move)
                state.board.move(state.to_move,(-1,0))
            else:
                print("Down","Color: ", state.to_move)
                state.board.move(state.to_move,(1,0))

    def result(self, state, move):
        "returns the result of applying a move to a state"
        raise NotImplementedError

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        
        raise NotImplementedError

    def terminal_test(self, state):
        "A state is terminal if it is won or there are no empty squares."
        raise NotImplementedError

    def display(self, state):
        "Displays the current state"
        state.board.display()
        return

## YOU ALSO NEED TO CREATE AN EVAL_FN AND A PLAYER FOR YOUR GAME THAT USE
## ALPHABETA_SEARCH INSTEAD OF ALPHABETA_FULL_SEARCH.
## YOU DO NOT NEED A CUTOFF_TEST BECAUSE I WILL USE DEPTHS FOR CUTTING THE
## LOOK-AHEAD SEARCH.

def main():
    blobs = Blobs()
    blobs.display(blobs.initial)
    cont = 1
    while True:
        print("Proximo Movimiento: ")
        mov = input()
        if cont == 1:
            cont = 0
            turn = 'G'
            letra = 'VERDE'
        else:
            cont = 1
            turn = 'R'
            letra = 'ROJO'
			
        blobs.initial = GameState(to_move=turn, utility=0,
                   board=blobs.initial.board, moves=[mov])
        print("_______________"+letra+"_________________________")
        blobs.actions(blobs.initial)
        blobs.display(blobs.initial)                      
	

if __name__ == "__main__":
    main()


