#Implementa una clase para resolver el problema de "Broken Calculator"

from search import ( # Bases para construcción de problemas
    Problem, Node, Graph, UndirectedGraph,
    SimpleProblemSolvingAgentProgram,
    GraphProblem
)

from search import ( # Algoritmos de búsqueda no informada
    tree_search, graph_search, best_first_graph_search,
    breadth_first_tree_search, breadth_first_search,
    depth_first_tree_search, depth_first_graph_search,
    depth_limited_search, iterative_deepening_search,
    uniform_cost_search,
    compare_searchers
)

from search import ( # Algoritmos de búsqueda informada (heurística)
    greedy_best_first_graph_search, astar_search
)

from random import randint
MULTIPLICACION = 1 
SUMA = 2
RESTA = 3
DIVISION = 4	 
CONCATENACION = 5

class BrokenCalculator(Problem):
	def __init__(self,initial=0, values=[2,3],goal=20,acciones=['MUL']):
			Problem.__init__(self,initial,goal)
			#~ self.level = level  #Level for the exercise}
			self.actualValue = 0
			self.valuesusing = values
			self.count = len(self.valuesusing)
			self.acciones = acciones
			#~ self.acciones = ['MUL','SUM','MINUS','DIV','CC']

	def actions(self,state):
		acciones = []
		for i in self.valuesusing:
			for accion in self.acciones:
				if accion == 'MUL':
					acciones.append('MUL')
				elif accion == 'SUM':
					acciones.append('SUM')
				elif accion == 'MINUS':
					acciones.append('MINUS')
				elif accion == 'DIV':
					acciones.append('DIV')
				elif accion == 'CC':
					acciones.append('CC')
		return acciones				

	def result(self, estado, accion):		
		"El resultado se calcula sumando el estado anterior con el nuevo estado."
		#~ newvalue = randint(2,3)
		newvalue = self.valuesusing[self.count-1]
		if accion == self.acciones[len(self.acciones)-1]:	
			self.count -= 1
			if self.count == 0:
				self.count = len(self.valuesusing)
			
		if accion == 'MUL':
			#~ print(accion+str(newvalue))
			return nuevo_estado(estado,newvalue,MULTIPLICACION)   
		elif accion == 'SUM':
			#~ print(accion+str(newvalue))
			return nuevo_estado(estado,newvalue,SUMA)  #donde 2 es sumar
		elif accion== 'MINUS':
			#~ print(accion+str(newvalue))
			return nuevo_estado(estado,newvalue,RESTA)  
		elif accion == 'DIV':
			#~ print(accion+str(newvalue))
			return nuevo_estado(estado,newvalue,DIVISION)
		elif accion == 'CC':
			return  nuevo_estado(estado,newvalue,CONCATENACION)


def nuevo_estado(estado,nuevovalor,operation):
	nuevoestado = 0
	if operation == MULTIPLICACION:
		nuevoestado = estado*nuevovalor
		#~ print(nuevoestado)
		return nuevoestado
	elif operation == SUMA:
		nuevoestado = estado+nuevovalor
		#~ print(nuevoestado)
		return nuevoestado
	elif operation == RESTA:
		nuevoestado = estado-nuevovalor
		#~ print(nuevoestado)
		return nuevoestado
	elif operation == DIVISION:
		nuevoestado = estado/nuevovalor
		#~ print(nuevoestado)
		return nuevoestado
	elif operation == CONCATENACION:
		nuevoestado = float(str(estado)+str(nuevovalor))
		#~ print(nuevoestado)
		return nuevoestado

def despliega_solucion(nodo_meta):
	 actiones = nodo_meta.solution()
	 nodos = nodo_meta.path()

	 for na in range(len(actiones)):
	 	print(actiones[na]+str(nodos[na].state))

#['MUL','SUM','MINUS','DIV','CC']
prob1 = BrokenCalculator(0,[2,3],19,['MUL','SUM','MINUS'])
meta1 = breadth_first_search(prob1)
if meta1:
	despliega_solucion(meta1)
else:
	print("Falla")

