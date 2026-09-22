# Tipo de Triángulos en Python
# Este programa determina el tipo de triángulo basado en las longitudes de sus lados.
# Autor: Andrés Felipe Gutiérrez Rivera
# Fecha: 2024-09-22

# Función para determinar el tipo de triángulo
def tipo_triangulo(lado1, lado2, lado3) -> str:
    # Verificar si los lados forman un triángulo válido
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        # Determinar el tipo de triángulo
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "No es un triángulo válido"


# Función ingresar los lados del triángulo
def ingresar_lados() -> tuple:
    # Solicitar al usuario que ingrese las longitudes de los lados
    lado1 = float(input("Ingrese la longitud del primer lado: "))
    lado2 = float(input("Ingrese la longitud del segundo lado: "))
    lado3 = float(input("Ingrese la longitud del tercer lado: "))
    return lado1, lado2, lado3


# Función para validar que los lados ingresados sean positivos
def validar_lados(lado1, lado2, lado3) -> bool:
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        print("Los lados deben ser números positivos.")
        return False
    return True


# Función resultado para mostrar el tipo de triángulo
def mostrar_resultado(lado1, lado2, lado3) -> str:
    resultado = tipo_triangulo(lado1, lado2, lado3)
    print(f"El triángulo con lados {lado1}, {lado2}, {lado3} es: {resultado}")


# Función principal if __name__ == "__main__":
# Determinar y mostrar el tipo de triángulo
if __name__ == "__main__":
    lado1, lado2, lado3 = ingresar_lados()
    validar = validar_lados(lado1, lado2, lado3)
    if validar:
        mostrar_resultado(lado1, lado2, lado3)
    else:
        print("Por favor, ingrese lados válidos para determinar el tipo de triángulo.")

