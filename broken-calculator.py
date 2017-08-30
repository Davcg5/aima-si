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
		return abs(self.goal-node.state)


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
prob1 = BrokenCalculator(0,[3,9,10],60,['MUL','SUM','MINUS','DIV'])
#---------------------------------------------------------------------------------------------------#
#-----------------------SOLUCION PROBLEMA-----------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
initial_time = time.time()
goal1 = breadth_first_search(prob1)
if goal1:
	display_solution(goal1)
	print("Time to method 1 Breadth First: "+str(time.time()-initial_time))
else:
	print("Fail")
initial_time = time.time()	
goal2 = astar_search(prob1)

if goal2:
	display_solution(goal2)
	print("Time to method 2 A*: "+str(time.time()-initial_time))
else:
	print("Fail")
	
prob2 = BrokenCalculator(5,[2,4,7],100,['MUL','SUM','MINUS','AC'])
#---------------------------------------------------------------------------------------------------#
#-----------------------SOLUCION PROBLEMA-----------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
initial_time = time.time()
goal3 = breadth_first_search(prob2)
if goal3:
	display_solution(goal3)
	print("Time to method 1 Breadth First: "+str(time.time()-initial_time))
else:
	print("Fail")
initial_time = time.time()	
goal4 = astar_search(prob2)

if goal4:
	display_solution(goal4)
	print("Time to method 2 A*: "+str(time.time()-initial_time))
else:
	print("Fail")
	
