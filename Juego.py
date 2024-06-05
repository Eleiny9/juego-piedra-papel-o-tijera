import random

cant_jugadas=0
cant_ganadas=0
cant_perdidas=0

while cant_jugadas < 3:
  
  op_user = input("Ingrese una operación (piedra , papel o tijera  ")

  op_user = op_user.lower()

  if op_user !="piedra" and op_user !="papel" and op_user !="tijera":
    print("La opción no es valida")
  else:  
    opcion = ["piedra", "papel", "tijera"]
    op_computer = random.choice(opcion)
  
    print("La computadora eligió: ", op_computer)
  
  
    if op_user == op_computer:
      print ("Empate")
  
    elif op_user == "piedra" and op_computer == "tijera" or op_user == "papel" and op_computer == "piedra" or op_user == "tijera" and op_computer == "papel":
      print ("Ganaste")
      cant_ganadas = cant_ganadas + 1
      
    else:
      print ("Perdiste")
      cant_perdidas = cant_perdidas + 1
  
    cant_jugadas += 1

    if cant_jugadas == 3:
      if cant_ganadas > cant_perdidas:
          print("********* Ganaste el juego ************")
      if cant_ganadas == cant_perdidas:
          print ("********* Empate ************")
      else:
          print("--------- Perdiste el juego -----------")
    
    



