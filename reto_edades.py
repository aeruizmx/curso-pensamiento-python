usuario_1 = input('¿Cual es el nombre del primer usuario? ')
edad_1 = int(input(f'¿Cuantos años tiene {usuario_1} ? '))
usuario_2 = input('¿Cual es el nombre del segundo usuario? ')
edad_2 = int(input(f'¿Cuantos años tiene {usuario_2} ? '))

if edad_1 > edad_2:
  print(f'{usuario_1} es mayor que {usuario_2}')
elif edad_1 < edad_2:
  print(f'{usuario_2} es mayor que {usuario_1}')
else:
  print(f'{usuario_1} y {usuario_2} tienen la misma edad')