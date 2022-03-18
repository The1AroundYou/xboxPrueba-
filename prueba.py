def Conversor(): # Función principal
    decimal = int(input("Introduzca un numero positivo para convertirlo a hexodecimal: ")) # Solicitud al usuario para que introduzca un decimal
    hexadecimal = ""
    while decimal != 0: 
         
        rem = CambiarDigitos(decimal % 16) # Divide entre 16 y guarda el resto
         
        hexadecimal = str(rem) + hexadecimal
        decimal = int(decimal / 16)
    print("Resultado: " + hexadecimal) 
 
def CambiarDigitos(digitos): # Convierte cada digito en su equivalencia hexadecimal
    decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for c in range(7):
        if digitos == decimales:
            digitos = hexadecimal
    return digitos
 
Conversor()