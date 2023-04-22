#Realizar un programa que muestre un menú con opciones de colores primario (Amarillo, azul, rojo, blanco y negro), el usuario debe escoger 2 colores de los ofrecidos en el menú y con una secuencia de if y elif evaluar las posibles combinaciones generadas con los colores primarios. Si el usuario escogió colores que no generan otro al ser combinados debe mostrar un mensaje de“opciones no validas”

print("Menú de colores primarios:")
print("1. Amarillo")
print("2. Azul")
print("3. Rojo")
print("4. Blanco")
print("5. Negro")

color1 = int(input("Elija el primer color (escriba el número correspondiente): "))
color2 = int(input("Elija el segundo color (escriba el número correspondiente): "))

if color1 == 1 and color2 == 2 or color1 == 2 and color2 == 1:
    print("La combinación de amarillo y azul da como resultado el color verde")
elif color1 == 1 and color2 == 3 or color1 == 3 and color2 == 1:
    print("La combinación de amarillo y rojo da como resultado el color naranja")
elif color1 == 2 and color2 == 3 or color1 == 3 and color2 == 2:
    print("La combinación de azul y rojo da como resultado el color morado")
elif color1 == 1 and color2 == 4 or color1 == 4 and color2 == 1:
    print("La combinación de amarillo y blanco da como resultado el color amarillo claro")
elif color1 == 2 and color2 == 4 or color1 == 4 and color2 == 2:
    print("La combinación de azul y blanco no genera otro color primario")
elif color1 == 3 and color2 == 4 or color1 == 4 and color2 == 3:
    print("La combinación de rojo y blanco no genera otro color primario")
elif color1 == 1 and color2 == 5 or color1 == 5 and color2 == 1:
    print("La combinación de amarillo y negro no genera otro color primario")
elif color1 == 2 and color2 == 5 or color1 == 5 and color2 == 2:
    print("La combinación de azul y negro no genera otro color primario")
elif color1 == 3 and color2 == 5 or color1 == 5 and color2 == 3:
    print("La combinación de rojo y negro no genera otro color primario")
elif color1 == 4 and color2 == 5 or color1 == 5 and color2 == 4:
    print("La combinación de blanco y negro no genera otro color primario")
else:
    print("Opciones no válidas")