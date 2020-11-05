# AutoDiffToy class
class AutoDiffToy():
    def __init__(self, val, der=1):
        #store the initial value and the derivative into the class variables
        self.val = val
        self.der = der    
    def __add__(self, other):
        try: #try to see if other is of the same type; if not go to the next step
            return AutoDiffToy(self.val+other.val,self.der+other.der)
        except AttributeError: # this occurs if not the same type meaning, we are adding a constant
            return AutoDiffToy(self.val+other,self.der)
    def __mul__(self, constant): #we must multiply the value and its deriative by whatever constant it is being multiplied by
        return AutoDiffToy(self.val*constant,self.der*constant)
    def __rmul__(self, constant): # this fixes the case in which the order of multiplication is switched
        return self.__mul__(constant)
    def __radd__(self, constant): # this fixes the case in which the order of addition is switched
        return self.__add__(constant)


a = 2.0 # Value to evaluate at
x = AutoDiffToy(a)

alpha = 2.0
beta = 3.0

f = alpha * x + beta
print(f.val, f.der)
f = x * alpha + beta
print(f.val, f.der)
f = beta + alpha * x
print(f.val, f.der)
f = beta + x * alpha
print(f.val, f.der)