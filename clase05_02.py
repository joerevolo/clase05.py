#------------------------------
#TRAPECIO
#AUTOR : Joe Revolo
#Fecha : 29/10/2024
#------------------------------
print('------------------')
print('Area del trapecio')
print('------------------')
xbmayor=int(input('ingrese base mayor: ')) 
xbmenor=int(input('ingrese base menor: '))
xaltura=int(input('ingrese la altura: '))
#Validar 
if (xbmayor < xbmenor):
    print('Verificar datos de las bases ')
else:    
    xarea =(xbmayor +xbmenor)/2
    print('El area del trapecio es: ', xarea)
