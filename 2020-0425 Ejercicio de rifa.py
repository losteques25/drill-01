numero=9 #el numero a acertar
intentos=0 # para decirle a la maquina que arranque desde cero.
lintentos=3 # La cantidad de oportunidades del jugador
print("*** Selecciona un numero del 1 al 9**** ")   
print("*** Solo tienes tres oportunidades de ganar***")
while intentos<lintentos: 
    adivina=int(input("Adivina el numero:    "))
    intentos += 1 # el contador
    if adivina==numero: 
        print("Felicitaciones. Ganastes un millon de dolares")
        break
else:    
    print("Lo sentimos. Será la proxima vez")
   
