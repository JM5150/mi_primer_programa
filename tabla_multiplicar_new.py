numero_tabla = int(input("de que numero quieres la tabla de multiplicar?"))

for multiplo in range(5, 16):

    print("{} * {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))