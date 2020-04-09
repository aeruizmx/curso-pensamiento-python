# ENUMERACION EXHAUSTIVA
def enumeracion_exhaustiva( objetivo ):
  respuesta = 0
  while respuesta**2 < objetivo:
      respuesta += 1
  if respuesta**2 == objetivo:
      print(f'La razi cuadrada de {objetivo} es {respuesta}')
  else:
      print(f'{objetivo} no tiene una raiz cuadrada exacta')

# APROXIMACION DE SOLUCIONES
def aproximacion( objetivo ):
  epsilon = 0.01
  paso = epsilon**2
  respuesta = 0.0

  while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

  if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
  else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

# BUSQUEDA BINARIA
def busqueda_binaria( objetivo ):
  epsilon = 0.01
  bajo = 0.0
  alto = max(1.0, objetivo)
  respuesta = (alto + bajo) / 2

  while abs(respuesta**2 - objetivo) >= epsilon:
    if respuesta**2 < objetivo:
      bajo = respuesta
    else:
      alto = respuesta
    respuesta = ( alto + bajo ) / 2
  print(f'La raiz cuadrada de {objetivo} es {respuesta}')

#PROGRAMA PRINCIPAL
opcion = int(input('BIENVENIDO AL PROGRAMA DE CALCULO DE RAIZ CUADRADA...\n Selecciona una forma de calculo:\n 1 .- Calcular por Enumeración Exhaustiva\n 2 .- Calcular por Aproximación\n 3 .- Calcular por Busqueda Binaria... '))
if opcion >= 1 and opcion <= 3:
  numero = int( input('Teclea un número para calcular la raiz cuadrada... ') )
  print(f'Calculando raiz para {numero}, espere un momento...')
  if opcion == 1:
    enumeracion_exhaustiva(numero)
  elif opcion == 2:
    aproximacion(numero)
  elif opcion == 3:
    busqueda_binaria(numero)
else:
  print(f'La opción {opcion} es inválida!')
