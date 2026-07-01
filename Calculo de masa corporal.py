'''
def bmi(weight, height):
    return weight / height ** 2


print(bmi(40.5, 1.65))
'''

'''
def bmi(weight, height):
    return weight / height ** 2
print(bmi(52.5, 1.65))
'''

'''
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2
print(bmi(352.5, 1.65))
'''

'''
def lb_to_kg(lb):
    return lb * 0.45359237
print(lb_to_kg(1))
'''

'''
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(1, 1))
'''

'''
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(6))



def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2
'''




def calcular_imc(peso, altura):
    # Calcula el IMC usando la fórmula: peso / altura al cuadrado
    return peso / (altura ** 2)

def clasificar_imc(imc):
    # Determina el estado nutricional según el resultado
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def programa_principal():
    print("--- Calculadora de Índice de Masa Corporal (IMC) ---")
    
    # Solicita los datos al usuario
    peso = float(input("Ingresa tu peso en kilogramos (ej. 70.5): "))
    altura = float(input("Ingresa tu altura en metros (ej. 1.75): "))
    
    # Llama a las funciones
    resultado_imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(resultado_imc)
    
    # Muestra los resultados redondeados a dos decimales
    print(f"\nTu IMC es: {resultado_imc:.2f}")
    print(f"Clasificación: {clasificacion}")

# Ejecuta el programa
programa_principal()



print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))




