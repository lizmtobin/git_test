class Powers:
#multiply to the power of
#input power of
    def __init__(self, powerOf):
        self.powerOf = powerOf

    def multipleOf(self, num1):
        result = num1**self.powerOf
        return result

pof = int(input("Enter number to use as a power: "))
powerBy10 = Powers(10)

calc = powerBy10.multipleOf(pof)

print(calc)