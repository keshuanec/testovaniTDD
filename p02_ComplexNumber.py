"""
https://cs.wikipedia.org/wiki/Komplexn%C3%AD_%C4%8D%C3%ADslo

Definujte třídu ComplexNumber reprezentující komplexní číslo
a definujte následující metody:
- __init__ (konstruktor)
- __eq__ (rovnost)
- __lt__ (<)
- __gt__ (>)
- __repr__  kdyz bubu mit objekt uvnitr neceho jineho, tak se spusti toto
- __str__ kdyz dam print "objekt" tak se mi spusti tahle
- properties (gettery a settery)
- add (sčítání)
- subtract (odečítání)
- multiply (násobení)
- divide (dělení)
- conjugate (číslo komplexně sdružené)
- absolute_value (absolutní hodnota)
"""


class ComplexNumber:
    def __init__(self, real_num, imaginary_num):
        self.real_num = real_num
        self.imaginary_num = imaginary_num

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __repr__(self):
        return f"hodnota komplexniho cisla  je  {self.real_num} + i{self.imaginary_num}"



cislo1 = ComplexNumber(5,6)

print(cislo1)