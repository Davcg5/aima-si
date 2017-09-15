from csp import (parse_neighbors,solve_zebra, first_unassigned_variable,
						backtracking_search,CSP)
from utils import argmin_random_tie, count, first
import operator
from math import ceil

class Picapix(CSP):

    """This class describes finite-domain Constraint Satisfaction Problems.
    A CSP is specified by the following inputs:
        variables        A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
    In the textbook and in most mathematical definitions, the
    constraints are specified as explicit pairs of allowable values,
    but the formulation here is easier to express and more compact for
    most cases. (For example, the n-Queens problem can be represented
    in O(n) space using this notation, instead of O(N^4) for the
    explicit representation.) In terms of describing the CSP as a
    problem, that's all there is.

    However, the class also supports data structures and methods that help you
    solve CSPs by calling a search function on the CSP.  Methods and slots are
    as follows, where the argument 'a' represents an assignment, which is a
    dict of {var:val} entries:
        assign(var, val, a)     Assign a[var] = val; do other bookkeeping
        unassign(var, a)        Do del a[var], plus other bookkeeping
        nconflicts(var, val, a) Return the number of other variables that
                                conflict with var=val
        curr_domains[var]       Slot: remaining consistent values for var
                                Used by constraint propagation routines.
    The following methods are used only by graph_search and tree_search:
        actions(state)          Return a list of actions
        result(state, action)   Return a successor of state
        goal_test(state)        Return true if all constraints satisfied
    The following are just for debugging purposes:
        nassigns                Slot: tracks the number of assignments made
        display(a)              Print a human-readable representation
    """

    def __init__(self, variables, domains, neighbors, constraints):
        "Construct a CSP problem. If variables is empty, it becomes domains.keys()."
        variables = variables or list(domains.keys())

        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = ()
        self.curr_domains = None
        self.nassigns = 0

    def assign(self, var, val, assignment):
        "Add {var: val} to assignment; Discard the old value if any."
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        "Return the number of conflicts var=val has with other variables."
        # Subclasses may implement this more efficiently
        def conflict(var2):
            return (var2 in assignment and
                    not self.constraints(var, val, var2, assignment[var2]))
        return count(conflict(v) for v in self.neighbors[var])

    def display(self, assignment):
        "Show a human-readable representation of the CSP."
        # Subclasses can print in a prettier way, or display with a GUI
        print('CSP:', self, 'with assignment:', assignment)

    # These methods are for the tree- and graph-search interface:

    def actions(self, state):
        """Return a list of applicable actions: nonconflicting
        assignments to an unassigned variable."""
        if len(state) == len(self.variables):
            return []
        else:
            assignment = dict(state)
            var = first([v for v in self.variables if v not in assignment])
            return [(var, val) for val in self.domains[var]
                    if self.nconflicts(var, val, assignment) == 0]

    def result(self, state, action):
        "Perform an action and return the new state."
        (var, val) = action
        return state + ((var, val),)

    def goal_test(self, state):
        "The goal is to assign all variables, with all constraints satisfied."
        assignment = dict(state)
        return (len(assignment) == len(self.variables)
                and all(self.nconflicts(variables, assignment[variables], assignment) == 0
                        for variables in self.variables))

    # These are for constraint propagation

    def support_pruning(self):
        """Make sure we can prune values from domains. (We want to pay
        for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        "Start accumulating inferences from assuming var=value."
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals

    def prune(self, var, value, removals):
        "Rule out var=value."
        self.curr_domains[var].remove(value)
        if removals is not None:
            removals.append((var, value))

    def choices(self, var):
        "Return all values for var that aren't currently ruled out."
        return (self.curr_domains or self.domains)[var]

    def infer_assignment(self):
        "Return the partial assignment implied by the current inferences."
        self.support_pruning()
        return {v: self.curr_domains[v][0]
                for v in self.variables if 1 == len(self.curr_domains[v])}

    def restore(self, removals):
        "Undo a supposition and all inferences from it."
        for B, b in removals:
            self.curr_domains[B].append(b)

    # This is for min_conflicts search

    def conflicted_vars(self, current):
        "Return a list of variables in current assignment that are in conflict"
        return [var for var in self.variables
                if self.nconflicts(var, current[var], current) > 0]

def create_domain(values,quantity_colors):
    j = 0
    new_domain = []
    for value in quantity_colors:
	    i = 0
	    colors = []
	    for quantity in value:
		    for num in range(quantity):
			    colors.append(values[i])
		    i += 1
	    new_domain.append(colors+["NC"])
    return new_domain

def unit_colors(domains,row_colum,color,variables,move):   
	variables2 = []
	modify = False
	if move == "row":
		for var in variables[5*row_colum:5*(row_colum+1)]:
			if domains[var].count(color) == 1:
				domains[var] = [color]
				print("--------------",var,domains[var])
				modify = True
	else:
		for i in range(5):
			variables2.append(variables[5*i+row_colum])
		for var in variables2:
			if domains[var].count(color) == 1:
				domains[var] = [color]
				print("--------------",var,domains[var])
				modify = True
	
	return domains,modify


def main2():
	variables=[]
	domains = {}   
	domains_order = {}
	for var in range(25):
		variables.append("V"+str(var+1))
		domains[variables[var]] = []

	colors = ["Pink", "Green", "Yellow", "NC"]
    #~ #Subdomains
    
	X1 = [[0,1,0],[0,0,0]]
	X2 = [[0,2,1],[0,0,0]]
	X3 = [[1,0,0],[0,0,0]]
	X4 = [[2,2,0],[0,1,0]]
	X5 = [[1,1,0],[0,0,0]]
	Y1 = [[1,0,0],[0,0,0]]
	Y2 = [[2,0,0],[0,0,0]]
	Y3 = [[1,1,0],[0,0,0]]
	Y4 = [[0,3,1],[0,1,0]]
	Y5 = [[0,3,0],[0,1,0]]
	colums = [X1[0],X2[0],X3[0],X4[0],X5[0]]
	row = [Y1[0],Y2[0],Y3[0],Y4[0],Y5[0]]
	predomains = [X1[0],X2[0],X3[0],X4[0],X5[0],Y1[0],Y2[0],Y3[0],Y4[0],Y5[0]]
	                              #
	predomains_order = [X1[1],X2[1],X3[1],X4[1],X5[1],Y1[1],Y2[1],Y3[1],Y4[1],Y5[1]]
	predomains = create_domain(colors,predomains)
    #~ map(add, list1, list2)
    
	Y1_V = ["V1","V2","V3","V4","V5"]
	Y2_V = ["V6","V7","V8","V9","V10"]
	Y3_V = ["V11","V12","V13","V14","V15"]
	Y4_V = ["V16","V17","V18","V19","V20"]
	Y5_V = ["V21","V22","V23","V24","V25"]
	X1_V = ["V1","V6","V11","V16","V21"]
	X2_V = ["V2","V7","V12","V17","V22"]
	X3_V = ["V3","V8","V13","V18","V23"]
	X4_V = ["V4","V9","V14","V19","V24"]
	X5_V = ["V5","V10","V15","V20","V25"]    
	for i in range(5):
		for j in range(5):
			domains[variables[j+5*i]] = list(set(predomains[j]) & set(predomains[i+5]))
			domains_order[variables[j+5*i]] = [predomains_order[i+5],predomains_order[j]]
	print(domains_order)
	
	final_domain = True
	type_move = "colum"
	while(final_domain):
		aux = []
		final_domain = False
		
		for i in range(5):
			aux = []
			#~ print("ITERACION "+type_move, i)
			for j in range(5):
				if type_move == "row":
					index = j+5*i
				else:
					index = 5*j+i
				aux += domains[variables[index]]
			#~ print("variable: ",aux )
			k = 0
			for color in colors[0:len(colors)-1]:
				if type_move == "row":
					val_dom = row[i][k]
					#~ print(color, row[i], val_dom)
					value = aux.count(color)-val_dom
					position = i
				else:
					val_dom = colums[i][k]
					#~ print(color,colums[i],val_dom)
					value = aux.count(color)-val_dom
					position = i
					 
				if value == 0 and val_dom>0:
					final_domain = True
					domains,modify = unit_colors(domains,position,color,variables,type_move)
					if modify:
						if type_move == "row":
							row[i][k] -= 1
						else:
							colums[i][k] -= 1
				k += 1
			
			for var in domains:
				if len(domains[var]) == 2:
					if type_move == "row":
						print(domains[var])
						col = int(var.split('V')[1])
						index = ceil(col/5-1)
						print("row",var,index,row[index])

		if type_move == "colum":
			type_move = "row"
			final_domain = True
		else:
			type_move = "column"
			
                         
             
	print(domains['V11'])
	#~ neighbors = parse_neighbors("""
			#~ V1: V2 V3 V4 V5 V6 V11 V16 V21;
			#~ V2: V3 V4 V5 V7 V12 V17 V22;
			#~ V3: V4 V5 V8 V13 V18 V23;
			#~ V4: V5 V9 V14 V19 V24;
			#~ V5: V10 V15 V20 V25;
			#~ V6: V7 V8 V9 V10 V11 V16 V21;
			#~ V7: V8 V9 V10 V12 V17 V22;
			#~ V8: V9 V10 V13 V18 V23;
			#~ V9: V10 V14 V19 V24;
			#~ V10: V15 V20 V25;
			#~ V11: V12 V13 V14 V15 V16 V21;
			#~ V12: V13 V14 V15 V17 V22;
			#~ V13: V14 V15 V18 V23;
			#~ V14: V15 V19 V24;
			#~ V15: V20 V25;
			#~ V16: V17 V18 V19 V20 V21;
			#~ V17: V18 V19 V20 V22;
			#~ V18: V19 V20 V23;
			#~ V19: V20 V24;
			#~ V20: V25;
			#~ V21: V22 V23 V24 V25;
			#~ V22: V23 V24 V25;
			#~ V23: V24 V25;
			#~ V24: V25""", variables)
	
	#~ values_updated = []
	#~ def picapix__constraint(A, a, B, b,invert = True):
		#~ index1 = int(A.split('V')[1])
		#~ index2 = int(B.split('V')[1])
		#~ if len(domains[A]) ==1  and len(domains[B]) == 1: #1 valor para cada uno
			#~ return True
		#~ if len(domains[A]) ==1:
			#~ if abs(index1-index2) == 1: #cuadros adyacentes
				#~ if row[ceil(index1/5)-1][index1-1]>0 or row[ceil(index2/5)-1][index1-1]> 0:
					#~ return True
			#~ elif abs(index1-index2) < 5: #adyancetes mismo row
				#~ if row[floor(index1/5)][index1-1]>0 or row[floor(index2/5)][index1-1]> 0:
					#~ return True

		#~ if a == b:# 2 same color
			#~ if colors.index(a) < 3 and colors.index(b) < 3: #colores iguales 

				#~ if domains_order[A][1][colors.index(b)] > 0 and \
							#~ abs(index1-index2) == 1 : #completar si existe arriba de dos colores disponibles
					#~ return True
			#~ else:
				#~ return False                            

		#~ if invert:
			#~ return picapix__constraint(B, b, A, a,invert = False)
        
		#~ return False
            

	#~ pica = Picapix(variables, domains, neighbors, picapix__constraint)
	#~ print("Resultado: ",backtracking_search(pica))


def main1():

	variables = "R1 R2 R3 R4".split()
	values = ["Red", "Green","Yellow"]
	domains={}
	for i in variables:
		domains[i] = values
    
	neighbors = parse_neighbors("""R1: R2 R3;
		R4: R3; R3: R2""", variables)

		
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
	pica = Picapix(variables, domains, neighbors, picapix__constraint)
	print("Resultado: ",backtracking_search(pica))




if __name__ == "__main__":
	main1() #Regiones jalando
	#~ main2() #este esta cabron

                


