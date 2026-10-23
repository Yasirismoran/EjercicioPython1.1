nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
print("Nombre:", nombre)
print("Edad:", edad)
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print("Promedio:", promedio)

if promedio >= 71:
    print("Aprobado")
else:
    print("No aprobado")
