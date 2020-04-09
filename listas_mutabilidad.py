#LISTAS Y MUTABILIDAD
#Son secuencias de objetos mutables
#Cuando modificamos una lista, puede haber efectos secundarios
#Es posible iterar con ellas

#Ejemplos en consola
my_list = [1, 2, 3]
my_list[0]

my_list[1,:]
#[2, 3]

my_list.append(4)
print(my_list)
#[1, 2, 3, 4]

#agregar
my_list[0] = 'a'
print(my_list)
['a', 2, 3]

#eliminar
my_list.pop()

#iterar
for element in my_list:
  print(element)

#side efects
a = [1, 2, 3]
b = a
id(a)
id(b)
c = [a, b]
a.append(5)

#Clonar listas
a = [1, 2, 3]
id(a)
b = a
#clonar con list
c = list(a)
id(a) != id(c)
#clonar con slices
d = a[::]

#List comprehension
my_list = list(range(100))
double = [i * 2 for i in my_list]

pares = [ i for i in my_list if i % 2 == 0]