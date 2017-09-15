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
        self.red_blobs = set(positions[0:12])
        self.green_blobs = set(positions[12:24])
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
        "displays the board"
        #print("Display")
        #print("RED")
        #print(self.red_blobs)
        #print("GREEN")
        #print(self.green_blobs)
        print("Red Points:" + str(len(self.red_blobs)))
        print("Green Points" + str(len(self.green_blobs)))

        for col in range(1, 7):
            for row in range(1, 7):
                position = (row, col)
                if col <= self.top_border or col >= self.bottom_border or \
                   row <= self.left_border or row >= self.right_border:
                    print('o', end=' ')
                elif position in self.red_blobs: print('R', end=' ')
                elif position in self.green_blobs: print('G', end=' ')
                else: print('.', end=' ')
            print()


    #Deber ser recursivo el update hasta que ya haya eliminado todos los bordes vacios

    def update_borders(self):
        "update the positions of the board borders"

        union_blob = self.red_blobs.union(self.green_blobs)    
        tuples_left_border = 0
        tuples_right_border = 0
        tuples_top_border = 0
        tuples_bottom_border = 0
           
        for blob in union_blob:
            x_by_tuple = blob[0]
            y_by_tuple = blob[1] 
            if x_by_tuple == self.left_border+1:
                tuples_left_border+=1
            else:
                if x_by_tuple == self.right_border-1:
                    tuples_right_border+=1
            
            if y_by_tuple == self.top_border+1:
                tuples_top_border+=1
            else:
                if y_by_tuple == self.bottom_border-1:
                    tuples_bottom_border+=1

        print("Total Tuplas")
        print("TUPLAS EN BORDE IZQUIERDO")
        print(tuples_left_border)
        print("TUPLAS EN BORDE DERECHO")
        print(tuples_right_border)
        print("TUPLAS EN BORDE SUPERIOR")
        print(tuples_top_border)
        print("TUPLAS EN BORDE INFERIOR")
        print(tuples_bottom_border)           
        
        if tuples_left_border == 0: 
            self.left_border += 1

        if tuples_right_border == 0:
            self.right_border -= 1

        if tuples_top_border == 0:
            self.top_border += 1

        if tuples_bottom_border == 0:
            self.bottom_border -= 1
        print("Nuevos Bordes")
        print("LEFT")
        print(self.left_border)
        print("RIGTH")
        print(self.right_border)
        print("UP")
        print(self.top_border)
        print("DOWN") 
        print(self.bottom_border)
         
    def move(self, color, direction):
        "moves all the blobs of a color in a direction"
        aux_blobs=set()  
        tuple_to_add = (0,0)    
        if direction == 'R':
            print("Moves Rigth")
            tuple_to_add = (1,0)                       
        elif direction == 'L':
            print("Moves Left")
            tuple_to_add = (-1,0)          
        elif direction == 'U':
            print("Moves Up")
            tuple_to_add = (0,-1)
        else:
            tuple_to_add = (0,1)
            print("Moves Down")

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
        self.update_borders()

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
        #Segun yo el to move es el color que va a mover no la accion
        for move in state.moves:
            if move == "R":
                #print("Right","Color: ", state.to_move)
                state.board.move(state.to_move,'R')
            elif move == "L":
                #print("Left","Color: ", state.to_move)
                state.board.move(state.to_move,'L')
            elif move == "U":
                #print("Up","Color: ", state.to_move)
                state.board.move(state.to_move,'U')
            else:
                #print("Down","Color: ", state.to_move)
                state.board.move(state.to_move,'D')

    def result(self, state, move):
        "returns the result of applying a move to a state" 
        #"If right, evaluate blobs disappered to the operation side"
        if move == 'R':
            #print("MOVE R")
            self.initial.board.move(self.initial.to_move,"R")     
        elif move == 'L':
            #print("Move L")
            self.initial.board.move(self.initial.to_move, "L")
        elif move == 'U':
            #print("Move U")
            self.initial.board.move(self.initial.to_move,"U")
        else:
            #print("MOVE D")
            self.initial.board.move(self.initial.to_move,"D")
        #print(state.board.red_blobs)
        return state

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        "If player 1 has not left red blobs, return -1"
        "If player 2 has not green red blobs, return 1"
        if len(state.board.red_blobs) == 0:
            return -1

        if len(state.board.green_blobs) == 0:
            return 1

        return 0    


    def terminal_test(self, state):
        #Que es estooo
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
    blobs = Blobs()
    blobs.display(blobs.initial)
    cont = 0
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


