import argparse

class Calculator:
    
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
        
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
    
    # Initialize Parser
    parser = argparse.ArgumentParser(description='Calculator Arguments')
    
    # Adding arguments
    parser.add_argument('-num1', '--number1', required=True, type=float, help='Enter an integer for first number')
    parser.add_argument('-num2', '--number2', required=True, type=float, help='Enter an integer for second number')
    
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    
    operation = Calculator(args.number1, args.number2)
    operation.add()
    operation.subtract()
    operation.multiply()
    operation.divide()