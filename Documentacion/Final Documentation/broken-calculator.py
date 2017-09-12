#Implement a class to resolve the problem called "Broken Calculator".
#Author: A01746886 Vazquez Nava Roberto Carlos 
#		 A01746887 Villegas Felix Nicolas 

from search import ( # Bases para construcción de problemas
    Problem, Node, Graph, UndirectedGraph,
    SimpleProblemSolvingAgentProgram,
    GraphProblem
)

from search import ( # Algoritmos de búsqueda no informada
    best_first_graph_search,breadth_first_search,depth_first_graph_search
)

from search import ( # Algoritmos de búsqueda informada (heurística)
    recursive_best_first_search, astar_search
)

import time
import math

#Define CONSTANTS
MULTIPLICATION = 1 
SUM = 2
SUBTRACTION = 3
DIVISION = 4	 
CONCATENATION = 5
RESET = 6

class BrokenCalculator(Problem):
	def __init__(self,initial=0, values=[2,3],goal=20,array_actions=['MUL']):
			Problem.__init__(self,initial,goal)
			self.using_values = values
			self.count = len(self.using_values)
			self.array_actions = array_actions

	def actions(self,state):
		actions_return = []
		for i in self.using_values:
			for action in self.array_actions:
				if action == 'MUL':
					actions_return.append('MUL')
				elif action == 'SUM':
					actions_return.append('SUM')
				elif action == 'MINUS':
					actions_return.append('MINUS')
				elif action == 'DIV':
					actions_return.append('DIV')
				elif action == 'CC':
					actions_return.append('CC')
				elif action == 'AC':
					actions_return.append('AC')
		return actions_return				

	def result(self, state, action):		
		"The result is calculated by adding the previous state to the new state."
		new_value_state = self.using_values[self.count-1]
		if action == self.array_actions[len(self.array_actions)-1]:	
			self.count -= 1
			if self.count == 0:
				self.count = len(self.using_values)			
		if action == 'MUL':
			return get_new_state(state,new_value_state,MULTIPLICATION)   
		elif action == 'SUM':
			return get_new_state(state,new_value_state,SUM) 
		elif action== 'MINUS':
			return get_new_state(state,new_value_state,SUBTRACTION)  
		elif action == 'DIV':
			return get_new_state(state,new_value_state,DIVISION)
		elif action == 'CC':
			return  get_new_state(state,new_value_state,CONCATENATION)
		elif action == 'AC':
			return  get_new_state(state,new_value_state,RESET)
		
	#Heuristic		
	def h(self, node):
		# No admissible
		# h=abs((2 ** 0.5)/2-node.state/((self.goal ** 2+node.state**2))**0.5)
		# h = abs(self.goal - math.exp(node.state / 60))


		# Admissible
		# h=abs(self.goal/((1+node.state*node.state)**0.5)-(node.state/(abs(node.state)+1)))
		h= abs(math.exp(-((node.state-self.goal)**2)/ 80)-1)
		return h


def get_new_state(state,new_value,operation):
	new_state = 0
	if operation == MULTIPLICATION:
		new_state = state*new_value
		return new_state
	elif operation == SUM:
		new_state = state+new_value
		return new_state
	elif operation == SUBTRACTION:
		new_state = state-new_value
		return new_state
	elif operation == DIVISION:
		new_state = state/new_value
		return new_state
	elif operation == CONCATENATION:
		new_state = float(str(state)+str(new_value))
		return new_state
	elif operation == RESET:
		new_state = 0
		return new_state

def display_solution(goal_node):
	 actions_solution = goal_node.solution()
	 nodes = goal_node.path()
	 print("Initial: "+str(nodes[0].state))
	 for i in range(len(actions_solution)):
	 	print(actions_solution[i]+": "+str(nodes[i+1].state))

#['MUL','SUM','MINUS','DIV','CC','AC']
#---------------------------------------------------------------------------------------------------#
#-----------------------SOLUCION PROBLEMA-----------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
print("---------------A* method-------------")
actions = ['MUL','SUM','DIV']
initial_numbers = [2,3,10]
goal_numbers= [123,147,102]
for number in goal_numbers:
	prob1 = BrokenCalculator(0,initial_numbers,number,actions)
	ini = time.time()
	goal1 = astar_search(prob1)

	if goal1:
		print("Number: ",number," time: ",time.time()-ini)
		display_solution(goal1)
	else:
		print("Fail")
print("---------------Breadth First-------------")
for number in goal_numbers:
	ini = time.time()
	prob2 = BrokenCalculator(0, initial_numbers, number, actions)
	goal2 = breadth_first_search(prob2)
	if goal2:
		print("Number: ",number," time: ",time.time()-ini)
		display_solution(goal2)
	else:
		print("Fail")