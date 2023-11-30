
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary =  self.imaginary + no.imaginary
        return Complex(real, imaginary)
        
    def __sub__(self, no):
        real = self.real - no.real
        imaginary =  self.imaginary - no.imaginary
        return Complex(real, imaginary)
     
    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary =  self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)
 
    def __truediv__(self, no):
        base = no.real * no.real + no.imaginary * no.imaginary
        real = (self.real * no.real + self.imaginary * no.imaginary) / base
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / base
        return Complex(real, imaginary)
 
    def mod(self):
        real = (self.real**2 + self.imaginary**2)**0.5
        return Complex(real, 0.0)


    def __str__(self):
        sign = ["+", ""][self.imaginary < 0]
        return (f"{self.real:.2f}{sign}{self.imaginary:.2f}i")


def main():
    num1 = Complex(*list(map(int, input().split())))
    num2 = Complex(*list(map(int, input().split())))
    # print(num1 + num2)
    # print(num1 - num2)
    # print(num1 * num2)
    # print(num1 / num2)
    # print(num1.mod())
    # print(num2.mod())
    print(*map(str, [num1+num2, num1-num2, num1*num2, num1/num2, num1.mod(), num2.mod()]), sep='\n')

if __name__ == "__main__":
    main()