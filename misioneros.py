# Implementa una clase para resolver el problema de "Misioneros y Caníbales"
# Incluye ejemplos de su uso para resolverlo mediante el algoritmo
# de búsqueda primero en anchura
#
# Autor: Dr. Santiago Enrique Conant Pablos
# Fecha: 24 de agosto de 2016

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

class MisionerosYCanibales(Problem):

    """El problema de misioneros y canibales.
   Estado: (# Misioneros en lado 1, # Canibales en lado 1, Lado de la barca)
   puede establecerse la cantidad de misioneros y caníbales involucrados"""

    def __init__(self, inicial=(3,3,1), meta=(0,0,0), myc=3):
        Problem.__init__(self, inicial, meta)
        self.misycan = myc # No. de misioneros = No. de caníbales
        self.acciones = ['M1M','M2M','M1C','M2C','M1M1C'] # acciones posibles
      

    def actions(self, estado):
        "Dependen de la distribución de misioneros y caníbales."
        accs = []
        print("actions")
        for accion in self.acciones:
            if accion == 'M1M' and \
               not estado_ilegal(nuevo_estado(estado,1,0), self.misycan):
                accs.append('M1M')
            elif accion == 'M2M' and \
                 not estado_ilegal(nuevo_estado(estado,2,0), self.misycan):
                accs.append('M2M')
            elif accion == 'M1C' and \
                 not estado_ilegal(nuevo_estado(estado,0,1), self.misycan):
                accs.append('M1C')
            elif accion == 'M2C' and \
                 not estado_ilegal(nuevo_estado(estado,0,2), self.misycan):
                accs.append('M2C')
            elif accion == 'M1M1C' and \
                 not estado_ilegal(nuevo_estado(estado,1,1), self.misycan):
                accs.append('M1M1C')
        return accs

    def result(self, estado, accion):
        "El resultado se calcula sumando o restando misioneros y/o caníbales."
        if accion == 'M1M':
            return nuevo_estado(estado,1,0)
        elif accion == 'M2M':
            return nuevo_estado(estado,2,0)
        elif accion == 'M1C':
            return nuevo_estado(estado,0,1)
        elif accion == 'M2C':
            return nuevo_estado(estado,0,2)
        elif accion == 'M1M1C':
            return nuevo_estado(estado,1,1)

    def h(self, node):
        "Diferencia entre meta y estado actual"
        amis, acan, al = node.state
        gmis, gcan, gl = self.goal
        return abs(gmis-amis) + abs(gcan-acan) + abs(gl-al)

def nuevo_estado(edo, mis, can):
    """Mueve mis misioneros y can caníbales para obtener un nuevo estado.
       El estado resultante no se verifica (puede ser inválido)"""
    nedo = list(edo)
    if nedo[2] == 0:
        nedo[2] = 1
    else:
        mis = - mis
        can = - can
        nedo[2] = 0
    nedo[0] = nedo[0] + mis
    nedo[1] = nedo[1] + can
    return tuple(nedo)
    
def estado_ilegal(edo, misycan):
    """Determina si un estado es ilegal"""
    return edo[0] < 0 or edo[0] > misycan or \
           edo[1] < 0 or edo[1] > misycan or \
           (edo[0] > 0 and edo[0] < edo[1]) or \
           (edo[0] < misycan and edo[0] > edo[1])

def despliega_solucion(nodo_meta):
    """Despliega la secuencia de estados y acciones de una solución"""
    acciones = nodo_meta.solution()
    nodos = nodo_meta.path()
    print('SOLUCION:')
    print('Estado:',nodos[0].state)
    for na in range(len(acciones)):
        if acciones[na] == 'M1M':
            print('Acción: mueve un misionero')
        if acciones[na] == 'M2M':
            print('Acción: mueve dos misioneros')
        if acciones[na] == 'M1C':
            print('Acción: mueve un canibal')
        if acciones[na] == 'M2C':
            print('Acción: mueve dos caníbales')
        if acciones[na] == 'M1M1C':
            print('Acción: mueve un misionero y un canibal')
        print('Estado:',nodos[na+1].state)
    print('FIN')

#-------------------------------------------------------------------
# EJEMPLOS DE USO

# Problema 1: (3,3,1) -> (0,0,0) para 3 misioneros y 3 caníbales
prob1 = MisionerosYCanibales()

# Resolviendo el problema 1:
print("Solución del Problema 1 mediante búsqueda primero en anchura")
meta1 = breadth_first_search(prob1)
if meta1:
    despliega_solucion(meta1)
else:
    print("Falla: no se encontró una solución")

# Resolviendo el problema 2:
