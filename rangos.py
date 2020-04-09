#Tecleado en CMD

# range( comienzo, fin, pasos)
my_range = range (1,5)
type(my_range)

for i in my_range:
  print(i)

my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)

#Value equality
my_range == my_other_range
#True

for i in my_range:
  print(i)
for i in my_other_range:
  print(i)

  #Direccion
  id(my_range)
  id(my_other_range)

  #Object Equality
  my_range is my_other_range
  #False

  for i in range (0, 101, 2):
    print(i)

#Reto
for i in range (1, 100, 2):
    print(i)
