from search import ( # Bases para construcción de problemas
    Problem, Node, Graph, UndirectedGraph,
    SimpleProblemSolvingAgentProgram,
    GraphProblem
)

from search import ( # Algoritmos de búsqueda no informada
    tree_search, graph_search, best_first_graph_search,
)


class BrokenCalculator(Problem):

    """El problema de misioneros y canibales.
   Estado: (# Misioneros en lado 1, # Canibales en lado 1, Lado de la barca)
   puede establecerse la cantidad de misioneros y caníbales involucrados"""

    def __init__(self, inicial=[2,3],meta=6):
        Problem.__init__(self, inicial, meta)
        self.acciones = ['sum','product', 'substraction','concatenate'] # acciones posibles

    def actions(self, estado):
        "Dependen de la distribución de misioneros y caníbales."
        accs = []
        for accion in self.acciones:
            if accion == 'sum':           #and not estado_ilegal(nuevo_estado(estado,1,0), self.misycan):
                accs.append('sum')
            elif accion == 'product':	  #and not estado_ilegal(nuevo_estado(estado,2,0), self.misycan):
                accs.append('product')
            elif accion == 'substraction': #and not estado_ilegal(nuevo_estado(estado,0,1), self.misycan):
                accs.append('substraction')
            elif accion == 'concatenate': #and not estado_ilegal(nuevo_estado(estado,0,1), self.misycan):
                accs.append('concatenate')
                
        return accs

    def result(self, estado, accion):
        "El resultado se calcula sumando o restando misioneros y/o caníbales."
        if accion == 'sum':
            return nuevo_estado(estado,1,0)
        elif accion == 'product':
            return nuevo_estado(estado,2,0)
        elif accion == 'substraction':
            return nuevo_estado(estado,0,1)
        elif accion == 'concatenate':
            return nuevo_estado(estado,0,2)


    def h(self, node):
        "Diferencia entre meta y estado actual"
        amis, acan, al = node.state
        gmis, gcan, gl = self.goal
        return abs(gmis-amis) + abs(gcan-acan) + abs(gl-al)
	
	def estado_ilegal(edo, misycan):
		"""Determina si un estado es ilegal"""
		return edo[0] < 0 or edo[0] > misycan or edo[1] < 0 or \
		 edo[1] > misycan or (edo[0] > 0 and edo[0] < edo[1]) or \
			   (edo[0] < misycan and edo[0] > edo[1])

        
        
        
def main()Ñ
	inicials_numbers = [2,3]
	goal_number = 6
	prob = BrokenCalculator(inicials_numbers,goal_number)

if __name__=="__main__":
	main()
