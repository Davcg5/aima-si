#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search import genetic_search,Problem,GAState
from math import exp,sin
import random
import copy

def genetic_algorithm(population, fitness_fn, ngen=1000, pmut=0.1):
    "[Figure 4.8]"
    for i in range(ngen):
        new_population = []
        for j in range(len(population)):
            fitnesses = map(fitness_fn, population)
            p1, p2 = weighted_sample_with_replacement(population, fitnesses, 2)
            child = p1.mate(p2)
            if random.uniform(0, 1) < pmut:
                child.mutate()
            new_population.append(child)
        population = new_population
    #print(population)
    #for i in range(len(population)):
    #    print(population[i].genes)
    return argmin(population, key=fitness_fn)

class StateGenetic(GAState):

	def __init__(self, genes):
		self.genes = genes[:]

	def mate(self, other):
		"Return a new individual crossing self and other."
		c = random.randrange(len(self.genes))
		cross = self.__class__(self.genes[:c] + other.genes[c:])
		return cross

	def mutate(self):
		"Change a few of my genes."
		for i in range(3):	
			s = list(self.genes)
			c = random.sample(range(0, 16), 1)[0]
			newnumber = self.genes[c]
			if newnumber == '0':
				newnumber = '1'
			else:
				newnumber = '0'
			s[c] = newnumber
			self.genes = "".join(s)
		return self.__class__(self.genes)

class GeneticNoLinear(Problem):

	def __init__(self,initial=StateGenetic('0000000000000000'), meta = StateGenetic('0000000000000000')):
		Problem.__init__(self, initial.genes, meta)
		self.initial_state = initial
		self.actions = ['A0','A1','A2','A3'] # acciones posibles
		self.data = [(2,26),(4,-1),(6,4),(8,20),(10,0),(12,2),(14,19),(16,1),(18,-4),(20,19)]
		self.error = []
		
	
	def result(self, estado, accion):
		new_state = estado.genes
		if accion == 'A0':
			#sg = StateGenetic('0001000000000100')
			sg = self.generate_individual()
			return StateGenetic(sg)
		elif accion == 'A1':
			#sh = StateGenetic('0000000100000100')
			sh = self.generate_individual()
			return StateGenetic(sh)
		elif accion == 'A2':
			#sy = StateGenetic('0000000100010000')
			sy = self.generate_individual()
			return StateGenetic(sy)
		elif accion == 'A3':
			#s = StateGenetic('0100000000000001')
			s = self.generate_individual() 
			return StateGenetic(s)
		elif accion == 'A4':
			#so = StateGenetic('1000100010001000')
			so = self.generate_individual()
			return StateGenetic(so)
		elif accion == 'A5':
			#so = StateGenetic('0100001000100000')
			so = self.generate_individual()
			return StateGenetic(so)

	def generate_individual(self):
		s  = ""
		for i in range(16):
			rannumber = random.sample(range(0, 2), 1)[0]
			s = s + str(rannumber)	
		return s

	def value(self, state):
		err = 0
		for x,y in self.data:
			err = err + abs(y-self.fun_nolinear(state,x))
		self.error.append(err)
		return err
	
	def fun_nolinear(self,state,x):
		strina0= state.genes[0:4]
		a0 = int(strina0,2)
		strina1 = state.genes[5:9]
		a1 = int(strina1,2)
		strina2 = state.genes[8:12]
		a2 = int(strina2,2)
		strina3 = state.genes[12:16]
		a3 = int(strina3,2)
		f = a0 / (x * x) + a1 * exp(a2 / x) + a3 * sin(x)
		return f


def convertir(genes):
	strina0= genes[0:4]
	a0 = int(strina0,2)
	strina1 = genes[5:9]
	a1 = int(strina1,2)
	strina2 = genes[8:12]
	a2 = int(strina2,2)
	strina3 = genes[12:16]
	a3 = int(strina3,2)
	print(a0)
	print(a1)
	print(a2)
	print(a3)

nolinear = GeneticNoLinear(StateGenetic('0000000000000000'))
state = genetic_search(nolinear, nolinear.value,1500,0.8)
print("Resultado:")
convertir(state.genes)