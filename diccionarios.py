#DICCIONARIOS
"""
Son listas, pero en lugar de usar indices, usan llaves.
No tienen orden interno
Los diccionarios son mutables
Puede iterarse
"""

my_dict = {
  'David': 35,
  'Erika': 32,
  'Jaime': 50,
}
my_dict['David']
my_dict.get('Juan', 30)

my_dict['Jaime'] = 20

my_dict['Pedro'] = 70

#Borrar
del my_dict['Jaime']

for llave in my_dict.keys():
  print(llave)

for valor in my_dict.values():
  print(valor)

for llave, valor in my_dict.items():
  print(llave, valor)

'David' in my_dict
#True

'Tom' in my_dict
#False