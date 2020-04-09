# Tecleado en cmd

my_tuple = ()
type(my_tuple)

#Reasignar tupla
my_tuple = (1, 'dos', True)
my_tuple[0]
my_tuple[1]
my_tuple[2]

#No se puede reasignar valor
my_tuple[0] = 2

#Tuplas con un solo valor se deben añadir comas
my_tuple = (1,)
type(my_tuple)

#Sumar tuplas, se reasigna
my_other_tuple = (2,3,4)
my_tuple += my_other_tuple
print(my_tuple)

#Desempaquetar valores
x,y,z = my_other_tuple

#Regresar varios valores
def coordenadas():
  return (5,4)

coordenada = coordenadas()
x,y = coordenadas()
