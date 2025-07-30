# importando el modulo os
import os
from Data.Datos import Lista_menú
from Programas.sumas import sumar2
from Juego.Juegos import Juego_1

#limpiar a terminal
os.system("cls")
estado = True

#Bucle que depende de la variabe estado
while estado:
 print("|+------------------------------------------+|")
 print("|Elizabeth                      2025      v.1|")
 print("|                                            |")
 print(f"|[1] : {Lista_menú[0]}")
 print(f"|[2] : {Lista_menú[1]}")
 print(f"|[3] : {Lista_menú[2]}")
 print(f"|[4] : Juego_1")
 print(f"|[0] : Salir")
 #Respuesta el dato ingresado
 r = int(input("|[?]: "))

 # Pregunta si el dato ingresado es una de las opciones disponibles 
 if r == 0:
  estado = False
 elif r == 1:
  sumar2()
 elif r == 4:
  Juego_1()


 #limpiar a terminal
 #os.system("clear")

 #Código fuera del bucle, se ejecuta si el bucle deja de ser Verdadero 
 print("Saliendo del programa...")
 
