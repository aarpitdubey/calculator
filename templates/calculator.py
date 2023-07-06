class Calculator:
    
    def __init__(self, num1, num2):
        self.num1=int(input("Enter the first number :- "))
        self.num2=int(input("Enter the second number :- "))
        
    def add(self):
        output=self.num1 + self.num2
        result= 'The sum of '+str(self.num1)+' and '+str(self.num2) + ' is '+str(output)
        print(result)
        return result
    
    def subtract(self):
        output=self.num1 - self.num2
        result= 'The difference of '+str(self.num1)+' and '+str(self.num2) + ' is '+str(output)
        print(result)
        return(result)
    
    def multiply(self):
        output=self.num1 * self.num2
        result= 'The product of '+str(self.num1)+' and '+str(self.num2) + ' is '+str(output)
        print(result)
        return result
    
    def divide(self):
        output=self.num1 / self.num2
        result= 'The quotient when '+str(self.num1)+' is divided by '+str(self.num2) + ' is '+str(output)
        print(result)
        return result
    
if __name__=="__main__":
    operation = Calculator(num1=0, num2=0)
    operation.add()
    operation.subtract()
    operation.multiply()
    operation.divide()