#Implementa una clase para resolver el problema de "Broken Calculator"
import time


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


MULTIPLICACION = 1 
SUMA = 2
RESTA = 3
DIVISION = 4	 
CONCATENACION = 5
RESET = 6

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
				elif accion == 'AC':
					acciones.append('AC')
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
		elif accion == 'AC':
			return  nuevo_estado(estado,newvalue,RESET)
			
	def h(self, node):
		hn = node.state
		gl = self.goal
		return abs(gl-hn)


def nuevo_estado(estado,nuevovalor,operacion):
	nuevoestado = 0
	if operacion == MULTIPLICACION:
		nuevoestado = estado*nuevovalor
		#~ print(nuevoestado)
		return nuevoestado
	elif operacion == SUMA:
		nuevoestado = estado+nuevovalor
		#~ print(nuevoestado)
		return nuevoestado
	elif operacion == RESTA:
		nuevoestado = estado-nuevovalor
		#~ print(nuevoestado)
		return nuevoestado
	elif operacion == DIVISION:
		nuevoestado = estado/nuevovalor
		#~ print(nuevoestado)
		return nuevoestado
	elif operacion == CONCATENACION:
		nuevoestado = float(str(estado)+str(nuevovalor))
		#~ print(nuevoestado)
		return nuevoestado
	elif operacion == RESET:
		nuevoestado = 0
		#~ print(nuevoestado)
		return nuevoestado

def despliega_solucion(nodo_meta):
	 actiones = nodo_meta.solution()
	 nodos = nodo_meta.path()
	 print("inicial: "+str(nodos[0].state))
	 for na in range(len(actiones)):
	 	print(actiones[na]+": "+str(nodos[na+1].state))

#['MUL','SUM','MINUS','DIV','CC']
prob1 = BrokenCalculator(0,[3],10002,['MUL','SUM','MINUS','DIV'])
#---------------------------------------------------------------------------------------------------#
#-----------------------SOLUCION PROBLEMA-----------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
ini = time.time()
#~ meta1 = breadth_first_search(prob1)
#~ if meta1:
	#~ despliega_solucion(meta1)
	#~ print("tiempo empleado metodo 1: "+str(time.time()-ini))
#~ else:
	#~ print("Falla")
ini = time.time()	
meta2 = astar_search(prob1)

if meta2:
	print("tiempo empleado metodo 2: "+str(time.time()-ini))
	despliega_solucion(meta2)
else:
	print("Falla")
	

