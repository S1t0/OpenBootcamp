año=int(input("Introduce el año"))


if año %4!=0:
    print(año,"No es año bisiesto")
elif año%4==0 and año%100 !=0:
    print(año,"Es año bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
    print(año,"No es año bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print(año,"Es año bisiesto") 



#Tambien esta el metodo facil, con calendar
import calendar
print(calendar.isleap(año))