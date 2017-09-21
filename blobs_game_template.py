#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import copy

from games import (GameState,Game, query_player, random_player, 
                    alphabeta_player,alphabeta_search, 
                    alphabeta_full_search)

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
        self.blobs_eaten = 0
        self.blobs_deleted = 0

    def new_random_board(self):
        "generate 12 random positions for each Blob color on the board"
        positions = [(row,col) for row in range(1, 7) for col in range(1, 7)]
        random.shuffle(positions)
        self.red_blobs = set(positions[0:12])
        self.green_blobs = set(positions[12:24])
              
    def display(self):
        "displays the board"

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

    def update_borders(self):
        "update the positions of the board borders"

        union_blob = self.red_blobs.union(self.green_blobs)
        #~ print(union_blob)
        self.left_border  = min([i for i,j in union_blob])-1
        self.top_border = min([j for i,j in union_blob])-1
        self.right_border = max([i for i,j in union_blob])+1
        self.bottom_border = max([j for i,j in union_blob])+1
         
    def move(self, color, direction):
        "moves all the blobs of a color in a direction"

        if direction == 'R':
            tuple_to_add = (1,0)                       
        elif direction == 'L':
            tuple_to_add = (-1,0)          
        elif direction == 'U':
            tuple_to_add = (0,-1)
        else:
            tuple_to_add = (0,1)

        def do_move(blobs_set,blobs_compare):
            blobs_new = [tuple(map(lambda x, y: x + y, blob, tuple_to_add)) for blob in blobs_set]
            blobs_new = set([blob for blob in blobs_new if
                     (blob[0] > self.left_border and blob[0] < self.right_border and \
                      blob[1] < self.bottom_border and blob[1] > self.top_border)])
            self.blobs_deleted = len(blobs_set) - len(blobs_new)
            self.blobs_eaten = len(blobs_new & blobs_compare)
            return blobs_new

        
        if color == 'G':
            self.green_blobs = do_move(self.green_blobs, self.red_blobs)
            self.red_blobs = self.red_blobs - self.green_blobs

        else:
            self.red_blobs = do_move(self.red_blobs,self.green_blobs)
            self.green_blobs = self.green_blobs - self.red_blobs

        self.update_borders()


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
        return [move for move in ['L','R','U','D']]

    def result(self, state, move):
        "returns the result of applying a move to a state"
        
        board_copy = copy.copy(state.board)
        print("COPY")
        print(board_copy.green_blobs)
        if move == 'R':
            state.board.move(state.to_move,move)     
        elif move == 'L':
            state.board.move(state.to_move,move)
        elif move == 'U':
            state.board.move(state.to_move,move)
        else:
            state.board.move(state.to_move,move)

        #~ print("Turn: ", state.to_move)
        print("Movement: ", move)
        #~ print("original: ",state.board.green_blobs)
        #~ print("copy2: ",board_copy.green_blobs)
        state.board.display()
        #~ board_copy.display()
        return GameState(to_move=('R' if state.to_move == 'G' else 'G'),
                         utility=self.utility(state, state.to_move),
                         board=board_copy, moves=state.moves)

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        "If player 1 has not left red blobs, return -1"
        "If player 2 has not green red blobs, return 1"
        return self.heuristic(state)
        if player == "R":
            if len(state.board.red_blobs) == 0:
                return -1
            else:
                if len(state.board.green_blobs) == 0:
                    return 1

        else:
            if len(state.board.green_blobs) == 0:
                return -1
            else:
                if len(state.board.red_blobs) == 0:
                    return 1
        return 0    

    def terminal_test(self, state):
        "A state is terminal if it is won or there are no empty squares."
        if len(state.board.red_blobs) == 0 or len(state.board.green_blobs) == 0:
            print("cero")
            return True
        return False


    def display(self, state):
        "Displays the current state"
        state.board.display()
        return
        
    def to_move(self, state):
        return state.to_move
        
    def heuristic(self,state):
         h = state.board.blobs_eaten - state.board.blobs_deleted
         return h
        

## YOU ALSO NEED TO CREATE AN EVAL_FN AND A PLAYER FOR YOUR GAME THAT USE
## ALPHABETA_SEARCH INSTEAD OF ALPHABETA_FULL_SEARCH.
## YOU DO NOT NEED A CUTOFF_TEST BECAUSE I WILL USE DEPTHS FOR CUTTING THE
## LOOK-AHEAD SEARCH.

def play_game(game, *players):
    """Play an n-person, move-alternating game."""

    state = game.initial
    while True:
        for player in players:
            game.display(state)
            print("Turn:\t\t",state.to_move)
            move = player(game, state)
            #~ print("Move: \t\t",move)
            state = game.result(state, move)
            if game.terminal_test(state):
                game.display(state)
                return game.utility(state, game.to_move(game.initial))


def main():
    blob = Blobs()
    play_game(blob,alphabeta_player,query_player)
  
if __name__ == "__main__":
    main()


