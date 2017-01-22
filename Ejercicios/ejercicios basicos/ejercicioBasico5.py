#Escribe un programa que calcule lo que tiene que cobrar un empleado sabiendo
#que se le tiene que aplicar al sueldo una retención del 20%.

sueldo = int(input("sueldo al que aplicar retencion"))

sueldoConRetencion = sueldo - (sueldo*0.2)

print(sueldoConRetencion)
