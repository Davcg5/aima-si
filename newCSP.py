from csp import (parse_neighbors,solve_zebra, first_unassigned_variable,
						backtracking_search,CSP)
from utils import argmin_random_tie, count, first
import operator
from math import ceil

#Basate en el NQueen para poder implicar la logica del codigo (archivo CSP.py)
class CSPPicaPix(CSP):

    def __init__(self, variables, domains, neighbors, constraints):
        "Construct a CSP problem. If variables is empty, it becomes domains.keys()."
        print("INIT CSPPP")
        CSP.__init__(self,variables, domains, neighbors, constraints)
        self.copiaassignment = None

    def assign(self, var, val, assignment):
        CSP.assign(self, var, val, assignment)
        self.copiaassignment = assignment
        #print(self.copiaassignment)

    def unassign(self, var, assignment):
        CSP.unassign(self, var, assignment)
        self.copiaassignment = assignment
        #print(self.copiaassignment)

def main1():
	print("main")
	variables = "R1 R2 R3 R4".split()
	values = ["Red", "Green","Yellow"]
	domains={}
	for i in variables:
		domains[i] = values
    
	neighbors = parse_neighbors("""R1: R2 R3;
		R4: R3; R3: R2""", variables)
	#no repetir relaciones

	#A B nodos R1 A R4
	#a b valores 
		
	def picapix__constraint(A, a, B, b,invert = True):        
		if A == 'R1' and B == 'R2' or A == 'R2' and B == 'R1':
			return a != b
		if (A == 'R2' and B == 'R4') or (A == 'R4' and B == 'R2') or \
			(A == 'R1' and B == 'R4') or (A == 'R4' and B == 'R1'):
			return a == b
		if A == 'R3' and B == 'R4' or A == 'R4' and B == 'R3':
			return a != b
		if A == 'R3' and B == 'R2' or A == 'R2' and B == 'R3':
			return a != b
		if A == 'R3' and B == 'R1' or A == 'R1' and B == 'R3':
			return a != b
		return False
	
	pica = CSPPicaPix(variables, domains, neighbors, picapix__constraint)
	print("Resultado: ",backtracking_search(pica))


	#Eje X y eje Y
	#25 variables 
	#Dominio Interseccion entre Colores arriba y colores lado derecho 
	# 1,1 A verde Lado Rojo, Verde so color es verde , verde y rojo y verde y rojo son valores son verde y rojo
	# si arriba es verde y abajo es rojo so valor = blanco
	# si 2 verdes dos fichas seguidas verdes	
if __name__ == "__main__":
	main1() #Regiones jalando
     
