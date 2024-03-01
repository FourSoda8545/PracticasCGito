# Practica17

#Prcatica17 = Series imprimir y decir la suma total
#1) 2, 4, 6, 8, 10, 12
#2) 3, 6, 9, 12, 15, 18
#3) 3, 4, 6, 8, 9, 12
#4) 1, 2, 3, 5, 8, 13
#5) 1, 2, 3, 6, 11, 20

suma=2
for x in range(13):
	print("x: ",x)
	print("valor suma : ",suma)
	suma+=x #suma = suma+x
	print("nuevo valor suma :",suma)
	print("-------------------------------------------------------")