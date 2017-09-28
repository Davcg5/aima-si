#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search import genetic_search,Problem,GAState
#from numpy import (exp,sin,arange)
from math import exp,sin
import random
import copy
#import matplotlib.pyplot as plt

class StateGenetic(GAState):

	def __init__(self, genes):
		self.genes = genes

	def mate(self, other):
		"Return a new individual crossing self and other."
		c = random.randrange(len(self.genes))
		valora = self.genes[0]
		valorb = self.genes[1]
		valorc = other.genes[2]
		valord = other.genes[3]
		#self.genes[:c] + other.genes[c:]
		na = [valora,valorb,valorc,valord]
		toret = self.__class__(na)
		print("Nuevo hijo")
		print(toret.genes)
		return toret

	def mutate(self):
		"Change a few of my genes."
		print("Antes de la mutacion")
		print(self.genes)
		c = random.sample(range(0, 4), 1)[0]
		newnumber = random.sample(range(0, 16), 1)[0]
		self.genes[c] = newnumber
		valora = self.genes[0]
		valorb = self.genes[1]
		valorc = self.genes[2]
		valord = self.genes[3]

		for i in range(4):
			aux = self.genes[i]
			if c == i:
				aux = newnumber
				if c == 0:
					valora = aux
				elif c == 1:
					valorb = aux
				elif c == 2: 
					valorc = aux
				else:
					valord = aux

		t = [valora,valorb,valorc,valord]
		print("New Mutation")
		print(t)
		return self.__class__(t)

class GeneticNoLinear(Problem):

	def __init__(self,initial=StateGenetic([0,0,0,0]), meta = StateGenetic([0,0,0,0])):
		Problem.__init__(self, initial.genes, meta)
		self.initial_state = initial
		self.actions = ['A0','A1','A2','A3'] # acciones posibles
		self.data = [(2,26),(4,-1),(6,4),(8,20),(10,0),(12,2),(14,19),(16,1),(18,-4),(20,19)]
		self.error = []
		
	
	def result(self, estado, accion):
		new_state = estado.genes
		#print(new_state)
		if accion == 'A0':
			if new_state[0] < 16:
				new_state[0] += 1
				new_state[1] = 0
				new_state[2] = 0
				new_state[3] = 0
			else:
				new_state[0] = random.sample(range(0, 16), 1)[0]
				new_state[1] = 0
				new_state[2] = 0
				new_state[3] = 0
			#print(new_state)
			sg = StateGenetic(new_state)
			return sg
		elif accion == 'A1':
			if new_state[1] < 16:
				new_state[1] += 1
				new_state[0] = 0
				new_state[2] = 0
				new_state[3] = 0
			else:
				new_state[1] = random.sample(range(0, 16), 1)[0]
				new_state[3] = 0
				new_state[2] = 0
				new_state[0] = 0
			#print(new_state)
			sh = StateGenetic(new_state)
			return sh
		elif accion == 'A2':
			if new_state[2] < 16:
				new_state[2] += 1
				new_state[1] = 0
				new_state[0] = 0
				new_state[3] = 0
			else:
				new_state[2] = random.sample(range(0, 16), 1)[0]
				new_state[0] = 0
				new_state[1] = 0
				new_state[3] = 0
			#print(new_state)
			sy = StateGenetic(new_state)
			return sy
		elif accion == 'A3':
			if new_state[3] < 16 :
				new_state[3] += 1
				new_state[1] = 0
				new_state[2] = 0
				new_state[0] = 0
			else:
				new_state[3] = random.sample(range(0, 16), 1)[0]
				new_state[1] = 0
				new_state[2] = 0
				new_state[0] = 0
			#print(new_state)
			so = StateGenetic(new_state)
			return so

	def value(self, state):
		err = 0
		for x,y in self.data:
			err = err + abs(y-self.fun_nolinear(state,x))
		self.error.append(err)
		return err
	
	def fun_nolinear(self,state,x):
		a0 = state.genes[0]
		a1 = state.genes[1]
		a2 = state.genes[2]
		a3 = state.genes[3]
		f = a0 / (x * x) + a1 * exp(a2 / x) + a3 * sin(x)
		return f


nolinear = GeneticNoLinear(StateGenetic([0,0,0,0]))
state = genetic_search(nolinear, nolinear.value)
print("agg")
print(state.genes)