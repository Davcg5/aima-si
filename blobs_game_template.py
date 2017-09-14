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
        #print("init BlobsBoard")

    def new_random_board(self):
        "generate 12 random positions for each Blob color on the board"
        positions = [(row,col) for row in range(1, 7) for col in range(1, 7)]
        random.shuffle(positions)
        self.red_blobs = set(positions[0:6])
        self.green_blobs = set(positions[6:12])
        print("ROJAS INICIALES")
        print(self.red_blobs)
        print("VERDES INICIALES")
        print(self.green_blobs)
    
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
        #print(self.red_blobs)

    def update_borders(self):
        "update the positions of the board borders"
        # update left border: moves right on left empty columns
        #Checar que no haya ningun elemento en x con valor x de left border-1
        #Si para ningun elemento en x =  0+1(LeftBorder + 1)  

        #for each 
        #print("UPDAT BORDERS")
        union_blob = self.red_blobs.union(self.green_blobs)
        longitud_rojas = len(self.red_blobs)
        longitud_verdes = len(self.green_blobs)
        #print("ROJAS")
        #print(self.red_blobs)
        #print("VERDES")
        #print(self.green_blobs)
        #print("Longitud rojas")
        #print(longitud_rojas)
        #print("Longitud Verdes")
        #print(longitud_verdes)
        #print(union_blob)
        #print("LIMITES, IZQUIERDO, DERECHO, TOP, BOTTOM")
        #print(self.left_border)
        #print(self.right_border)
        #print(self.top_border)
        #print(self.bottom_border)
        tuples_left_border = 0
        tuples_right_border = 0
        tuples_top_border = 0
        tuples_bottom_border = 0
        for blob in union_blob:
            #print("Tupla a Analizar")
           # print(blob)
            x_by_tuple = blob[0]
            y_by_tuple = blob[1]

            #print("X:" + str(x_by_tuple))
            #print("Y:" + str(y_by_tuple))
            if x_by_tuple == self.left_border+1:
                tuples_left_border+=1
            elif x_by_tuple == self.right_border-1:
                tuples_right_border+=1
            elif y_by_tuple == self.top_border+1:
                tuples_top_border+=1
            else:
                if y_by_tuple == self.bottom_border-1:
                    tuples_bottom_border+=1

        #print("Total Tuplas")
        #print("TUPLAS EN BORDE IZQUIERDO")
        #print(tuples_left_border)
        #print("TUPLAS EN BORDE DERECHO")
        #print(tuples_right_border)
        #print("TUPLAS EN BORDE SUPERIOR")
        #print(tuples_top_border)
        #print("TUPLAS EN BORDE INFERIOR")
        #print(tuples_bottom_border)

        # update right border: moves left on right empty columns

        #Checar que no haya ningun elemento en x con valor de x = right border

        # update top border: moves down on top empty rows

        #Checar que no haya ningun elemento 
        # update bottom border: moves up on bottom empty rows
        #raise NotImplementedError
 
    def move(self, color, direction):
        "moves all the blobs of a color in a direction"
        aux_blobs=set()      
        if direction == 'R':
            tuple_to_add = (1,0)
            if color == 'R':   
                for blob in self.red_blobs:  
                    new_tuple=tuple(map(lambda x, y: x + y, blob, tuple_to_add))              
                    if not (self.is_inside_border(new_tuple)):
                       continue

                    if self.exist_tuple(new_tuple,self.green_blobs):
                        aux_remain_green_tuples = set()
                        for blob in self.green_blobs:
                            x_by_tuple = blob[0] 
                            y_by_tuple = blob[1]
                            if not (x_by_tuple == new_tuple[0] and y_by_tuple == new_tuple[1]):
                                 aux_remain_green_tuples.add(blob)
                        self.green_blobs = aux_remain_green_tuples                 
                    aux_blobs.add(new_tuple)
                self.red_blobs = aux_blobs 
                print("ROJOS RESTANTES")
                print(self.red_blobs)          
                print("VERDES RESTANTES")
                print(self.green_blobs)   
            else:    
                for blob in self.green_blobs:   
                    new_tuple=tuple(map(lambda x, y: x + y, blob, tuple_to_add))         
                    if not (self.is_inside_border(new_tuple)):
                        continue
                    if self.exist_tuple(new_tuple,self.red_blobs):
                        aux_remain_tuples = set()
                        for blob in self.red_blobs:
                            x_by_tuple = blob[0] 
                            y_by_tuple = blob[1]
                            if not (x_by_tuple == new_tuple[0] and y_by_tuple == new_tuple[1]):
                                aux_remain_tuples.add(blob)
                        self.red_blobs = aux_remain_tuples              
                    aux_blobs.add(new_tuple)   
                self.green_blobs = aux_blobs
                print("ROJOS RESTANTES")
                print(self.red_blobs)          
                print("VERDES RESTANTES")
                print(self.green_blobs)                         
        elif direction == 'L':
            print("Moves Left")
            tuple_to_add = (-1,0) 
            if color == 'R':   
                print("moves Red")                
                for blob in self.red_blobs:
                    print("Old Tuple") 
                    print(blob)
                    new_tuple = tuple(map(lambda x,y: x + y,blob, tuple_to_add))             
                    if self.is_inside_border(new_tuple):
                        print("Is a valid tuple")
                    else:
                        print("Is an invalid tuple")
                    if self.exist_tuple(new_tuple,self.green_blobs):
                        print("The new tuple exist in the green blobs")
                        #So  we need to eliminate from green blobs the repeated tuple

                        print(self.green_blobs)
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
                    if self.is_inside_border(new_tuple):
                        print("Is a valid tuple")
                    else:
                        print("Is an invalid tuple")

                    if self.exist_tuple(new_tuple,self.red_blobs):
                        print("The new tuple exist in the red blobs")
                        #So  we need to eliminate from red blobs the repeated tuple
                        print(self.red_blobs)

                    print("New Tuple")
                    print(new_tuple)
                    aux_blobs.add(new_tuple)
                self.green_blobs = aux_blobs    
        elif direction == 'U':
            print("Moves Up")
            tuple_to_add = (0,-1)
            if color == 'R':   
                print("moves Red")
                for blob in self.red_blobs:
                    print("Old tuple")
                    print(blob)
                    new_tuple = tuple(map(lambda x,y: x + y,blob,tuple_to_add))             
                    if self.is_inside_border(new_tuple):
                        print("Is a valid tuple")
                    else:
                        print("Is an invalid tuple")
                    if self.exist_tuple(new_tuple,self.green_blobs):
                        print("The new tuple exist in the green blobs")
                        #So  we need to eliminate from green blobs the repeated tuple
                        print(self.green_blobs)
                    print("New tuple")
                    print(new_tuple)
                    aux_blobs.add(new_tuple)
                self.red_blobs = aux_blobs
            else:
                print("MOVES Green")
                for blob in self.green_blobs:
                    print("OLD TUPLE")
                    print(blob)
                    new_tuple = tuple(map(lambda x,y: x + y,blob,tuple_to_add))
                    if self.is_inside_border(new_tuple):
                        print("Is a valid tuple")
                    else:
                        print("Is an invalid tuple")
                    if self.exist_tuple(new_tuple,self.red_blobs):
                        print("The new tuple exist in the red blobs")
                        #So  we need to eliminate from red blobs the repeated tuple
                        print(self.red_blobs)
                    print("New tuple")
                    print(new_tuple)
                    aux_blobs.add(new_tuple)
                self.green_blobs = aux_blobs
        else:
            tuple_to_add = (0,1)
            print("Moves Down")
            if color == 'R':   
                print("moves Red")
                for blob in self.red_blobs:
                    print("old tuple")
                    print(blob)
                    new_tuple = tuple(map(lambda x,y: x+y,blob,tuple_to_add))
                    if self.is_inside_border(new_tuple):
                        print("Is a valid tuple")
                    else:
                        print("Is an invalid tuple")
                    if self.exist_tuple(new_tuple,self.green_blobs):
                        print("The new tuple exist in the green blobs")
                        #So  we need to eliminate from green blobs the repeated tuple
                        print(self.green_blobs)
                    print("NEW tuple")
                    print(new_tuple)
                    aux_blobs.add(new_tuple)
                self.red_blobs = aux_blobs   
            else:
                print("MOVES Green")
                for blob in self.green_blobs:
                    print("Old Tuple")
                    print(blob)
                    new_tuple = tuple(map(lambda x,y: x+y,blob,tuple_to_add))
                    if self.is_inside_border(new_tuple):
                        print("Is a valid tuple")
                    else:
                        print("Is an invalid tuple")
                    if self.exist_tuple(new_tuple,self.red_blobs):
                        print("The new tuple exist in the red blobs")
                        #So  we need to eliminate from red blobs the repeated tuple
                        print(self.red_blobs)
                    print("NEW tuple")
                    print(new_tuple)
                    aux_blobs.add(new_tuple)
                self.green_blobs = aux_blobs

        #
        
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
        self.update_borders()
        #raise NotImplementedError

    # other methods???
    #The function define if the tuple is in a border of the board
    def is_inside_border(self, tuple):
         x_by_tuple = tuple[0]
         y_by_tuple = tuple[1]
         if (x_by_tuple > self.left_border and x_by_tuple < self.right_border) and (y_by_tuple > self.top_border and y_by_tuple < self.bottom_border):
            #Is inside border
            return True 
         else:
            return False   

    #The function define is a tuple exist in an other list of tuples        
    def exist_tuple(self,tuple,list_tuples):
        exist = False
        for blob in list_tuples:
            if ((blob[0] == tuple[0]) and (blob[1] == tuple[1])):
                #Is the same tuple
                return True
        #The tuple do not exist in the list of tuples
        return False




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

        #print("Action in BLOB")
        #print("State to move")
        #print(state.to_move)
        if state.to_move == "R":
            legal_movements.append('R')
            self.result(state,'R')
        #MOVE GREEN  
        elif state.to_move == "G":
            legal_movements.append('R')
            self.result(state,'R')
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
        #"If right, evaluate blobs disappered to the operation side"
        if move == 'R':
            print("MOVE R")
            self.initial.board.move(self.initial.to_move,"R")     
        elif move == 'L':
            print("Move L")
            self.initial.board.move(self.initial.to_move, "L")
        elif move == 'U':
            print("Move U")
            self.initial.board.move(self.initial.to_move,"U")
        else:
            print("MOVE D")
            self.initial.board.move(self.initial.to_move,"D")
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


