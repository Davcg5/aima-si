from csp import (parse_neighbors,solve_zebra, first_unassigned_variable,
						backtracking_search,CSP)
from utils import argmin_random_tie, count, first
import operator
from math import ceil

#Basate en el NQueen para poder implicar la logica del codigo (archivo CSP.py)
class CSPPicaPix(CSP):

    def __init__(self, variables, domains, neighbors, constraints):
        "Construct a CSP problem. If variables is empty, it becomes domains.keys()."     
        CSP.__init__(self,variables, domains, neighbors, constraints)

    def assign(self, var, val, assignment):
        CSP.assign(self, var, val, assignment)
        #print(assignment)

    def unassign(self, var, assignment):
        CSP.unassign(self, var, assignment)
        #print(assignment)
      
def main1():
	print("Challenge 1")
	variables=[]
	values = ["R","W","Y","G"]
	domains={}  
	for x in range(25):
		variable = 'V'+str(x+1)
		variables.append(variable)

	for i in variables:
		if i == 'V1' or i == 'V2' or i == 'V3' or i == 'V4' or i == 'V5' or i == 'V6' or i == 'V8' or i == 'V10' or i == 'V11' or i == 'V12' or i == 'V13' or i == 'V14' or i == 'V15' or i == 'V16' or i == 'V18' or i == 'V20' or i == 'V21' or i == 'V22' or i == 'V23' or i == 'V24' or i == 'V25':
			domains[i] = {"R","W"}
		elif i == 'V7':
			domains[i] = {"R","W","A","V"}
		elif i == 'V9' or  i == 'V17' or i == 'V19':
			domains[i] = {"R","V","W"}
		else:
			domains[i] = values

	print(variables)
	neighbors=  parse_neighbors("""V1: V2 V3 V4 V5 V6 V11 V16 V21;
		V2: V3 V4 V5 V7 V12 V17 V22;
		V3: V4 V5 V8 V13 V18 V23;
		V4: V5 V9 V14 V19 V24;
		V5: V10 V15 V20 V25;
		V6: V7 V8 V9 V10 V11 V16 V21;
		V7: V8 V9 V10 V12 V17 V22;
		V8: V9 V10 V13 V18 V23;
		V9: V10 V14 V19 V24;
		V10: V15 V20 V25;
		V11: V12 V13 V14 V15 V16 V21;
		V12: V13 V14 V15 V17 V22;
		V13: V14 V15 V18 V23;
		V14: V15 V19 V24;
		V15: V20 V25;
		V16: V17 V18 V19 V20 V21;
		V17: V18 V19 V20 V22;
		V18: V19 V20 V23;
		V19: V20 V24;
		V20: V25;
		V21: V22 V23 V24 V25;
		V22: V23 V24 V25;
		V23: V24 V25;
		V24: V25""",variables)
	   
	def picapix_constraint(A,a,B,b,invert=True):

	    if A == 'V1' and B == 'V2' or A  =='V2' and B == 'V1':
	    	return a == b
	    if A == 'V1' and B == 'V3' or A == 'V3' and B == 'V1':
	    	return a != b
	    if A == 'V1' and B == 'V4' or A == 'V4' and B == 'V1':
	    	return a != b
	    if A == 'V1' and B == 'V5' or A == 'V5' and B == 'V1':
	    	return a == b
	    if A == 'V1' and B == 'V6' or A == 'V6' and B == 'V1':
	    	return a == b 
	    if A == 'V1' and B == 'V11' or A == 'V11' and B == 'V1':
	    	return a != b 
	    if A == 'V1' and B == 'V16' or A  == 'V16' and B == 'V1':
	    	return a != b
	    if A == 'V1' and B == 'V21' or A == 'V21' and B == 'V1':
	    	return a == b 


	    if A == 'V2' and B == 'V3' or A == 'V3' and B == 'V2':
	    	return a != b 
	    if A == 'V2' and B == 'V4' or A == 'V4' and B == 'V2':
	    	return a != b
	    if A == 'V2' and B == 'V5' or A == 'V5' and B == 'V2':
	    	return a == b
	    if A == 'V2' and B == 'V7' or A == 'V7' and B == 'V2':
	    	return a != b
	    if A  == 'V2' and B == 'V12' or A == 'V12' and B == 'V2':
	    	return a != b
	    if A  == 'V2' and B == 'V17' or A == 'V17' and B == 'V2':
	    	return a != b
	    if A  == 'V2' and B == 'V22' or A == 'V22' and B == 'V2':
	    	return a == b


	    if A  == 'V3' and B == 'V4' or A == 'V4' and B == 'V3':
	    	return a == b
	    if A  == 'V3' and B == 'V5' or A == 'V5' and B == 'V3':
	    	return a != b
	    if A  == 'V3' and B == 'V8' or A == 'V8' and B == 'V3':
	    	return a == b
	    if A  == 'V3' and B == 'V13' or A == 'V13' and B == 'V3':
	    	return a != b
	    if A  == 'V3' and B == 'V18' or A == 'V18' and B == 'V3':
	    	return a == b
	    if A  == 'V3' and B == 'V23' or A == 'V23' and B == 'V3':
	    	return a == b


	    if A  == 'V4' and B == 'V5' or A == 'V5' and B == 'V4':
	    	return a != b
	    if A  == 'V4' and B == 'V9' or A == 'V9' and B == 'V4':
	    	return a != b
	    if A  == 'V4' and B == 'V14' or A == 'V14' and B == 'V4':
	    	return a == b
	    if A  == 'V4' and B == 'V19' or A == 'V19' and B == 'V4':
	    	return a != b
	    if A  == 'V4' and B == 'V24' or A == 'V24' and B == 'V4':
	    	return a == b

	    if A  == 'V5' and B == 'V10' or A == 'V10' and B == 'V5':
	    	return a == b
	    if A  == 'V5' and B == 'V15' or A == 'V15' and B == 'V5':
	    	return a != b
	    if A  == 'V5' and B == 'V20' or A == 'V20' and B == 'V5':
	    	return a != b
	    if A  == 'V5' and B == 'V25' or A == 'V25' and B == 'V5':
	    	return a == b			
	    
	    if A  == 'V6' and B == 'V7' or A == 'V7' and B == 'V6':
	    	return a != b
	    if A  == 'V6' and B == 'V8' or A == 'V8' and B == 'V6':
	    	return a != b		
	    if A  == 'V6' and B == 'V9' or A == 'V9' and B == 'V6':
	    	return a != b
	    if A  == 'V6' and B == 'V10' or A == 'V10' and B == 'V6':
	    	return a == b
	    if A  == 'V6' and B == 'V11' or A == 'V11' and B == 'V6':
	    	return a != b	
	    if A  == 'V6' and B == 'V16' or A == 'V16' and B == 'V6':
	    	return a != b
	    if A  == 'V6' and B == 'V21' or A == 'V21' and B == 'V6':
	    	return a == b


	    if A  == 'V7' and B == 'V8' or A == 'V8' and B == 'V7':
	    	return a != b
	    if A  == 'V7' and B == 'V9' or A == 'V9' and B == 'V7':
	    	return a != b
	    if A  == 'V7' and B == 'V10' or A == 'V10' and B == 'V7':
	    	return a != b
	    if A  == 'V7' and B == 'V12' or A == 'V12' and B == 'V7':
	    	return a != b
	    if A  == 'V7' and B == 'V17' or A == 'V17' and B == 'V7':
	    	return a != b
	    if A  == 'V7' and B == 'V22' or A == 'V22' and B == 'V7':
	    	return a != b


	    if A  == 'V8' and B == 'V9' or A == 'V9' and B == 'V8':
	    	return a != b
	    if A  == 'V8' and B == 'V10' or A == 'V10' and B == 'V8':
	    	return a != b
	    if A  == 'V8' and B == 'V13' or A == 'V13' and B == 'V8':
	    	return a != b	
	    if A  == 'V8' and B == 'V18' or A == 'V18' and B == 'V8':
	    	return a == b
	    if A  == 'V8' and B == 'V23' or A == 'V23' and B == 'V8':
	    	return a == b

	    if A  == 'V9' and B == 'V10' or A == 'V10' and B == 'V9':
	    	return a != b	
	    if A  == 'V9' and B == 'V14' or A == 'V14' and B == 'V9':
	    	return a != b	
	    if A  == 'V9' and B == 'V19' or A == 'V19' and B == 'V9':
	    	return a != b
	    if A  == 'V9' and B == 'V24' or A == 'V24' and B == 'V9':
	    	return a != b	

	    if A  == 'V10' and B == 'V15' or A == 'V15' and B == 'V10':
	    	return a != b
	    if A  == 'V10' and B == 'V20' or A == 'V20' and B == 'V10':
	    	return a != b
	    if A  == 'V10' and B == 'V25' or A == 'V25' and B == 'V10':
	    	return a == b


	    if A  == 'V11' and B == 'V12' or A == 'V12' and B == 'V11':
	    	return a == b
	    if A  == 'V11' and B == 'V13' or A == 'V13' and B == 'V11':
	    	return a != b 
	    if A  == 'V11' and B == 'V14' or A == 'V14' and B == 'V11':
	    	return a == b
	    if A  == 'V11' and B == 'V15' or A == 'V15' and B == 'V11':
	    	return a == b
	    if A  == 'V11' and B == 'V16' or A == 'V16' and B == 'V11':
	    	return a == b	
	    if A  == 'V11' and B == 'V21' or A == 'V21' and B == 'V11':
	    	return a != b


	    if A  == 'V12' and B == 'V13' or A == 'V13' and B == 'V12':
	    	return a != b
	    if A  == 'V12' and B == 'V14' or A == 'V14' and B == 'V12':
	    	return a == b
	    if A  == 'V12' and B == 'V15' or A == 'V15' and B == 'V12':
	    	return a == b
	    if A  == 'V12' and B == 'V17' or A == 'V17' and B == 'V12':
	    	return a != b
	    if A  == 'V12' and B == 'V22' or A == 'V22' and B == 'V12':
	    	return a != b

	    if A  == 'V13' and B == 'V14' or A == 'V14' and B == 'V13':
	    	return a != b	
	    if A  == 'V13' and B == 'V15' or A == 'V15' and B == 'V13':
	    	return a != b
	    if A  == 'V13' and B == 'V18' or A == 'V18' and B == 'V13':
	    	return a != b
	    if A  == 'V13' and B == 'V23' or A == 'V23' and B == 'V13':
	    	return a != b

	    if A  == 'V14' and B == 'V15' or A == 'V15' and B == 'V14':
	    	return a == b
	    if A  == 'V14' and B == 'V19' or A == 'V19' and B == 'V14':
	    	return a != b
	    if A  == 'V14' and B == 'V24' or A == 'V24' and B == 'V14':
	    	return a == b

	    if A  == 'V15' and B == 'V20' or A == 'V20' and B == 'V15':
	    	return a == b
	    if A  == 'V15' and B == 'V25' or A == 'V25' and B == 'V15':
	    	return a != b	

	    if A  == 'V16' and B == 'V17' or A == 'V17' and B == 'V16':
	    	return a != b
	    if A  == 'V16' and B == 'V18' or A == 'V18' and B == 'V16':
	    	return a == b
	    if A  == 'V16' and B == 'V19' or A == 'V19' and B == 'V16':
	    	return a != b
	    if A  == 'V16' and B == 'V20' or A == 'V20' and B == 'V16':
	    	return a == b
	    if A  == 'V16' and B == 'V21' or A == 'V21' and B == 'V16':
	    	return a != b
	    
	    if A  == 'V17' and B == 'V18' or A == 'V18' and B == 'V17':
	    	return a != b	
	    if A  == 'V17' and B == 'V19' or A == 'V19' and B == 'V17':
	    	return a != b	
	    if A  == 'V17' and B == 'V20' or A == 'V20' and B == 'V17':
	    	return a != b	
	    if A  == 'V17' and B == 'V22' or A == 'V22' and B == 'V17':
	    	return a != b	

	    if A  == 'V18' and B == 'V19' or A == 'V19' and B == 'V18':
	    	return a != b	
	    if A  == 'V18' and B == 'V20' or A == 'V20' and B == 'V18':
	    	return a == b
	    if A  == 'V18' and B == 'V23' or A == 'V23' and B == 'V18':
	    	return a == b

	    if A  == 'V19' and B == 'V20' or A == 'V20' and B == 'V19':
	    	return a != b
	    if A  == 'V19' and B == 'V24' or A == 'V24' and B == 'V19':
	    	return a != b

	    if A  == 'V20' and B == 'V25' or A == 'V25' and B == 'V20':
	    	return a != b

	    if A  == 'V21' and B == 'V22' or A == 'V22' and B == 'V21':
	    	return a == b
	    if A  == 'V21' and B == 'V23' or A == 'V23' and B == 'V21':
	    	return a != b
	    if A  == 'V21' and B == 'V24' or A == 'V24' and B == 'V21':
	    	return a != b
	    if A  == 'V21' and B == 'V25' or A == 'V25' and B == 'V21':
	    	return a == b


	    if A  == 'V22' and B == 'V23' or A == 'V23' and B == 'V22':
	    	return a != b
	    if A  == 'V22' and B == 'V24' or A == 'V24' and B == 'V22':
	    	return a != b
	    if A  == 'V22' and B == 'V25' or A == 'V25' and B == 'V22':
	    	return a == b

	    if A  == 'V23' and B == 'V24' or A == 'V24' and B == 'V23':
	    	return a == b
	    if A  == 'V23' and B == 'V25' or A == 'V25' and B == 'V23':
	    	return a != b

	    if A  == 'V24' and B == 'V25' or A == 'V25' and B == 'V24':
	    	return a != b
	    return False    

	pica = CSPPicaPix(variables, domains, neighbors, picapix_constraint)
	print("Resultado: ",backtracking_search(pica))

