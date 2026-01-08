class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b


    def addition(self):
        self.result=self.a+self.b
        return self.result

    def subtraction(self):
        self.result=self.a-self.b
        return self.result

    def multiplication(self,):
        self.result=self.a*self.b
        return self.result

    def division(self):
        self.result=self.a/self.b
        return self.result

    def modulus(self):
        self.result=self.a%self.b
        return self.result

calc=Calculator(a=20,b=20)
print("Add:",calc.addition())
print("Sub:",calc.subtraction())
print("Mul:",calc.multiplication())
print("Div:",calc.division())
print("Mod:",calc.modulus())

