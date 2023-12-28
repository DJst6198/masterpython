import math
import unittest

# Calculo de areas:
def area_circulo(radio):
    """
    Calcula el area de un circulo.

    Parameters:
    - radio (float): El radio del circulo.

    Returns:
    float: El area del circulo.
    """
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    """
    Calcula el area de un triangulo.

    Parameters:
    - base (float): La longitud de la base del triangulo.
    - altura (float): La altura del triangulo.

    Returns:
    float: El area del triangulo.
    """
    return 0.5 * base * altura

def area_cuadrado(lado):
    """
    Calcula el area de un cuadrado.

    Parameters:
    - lado (float): La longitud de un lado del cuadrado.

    Returns:
    float: El area del cuadrado.
    """
    return lado ** 2

#Calculo de volumenes:
def volumen_esfera(radio):
    """
    Calcula el volumen de una esfera.

    Parameters:
    - radio (float): El radio de la esfera.

    Returns:
    float: El volumen de la esfera.
    """
    return (4/3) * math.pi * radio ** 3

def volumen_cubo(lado):
    """
    Calcula el volumen de un cubo.

    Parameters:
    - lado (float): La longitud de un lado del cubo.

    Returns:
    float: El volumen del cubo.
    """
    return lado ** 3

def volumen_piramide(nlados,lado,apotema,altura):
    """
    Calcula el volumen de una piramide con base poligonal.

    Parameters:
    - nlados (int): El numero de lados de la base de la piramide.
    - lado (float): La longitud de un lado de la base de la piramide.
    - apotema (float): La apotema de la base de la piramide.
    - altura (float): La altura de la piramide.

    Returns:
    float: El volumen de la piramide.
    """    
    
    if(nlados == 3):
        volumen = (((lado*apotema)/2) * altura)/3
    
    elif (nlados == 4):
        volumen = ((lado**2)*altura)/3

    else:
        volumen = ((((lado * nlados)*apotema)/2)*altura)/3

    return volumen

#Selector de opciones
print("CALCULO DE AREAS Y VOLUMENES:")
print(f"1: Calcular el area de un circulo")
print(f"2: Calcular el area de un triangulo")
print(f"3: Calcular el area de un cuadrado")
print(f"4: Calcular el volumen de una esfera")
print(f"5: Calcular el volumen de un cubo")
print(f"6: Calcular el volumen de una piramide")

while True:
    try:
        opcion = int(input("Introduce el numero de la opcion que quieras ejecutar: "))
        if (1 <= opcion <= 6):
            break
        else:
            print(f"Tienes que introducir un numero del 1 al 6")

    except ValueError as error:
        print("Debes introducir un numero del 1 al 6")


if(opcion == 1):
    while True:
        try:
            radio = float(input("Tamano del radio del circulo: "))
            
            if (radio < 0):
                print("Debes introducir un numero positivo")
                
            else:
                break

        except ValueError as error:
            print("Debes introducir un numero")
    
    print(f"Area del circulo definido: {area_circulo(radio)}")

elif(opcion == 2):
    while True: #no funciona
        try:
            base = float(input("Tamano de la base del triangulo: "))
            altura = float(input(f"Tamano de la altura del triangulo: "))
            
            if (base < 0 or altura < 0):
                print("Debes introducir numeros positivos")
            
            else:
                break

        except ValueError as error:
            print(f"Debes introducir un numero") #revisar porque me da error.

    print(f"Area del triangulo definido: {area_triangulo(base, altura)}")

elif(opcion == 3):
    while True:
        try:
            lado = float(input("Tamano del lado del cuadrado: "))
            
            if (lado < 0):
                print("Debes introducir un numero positivo")
            
            else:
                break

        except ValueError as error:
            print(f"Debes introducir un numero") #revisar porque me da error.
    
    print(f"Area del cuadrado definido: {area_cuadrado(lado)}")

elif(opcion == 4):
    while True:
        try:
            radio = float(input("Tamano del radio del circulo: "))
            
            if (radio < 0):
                print("Debes introducir un numero positivo")
            
            else:
                break

        except ValueError as p:
            print(f"Debes introducir un numero")
   
    print(f"El volumen de la esfera definida es: {volumen_esfera(radio)}")

elif(opcion == 5):
    while True:
        try:
            lado = float(input("Tamano del lado del cuadrado: "))
            
            if (lado < 0):
                print("Debes introducir un numero positivo")
            
            else:
                break

        except ValueError as p:
            print(f"Debes introducir un numero")
    
    print(f"El volumen del cubo es: {volumen_cubo(lado)}")

else:
    while True:
        try:
            nlados = int(input("Numero de lados que tiene la base de la piramide: "))
            if (nlados > 2):
                break
            else:
                print(f"Tienes que introducir un numero entero mayor a 2")

        except ValueError as error:
            print("Debes introducir un numero entero mayor a 2")
    
    while True:
        try:
            lado = float(input("Tamano del lado de la base de la piramide: "))
            apotema = float(input("Tamano de la apotema de la base de la piramide: "))
            altura = float(input("Tamano de la altura de la piramide: "))
            
            if (lado < 0 or apotema < 0 or altura < 0):
                print("Debes introducir un numero positivo")
            
            else:
                break

        except ValueError as p:
            print(f"Debes introducir un numero")

    print(f"El volumen de la piramide definida es: {volumen_piramide(nlados,lado,apotema,altura)}")
    

# Pruebas unitarias
class TestGeometricCalculations(unittest.TestCase):
    def test_area_circulo(self):
        self.assertAlmostEqual(area_circulo(5), 78.54, places=2)
        self.assertEqual(area_circulo(0), 0)
        self.assertAlmostEqual(area_circulo(2.5), 19.63, places=2)

    def test_area_triangulo(self):
        self.assertEqual(area_triangulo(4, 6), 12)
        self.assertEqual(area_triangulo(0, 8), 0)
        self.assertEqual(area_triangulo(3.5, 7), 12.25)

    def test_area_cuadrado(self):
        self.assertEqual(area_cuadrado(3), 9)
        self.assertEqual(area_cuadrado(0), 0)
        self.assertEqual(area_cuadrado(4.5), 20.25)

    def test_volumen_esfera(self):
        self.assertAlmostEqual(volumen_esfera(3), 113.1, places=1)
        self.assertEqual(volumen_esfera(0), 0)
        self.assertAlmostEqual(volumen_esfera(2.5), 65.45, places=1)

    def test_volumen_cubo(self):
        self.assertEqual(volumen_cubo(4), 64)
        self.assertEqual(volumen_cubo(0), 0)
        self.assertAlmostEqual(volumen_cubo(3.5), 42.88, places=1)

    def test_volumen_piramide(self):
        self.assertAlmostEqual(volumen_piramide(3, 5, 2, 8), 13.333, places=3)
        self.assertEqual(volumen_piramide(4, 0, 3, 6), 0)
        self.assertEqual(volumen_piramide(5, 4.5, 1, 10), 37.5)

if __name__ == '__main__':
    unittest.main()