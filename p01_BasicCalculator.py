class BasicCalculator:

    def add(self, num1, num2):
        if isinstance(num1,str) or isinstance(num2,str):
            return None
        return num1 + num2

    def multiply(self,num1,num2):
        return num1 * num2

