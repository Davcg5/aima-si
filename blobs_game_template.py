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
        print("init BlobsBoard")

    def new_random_board(self):
        "generate 12 random positions for each Blob color on the board"
        positions = [(row,col) for row in range(1, 7) for col in range(1, 7)]
        random.shuffle(positions)
        self.red_blobs = set(positions[0:12])
        self.green_blobs = set(positions[12:24])
    
    #def display(self):
    ##    print("displays the board")
    ###    for row in range(1, 7):
    ###        for col in range(1, 7):
    ###            position = (row, col)
    ###            if row <= self.top_border or row >= self.bottom_border or col <= self.left_border or col >= self.right_border:
    ## #               print('o'," ")
    ###            elif position in self.red_blobs: print('R',' ')
    ###            elif position in self.green_blobs: print('G',' ')
    ##            else: print('.',' ')
    #        print()
            
    def display(self):
        for row in range(1,7):
            blobs = []
            for col in range(1,7):
               position = (row, col)
               if row <= self.top_border or row >= self.bottom_border or\
                   col <= self.left_border or col >= self.right_border:
                  blobs.append('o')
               #elif position in self.red_blobs: blobs.append('O') #red
               elif position in self.green_blobs: blobs.append('X') #green
               else: blobs.append('.')
            #print(blobs)
        print(self.red_blobs)
                

    def update_borders(self):
        "update the positions of the board borders"
        # update left border: moves right on left empty columns
        # update right border: moves left on right empty columns
        # update top border: moves down on top empty rows
        # update bottom border: moves up on bottom empty rows
        raise NotImplementedError
    
    def move(self, color, direction):
        print("move in game")
        #"moves all the blobs of a color in a direction"\
        aux_blobs=set()      
        if direction == 'R':
            tuple_to_add = (1,0)
            print("Moves Rigth")
            if color == 'R': 
                print("moves Red")   
                for blob in self.red_blobs:
                    print("Old Tuple")
                    print(blob)   
                    new_tuple=tuple(map(lambda x, y: x + y, blob, tuple_to_add))
                    #Aqui debe pregunta si la nueva tupla existen en GREEN blobs entonces la eliminas de GREEN
                    #ver si no se sale del rango
                    print("New Tuple")
                    print(new_tuple)
                    aux_blobs.add(new_tuple)
                self.red_blobs = aux_blobs           
            else:
                print("MOVES Green")     
                for blob in self.green_blobs:
                    print("Old Tuple")
                    print(blob)   
                    new_tuple=tuple(map(lambda x, y: x + y, blob, tuple_to_add))
                    #Aqui debe pregunta si la nueva tupla existen en red blobs entonces la eliminas de RED
                    #ver si no se sale del rango 
                    print("New Tuple")
                    print(new_tuple)   
                    aux_blobs.add(new_tuple)
                self.green_blobs = aux_blobs      
        elif direction == 'L':
            print("Moves Left")
            tuple_to_add = (-1,0) 
            if color == 'R':   
                print("moves Red")                
                for blob in self.red_blobs:
                    print("Old Tuple") 
                    print(blob)
                    new_tuple = tuple(map(lambda x,y: x + y,blob, tuple_to_add))
                    print("New Tuple")
                    print(new_tuple)
                    aux_blobs.add(new_tuple)
                self.red_blobs = aux_blobs
            else:
                print("MOVES Green")
                for blob in self.green_blobs:
                    print("Old tuple")
                    print(blob)
                    new_tuple = tuple(map(lambda x,y: x + y, blob,tuple_to_add))
                    print("New Tuple")
                    print(new_tuple)
                    aux_blobs.add(new_tuple)
                self.green_blobs = aux_blobs    
        elif direction == 'U':
            print("Moves Up")
            if color == 'R':   
                print("moves Red")
            else:
                print("MOVES Green")
        else:
            print("Moves Down")
            if color == 'R':   
                #for blob in 
                print("moves Red")
            else:
                print("MOVES Green")
        #
        #tuple_r = (0,1)
        #for blob in state.board.green_blobs:
            
        #    if new_tuple[0]<=6 and new_tuple[1]<=6:
        #       
        #state.board.green_blobs = aux_blobs
        #print("MOVES")
        #print(color)
        #print(direction)
        # move blobs of the specified color eliminating those that fall out of the board
        # eliminate corresponding blobs of the opponent
        # update borders
        #raise NotImplementedError

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

    def actions(self, state):
        "Legal moves are always all the four original directions."
        legal_movements = []
        "Move right","Move left","Move up","Move down"
        #Segun yo el to move es el color que va a mover no la accion
            #deberia de retornar las acciones validas segun el color
        #MOVE RED
        print("Action in BLOB")
        print("State to move")
        print(state.to_move)
        if state.to_move == "R":
            legal_movements.append('R')
            self.result(state,'L')
        #MOVE GREEN  
        elif state.to_move == "G":
            legal_movements.append('R')
            self.result(state,'L')
            #self.result(state,"L")
            #return  
        #elif state.to_move == "U":
        #    legal_movements.append('U')
            #self.result(state,(0,1))
            #return  
        #else:
        #    legal_movements.append('D')
            #self.result(state,(0,-1))
            #return   
        #raise NotImplementedError
        #return legal_movements

    def result(self, state, move):
        "returns the result of applying a move to a state" 
        #"If right, evaluate blobs disappered to the rigth side"
        if move == 'R':
            print("MOVE R")
            self.initial.board.move(self.initial.to_move,"R")     
        elif move == 'L':
            print("Move L")
            self.initial.board.move(self.initial.to_move, "L")
        else:
            print("Result not valid")
        #print(state.board.red_blobs)
        return state

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
        state.board.display()
        #~ raise NotImplementedError

## YOU ALSO NEED TO CREATE AN EVAL_FN AND A PLAYER FOR YOUR GAME THAT USE
## ALPHABETA_SEARCH INSTEAD OF ALPHABETA_FULL_SEARCH.
## YOU DO NOT NEED A CUTOFF_TEST BECAUSE I WILL USE DEPTHS FOR CUTTING THE
## LOOK-AHEAD SEARCH.
def main():
    movement = Blobs()
    movement.display(movement.initial)
    state = movement.actions(movement.initial)
    #print("_______________MOVIMIENTO DERECHA_________________________")
    #movement.display(state)
    

if __name__ == "__main__":
    main()


