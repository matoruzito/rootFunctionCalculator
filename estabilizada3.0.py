from sympy import *
import math
from matplotlib import pyplot

salida = False

while(salida == False):
	x = symbols('x')
	funcion = input("Ingresa la funcion:")			#Obtengo la función del usuario. 
	funcion = sympify(funcion)						#Evito que sea string lo que está en la variable
	derivada = diff(funcion)						#Derivo la función 
	dobleDer = diff(derivada)						#Doblederivo para testear convergencia

	#Entre lineas: Seteo correcto de variables para su utilización posterior----------------------------

	convergenciaAck = False



	#---------------------------------------------------------------------------------------------------

	#mientras que el punto no sea el correcto, le pediremos puntos al usuario
		

	while (convergenciaAck == False):
		pInicial = input("Ingresá punto inicial")
		pInicial = sympify(pInicial)
		funcion_en_pInicial = funcion.subs(x, pInicial)
		derivada_pInicial = derivada.subs(x, pInicial)
		doble_derivada_pInicial = dobleDer.subs(x, pInicial)

		#Test convergencia 
		a = (funcion_en_pInicial * doble_derivada_pInicial) / (derivada_pInicial ** 2)
		
		convergencia = abs(a)
		
		if(math.isnan(convergencia) == True):
			convergenciaAck = False
			print("No converge en ese punto. Tendrás que elegir otro...:")

		else:
			if(convergencia < 1):
				convergenciaAck = True
			else:
				convergenciaAck = False 
				print("No converge en ese punto. Tendrás que elegir otro...:")




	#Si el programa llegó aquí quiere decir que la funcion es convergente en ese punto, sou podemos hacer N-R
	#Mientras que la función del punto obtenido no sea menor que la tolerancia que deseamos, seguirá iterando.

	funcion_en_pObtenido = funcion_en_pInicial

	cantIteraciones = 0

	while(abs(funcion_en_pObtenido) > 0.00000001):
		cantIteraciones = cantIteraciones + 1 
		funcion_en_pInicial = funcion.subs(x, pInicial)
		derivada_pInicial = derivada.subs(x, pInicial)

		b = funcion_en_pInicial / derivada_pInicial
		b = float(b)

		pObtenido = pInicial - b

		print("Iteracion numero:")
		print(cantIteraciones)
		print("Punto obtenido: ")
		print(pObtenido)
		
		funcion_en_pObtenido = funcion.subs(x, pObtenido)

		if(abs(funcion_en_pObtenido) > 0.00000001):
			pInicial = pObtenido  			#Esto es para que se continúe iterando	
		


	print("La raiz mas proxima a tu punto es: ")
	pObtenido = round(pObtenido, 5)
	print(pObtenido)


	print("Mira el grafico: ")

	#A partir de aquí se programa la graficación de la funcion. 




	rango = 2 * abs(pObtenido)
	rangoMin = rango - (rango * 2)
	rangoMax = rango
	rangoMin = int(rangoMin)
	rangoMax = int(rangoMax)

	#Hay que generar todos los puntos y correspondientes al rango de x 

	nX = range(rangoMin, rangoMax)

	#no funco >>  pyplot.plot(x, [funcion.subs(x, i) for i in nX])
	
	counter = rangoMin

	arrayX = []
	arrayY = []


	while(counter <= rangoMax):
		arrayX.append(counter)
	
		arrayY.append(funcion.subs(x, counter))
		counter = counter + 1
	



	
	pyplot.plot(arrayX, arrayY, color = "#B40404")




	pyplot.axhline(0, color="black")		#Color de los ejes
	pyplot.axvline(0, color="black")		#Color de los ejes

	#Obtengo cual es el maximo y el minimo en y 

	rangoYmax = 10
	rangoYmin = -10

	rangoYmax = int(rangoYmax)
	rangoYmin = int(rangoYmin)


	pyplot.xlim(rangoMin, rangoMax)
	pyplot.ylim(rangoYmin, rangoYmax)	

	pyplot.savefig("output.png")
	pyplot.show()




	


	user_decide = input("Para salir poné 1 y despues dos veces enter, para ingresar otra funcion poné 2")
	if(user_decide == 1):
		salida = True
	elif(user_decide == 2):
		salida = False







		