def main2():

	print("Challenge 2")
	variables = []
	values = ["Orange","White","Black","Yellow"] 
	domains = {}

	for x in range(25):
		variable = 'V'+str(x+1)
		variables.append(variable)
	print(variables)
	neighbors=  parse_neighbors("""V1: V2 V3 V4 V5 V6 V11 V16 V21;
		V2: V3 V4 V5 V7 V12 V17 V22;
		V3: V4 V5 V8 V13 V18 V23;
		V4: V5 V9 V14 V19 V24;
		V5: V10 V15 V20 V25;
		V6: V7 V8 V9 V10 V11 V16 V21;
		V7: V8 V9 V10 V12 V17 V22;
		V8: V9 V10 V13 V18 V23;
		V9: V10 V14 V19 V24;
		V10: V15 V20 V25;
		V11: V12 V13 V14 V15 V16 V21;
		V12: V13 V14 V15 V17 V22;
		V13: V14 V15 V18 V23;
		V14: V15 V19 V24;
		V15: V20 V25;
		V16: V17 V18 V19 V20 V21;
		V17: V18 V19 V20 V22;
		V18: V19 V20 V23;
		V19: V20 V24;
		V20: V25;
		V21: V22 V23 V24 V25;
		V22: V23 V24 V25;
		V23: V24 V25;
		V24: V25""",variables)
	   	
	for i in variables:
		if i == 'V1' or i == 'V16' or i == 'V21' or i == 'V23' or i == 'V5' or i == 'V25':
			domains[i] = {"Yellow","White"} 
		elif i == 'V2' or i == 'V4' or i == 'V8' or i == 'V10' or i == 'V12' or i == 'V13' or i == 'V14' or i == 'V15' or i == 'V17' or i == 'V19':
			domains[i] = {"Orange","White"}
		elif i  == 'V3' or i == 'V5' or i == 'V18' or i == 'V20':
			domains[i] = {"Yellow","Orange","White"}
		elif i == 'V7' or i == 'V9':
			domains[i] = {"Black","Orange","White"}
		else:
			domains[i] = {"White"}

	def constrains(A,a,B,b, invert=True):
		if A == 'V1' and B == 'V2' or A  =='V2' and B == 'V1':
			return a != b
		if A == 'V1' and B == 'V3' or A == 'V3' and B == 'V1':
			return a != b
		if A == 'V1' and B == 'V4' or A == 'V4' and B == 'V1':
			return a != b
		if A == 'V1' and B == 'V5' or A == 'V5' and B == 'V1':
			return a != b
		if A == 'V1' and B == 'V6' or A == 'V6' and B == 'V1':
			return a != b 
		if A == 'V1' and B == 'V11' or A == 'V11' and B == 'V1':
			return a != b 
		if A == 'V1' and B == 'V16' or A  == 'V16' and B == 'V1':
			return a == b
		if A == 'V1' and B == 'V21' or A == 'V21' and B == 'V1':
			return a != b 

		if A == 'V2' and B == 'V3' or A == 'V3' and B == 'V2':
			return a != b 
		if A == 'V2' and B == 'V4' or A == 'V4' and B == 'V2':
			return a != b
		if A == 'V2' and B == 'V5' or A == 'V5' and B == 'V2':
			return a == b
		if A == 'V2' and B == 'V7' or A == 'V7' and B == 'V2':
			return a != b
		if A  == 'V2' and B == 'V12' or A == 'V12' and B == 'V2':
			return a != b
		if A  == 'V2' and B == 'V17' or A == 'V17' and B == 'V2':
			return a == b
		if A  == 'V2' and B == 'V22' or A == 'V22' and B == 'V2':
			return a == b

		if A  == 'V3' and B == 'V4' or A == 'V4' and B == 'V3':
			return a == b
		if A  == 'V3' and B == 'V5' or A == 'V5' and B == 'V3':
			return a != b
		if A  == 'V3' and B == 'V8' or A == 'V8' and B == 'V3':
			return a == b
		if A  == 'V3' and B == 'V13' or A == 'V13' and B == 'V3':
			return a == b
		if A  == 'V3' and B == 'V18' or A == 'V18' and B == 'V3':
			return a == b
		if A  == 'V3' and B == 'V23' or A == 'V23' and B == 'V3':
			return a != b


		if A  == 'V4' and B == 'V5' or A == 'V5' and B == 'V4':
			return a != b
		if A  == 'V4' and B == 'V9' or A == 'V9' and B == 'V4':
			return a != b
		if A  == 'V4' and B == 'V14' or A == 'V14' and B == 'V4':
			return a == b
		if A  == 'V4' and B == 'V19' or A == 'V19' and B == 'V4':
			return a == b
		if A  == 'V4' and B == 'V24' or A == 'V24' and B == 'V4':
			return a != b

		if A  == 'V5' and B == 'V10' or A == 'V10' and B == 'V5':
			return a != b
		if A  == 'V5' and B == 'V15' or A == 'V15' and B == 'V5':
	   		return a != b
		if A  == 'V5' and B == 'V20' or A == 'V20' and B == 'V5':
			return a == b
		if A  == 'V5' and B == 'V25' or A == 'V25' and B == 'V5':
			return a != b			
	    
		if A  == 'V6' and B == 'V7' or A == 'V7' and B == 'V6':
			return a != b
		if A  == 'V6' and B == 'V8' or A == 'V8' and B == 'V6':
			return a != b		
		if A  == 'V6' and B == 'V9' or A == 'V9' and B == 'V6':
			return a != b
		if A  == 'V6' and B == 'V10' or A == 'V10' and B == 'V6':
			return a != b
		if A  == 'V6' and B == 'V11' or A == 'V11' and B == 'V6':
			return a == b	
		if A  == 'V6' and B == 'V16' or A == 'V16' and B == 'V6':
			return a != b
		if A  == 'V6' and B == 'V21' or A == 'V21' and B == 'V6':
			return a == b


		if A  == 'V7' and B == 'V8' or A == 'V8' and B == 'V7':
			return a != b
		if A  == 'V7' and B == 'V9' or A == 'V9' and B == 'V7':
			return a == b
		if A  == 'V7' and B == 'V10' or A == 'V10' and B == 'V7':
			return a != b
		if A  == 'V7' and B == 'V12' or A == 'V12' and B == 'V7':
			return a != b
		if A  == 'V7' and B == 'V17' or A == 'V17' and B == 'V7':
			return a != b
		if A  == 'V7' and B == 'V22' or A == 'V22' and B == 'V7':
			return a != b

		if A  == 'V8' and B == 'V9' or A == 'V9' and B == 'V8':
			return a != b
		if A  == 'V8' and B == 'V10' or A == 'V10' and B == 'V8':
			return a == b
		if A  == 'V8' and B == 'V13' or A == 'V13' and B == 'V8':
			return a == b	
		if A  == 'V8' and B == 'V18' or A == 'V18' and B == 'V8':
			return a == b
		if A  == 'V8' and B == 'V23' or A == 'V23' and B == 'V8':
			return a != b

		if A  == 'V9' and B == 'V10' or A == 'V10' and B == 'V9':
			return a != b	
		if A  == 'V9' and B == 'V14' or A == 'V14' and B == 'V9':
			return a != b	
		if A  == 'V9' and B == 'V19' or A == 'V19' and B == 'V9':
			return a != b
		if A  == 'V9' and B == 'V24' or A == 'V24' and B == 'V9':
			return a != b	

		if A  == 'V10' and B == 'V15' or A == 'V15' and B == 'V10':
			return a == b
		if A  == 'V10' and B == 'V20' or A == 'V20' and B == 'V10':
			return a != b
		if A  == 'V10' and B == 'V25' or A == 'V25' and B == 'V10':
			return a != b


		if A  == 'V11' and B == 'V12' or A == 'V12' and B == 'V11':
			return a != b
		if A  == 'V11' and B == 'V13' or A == 'V13' and B == 'V11':
			return a != b 
		if A  == 'V11' and B == 'V14' or A == 'V14' and B == 'V11':
			return a != b
		if A  == 'V11' and B == 'V15' or A == 'V15' and B == 'V11':
			return a != b
		if A  == 'V11' and B == 'V16' or A == 'V16' and B == 'V11':
			return a != b	
		if A  == 'V11' and B == 'V21' or A == 'V21' and B == 'V11':
			return a == b


		if A  == 'V12' and B == 'V13' or A == 'V13' and B == 'V12':
	   		return a == b
		if A  == 'V12' and B == 'V14' or A == 'V14' and B == 'V12':
			return a == b
		if A  == 'V12' and B == 'V15' or A == 'V15' and B == 'V12':
			return a == b
		if A  == 'V12' and B == 'V17' or A == 'V17' and B == 'V12':
			return a != b
		if A  == 'V12' and B == 'V22' or A == 'V22' and B == 'V12':
			return a != b

		if A  == 'V13' and B == 'V14' or A == 'V14' and B == 'V13':
			return a == b	
		if A  == 'V13' and B == 'V15' or A == 'V15' and B == 'V13':
			return a == b
		if A  == 'V13' and B == 'V18' or A == 'V18' and B == 'V13':
			return a == b
		if A  == 'V13' and B == 'V23' or A == 'V23' and B == 'V13':
			return a != b

		if A  == 'V14' and B == 'V15' or A == 'V15' and B == 'V14':
			return a == b
		if A  == 'V14' and B == 'V19' or A == 'V19' and B == 'V14':
			return a == b
		if A  == 'V14' and B == 'V24' or A == 'V24' and B == 'V14':
			return a != b

		if A  == 'V15' and B == 'V20' or A == 'V20' and B == 'V15':
			return a != b
		if A  == 'V15' and B == 'V25' or A == 'V25' and B == 'V15':
			return a != b	

		if A  == 'V16' and B == 'V17' or A == 'V17' and B == 'V16':
			return a != b
		if A  == 'V16' and B == 'V18' or A == 'V18' and B == 'V16':
			return a != b
		if A  == 'V16' and B == 'V19' or A == 'V19' and B == 'V16':
			return a != b
		if A  == 'V16' and B == 'V20' or A == 'V20' and B == 'V16':
			return a != b
		if A  == 'V16' and B == 'V21' or A == 'V21' and B == 'V16':
			return a != b
	    
		if A  == 'V17' and B == 'V18' or A == 'V18' and B == 'V17':
			return a != b	
		if A  == 'V17' and B == 'V19' or A == 'V19' and B == 'V17':
			return a != b	
		if A  == 'V17' and B == 'V20' or A == 'V20' and B == 'V17':
			return a == b	
		if A  == 'V17' and B == 'V22' or A == 'V22' and B == 'V17':
			return a == b	

		if A  == 'V18' and B == 'V19' or A == 'V19' and B == 'V18':
			return a == b	
		if A  == 'V18' and B == 'V20' or A == 'V20' and B == 'V18':
			return a != b
		if A  == 'V18' and B == 'V23' or A == 'V23' and B == 'V18':
			return a != b

		if A  == 'V19' and B == 'V20' or A == 'V20' and B == 'V19':
			return a != b
		if A  == 'V19' and B == 'V24' or A == 'V24' and B == 'V19':
			return a != b

		if A  == 'V20' and B == 'V25' or A == 'V25' and B == 'V20':
			return a != b

		if A  == 'V21' and B == 'V22' or A == 'V22' and B == 'V21':
			return a == b
		if A  == 'V21' and B == 'V23' or A == 'V23' and B == 'V21':
			return a != b
		if A  == 'V21' and B == 'V24' or A == 'V24' and B == 'V21':
			return a == b
		if A  == 'V21' and B == 'V25' or A == 'V25' and B == 'V21':
			return a != b


		if A  == 'V22' and B == 'V23' or A == 'V23' and B == 'V22':
			return a != b
		if A  == 'V22' and B == 'V24' or A == 'V24' and B == 'V22':
			return a == b
		if A  == 'V22' and B == 'V25' or A == 'V25' and B == 'V22':
			return a != b

		if A  == 'V23' and B == 'V24' or A == 'V24' and B == 'V23':
			return a != b
		if A  == 'V23' and B == 'V25' or A == 'V25' and B == 'V23':
			return a == b

		if A  == 'V24' and B == 'V25' or A == 'V25' and B == 'V24':
			return a != b
		return False   
	pica = CSPPicaPix(variables, domains, neighbors, constrains)
	print("Resultado: ",backtracking_search(pica))	

if __name__ == "__main__":
	#main1()
	main2()
     
