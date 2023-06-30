entradas_vip = [""] * 20
entradas_normales = [""] * 10
entradas_economicas = [""] * 20
asistentes = []
ganancias_vip = 0
ganancias_normales = 0
ganancias_economicas = 0
def mostrar_menu():
  print()
  print("---------------MENU----------------")
  print("1) Comprar Entradas")
  print("2) Mostrar Ubicaciones Disponibles")
  print("3) Ver Listado De asistentes")
  print("4) Mostrar Ganancias totales")
  print("5) Salir")
def mostrar_ubicaciones_disponibles():
  variable_espaciado = 0
  print("Asientos disponibles: ")
  for repeticion in range(len(entradas_vip)):
    variable_espaciado = variable_espaciado + 1
    if(entradas_vip[repeticion]==""):
      if variable_espaciado==11:
        print("")
      print(repeticion+1, end=" ")
    else:
      if variable_espaciado==11:
        print("")
      print("X",end=" ")
  print()
  for repeticion in range(len(entradas_normales)):
    if(entradas_normales[repeticion]==""):
      print(repeticion+21, end=" ")
    else:
      print("X",end=" ")
  print()
  variable_espaciado = 0
  for repeticion in range(len(entradas_economicas)):
    variable_espaciado = variable_espaciado + 1
    if(entradas_economicas[repeticion]==""):
      if variable_espaciado==11:
        print("")
      print(repeticion+31, end=" ")
    else:
      if variable_espaciado==11:
        print("")
      print("X",end=" ")
def comprar_entradas():
  global ganancias_vip
  global ganancias_normales
  global ganancias_economicas
  cantidad = int(input("Ingrese la cantidad de entradas a comprar (1 o 2)"))
  if(cantidad <= 0 or cantidad >= 3):
    print("Error en la cantidad, debe ser 1 o 2")
    return
  print(cantidad)
  for repeticion in range(cantidad):
    print("Ubicaciones disponibles:")
    mostrar_ubicaciones_disponibles()
    ubicacion_valida = False
    while not ubicacion_valida:
      print("")
      ubicacion = int(input("Seleccione una ubicacion: "))
      if ubicacion >= 1 and ubicacion <= 50:
        if ubicacion <= 20 and entradas_vip[ubicacion-1] == "":
          entradas_vip[ubicacion-1] = ingresar_rut()
          ubicacion_valida = True
          ganancias_vip = ganancias_vip + 100000
          asistentes.append(entradas_vip[ubicacion -1])
        elif ubicacion <= 30 and entradas_normales[ubicacion-21] == "":
          entradas_normales[ubicacion-21] = ingresar_rut()
          ubicacion_valida = True
          ganancias_normales = ganancias_normales + 50000
          asistentes.append(entradas_normales[ubicacion -21])
        elif ubicacion <= 50 and entradas_economicas[ubicacion-31] == "":
          entradas_economicas[ubicacion-31] = ingresar_rut()
          ubicacion_valida = True
          ganancias_economicas = ganancias_economicas + 10000
          asistentes.append(entradas_economicas[ubicacion -31])
        if not ubicacion_valida:
          print("No esta disponible")
    print("Operación realizada exitosamente")
def ingresar_rut():
  run_valido = False
  while not run_valido:
    run = input("Ingrese el RUN sin Digito Verificador ni guiones:")
    if(len(run) == 7 or len(run) == 8):
      run_valido = True
  return run
def mostrar_asistentes():
  print("Listado de asistentes")
  asistentes.sort()
  for asistente in asistentes:
    print(asistente, end=".")
def mostrar_ganancias():
  print ("Ganancias por seccion!")
  print (ganancias_vip)
  print (ganancias_normales)
  print (ganancias_economicas)
def inicio():
  try:
    while True:
      mostrar_menu()
      opcion = int(input("Ingrese opcion: "))
      if opcion == 1:
        comprar_entradas()
      elif opcion == 2:
        mostrar_ubicaciones_disponibles()
      elif opcion == 3:
        mostrar_asistentes()
      elif opcion == 4:
        mostrar_ganancias()
      elif opcion == 5:
        print("Gracias por usar el Sofware")
        break
  except:
    print("Ha ocurrido un error")
inicio()
