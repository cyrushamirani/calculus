from math import e, pi, sin, cos
from operator import add, sub, mul

def div(a, b):
    return a / b

#for parsing the function passed in as a string
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operator = {'+': add, '-': sub, '*': mul, '/': div}


class Function:
    #Initialize a given function.
    def __init__(self, text):
        self.func = text

    #Evalute function with value val assigned to variable var.
    def evaluate(self, val, var):
        expression = []
        copy = self.func
        #build a list of evaluated terms, to be evaluated by the operators which seperate them.
        while copy:
            exponent = 1
            try:
                term = copy[:copy.index(" ")]
            #exception handles if there are no more terms after this term that we are currently evaluating.
            except:
                term = copy
            try:
                term = int(term)
            #exception handles if term is something other than an integer
            except ValueError:
                if term in operator:
                    term = operator[term]
                else:
                    coefficient = term[:term.index(var)]
                    #Checking to see if there is an exponent.
                    try:
                        if term[term.index(var) + 1 : term.index(var) + 2] == '^':
                            exponent = int(term[term.index(var) + 2:])
                    finally:  
                        if coefficient:
                            term = mul(int(coefficient), pow(val, exponent))
                        else:
                            term = val
            expression += [term]
            try:
                copy = copy[copy.index(" ") + 1:]
            #exception handles if there are no more terms after this term that we are currently evaluating.
            except:
                copy = ""
        #evaluate the list of the terms that we evaluated in previous step to obtain numerical result.
        while len(expression) != 1:
            result = expression[1](expression[0], expression[2])
            expression = [result] + expression[3:]
        return expression[0]
            
    # Differentiate function at a point val with respect to a certain variable var. 
    def differentiate(self, val, var, step):
        return (self.evaluate(val + (1 * step), var) - self.evaluate(val, var)) / step

    # Riemann approximation of the integral of a given function across a given bound a to b with step size step.
    def integrate(self, a, b, var, step):
        result = 0
        while a < b:
            result += self.evaluate(a, var) * step
            a += step
        return result
