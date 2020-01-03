from math import e, pi, sin, cos
from operator import add, sub, mul
#Enabling python3 HTML
#import cgitb 
#cgitb.enable()

def div(a, b):
    return a / b

operator = {'+': add, '-': sub, '*': mul, '/': div, 'sin': sin, 'cos': cos}
constant = {'e': e, 'π': pi}

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
                term = float(term)
            #exception handles if term is something other than an integer
            except ValueError:
                if term in operator:
                    term = operator[term]
                else:
                    coefficient = term[:term.index(var)]
                    #Checking to see if there is an exponent. If not, uses default value of 1.
                    try:
                        if term[term.index(var) + 1 : term.index(var) + 2] == '^':
                            exponent = Function(term[term.index(var) + 2:]).evaluate(val, var)
                    finally:  
                        if coefficient:
                            term = mul(Function(coefficient).evaluate(val, var), pow(val, exponent))
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
        return round((self.evaluate(val + (1 * step), var) - self.evaluate(val, var)) / step, 3)

    # Riemann approximation of the integral of a given function across a given bound a to b with step size step.
    def integrate(self, a, b, var, step):
        result = 0
        while a < b:
            result += self.evaluate(a, var) * step
            a += step
        return round(result, 3)
        
new_func = Function('2x^2 + 4x + 10x^3')
print('Function:', new_func.func)

eval_result = new_func.evaluate(2, 'x')
print('Eval Result:', eval_result)

diff_result = new_func.differentiate(3, 'x', 0.0001)
print('Diff Result:', diff_result)

inte_result = new_func.integrate(0, 1, 'x', 0.0001)
print('Integrate Result:', inte_result)
