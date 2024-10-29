#--------------------------
#boleta de tienda
#--------------------------
#si se vende mas de 10 unidades se aplicara un descuento de 5%
print('------------')
print('Bodega Mass')
print('------------')
xcambio= 3.4
xvendedor='Juan alva'
xpro = input('Ingrese producto: ')
xpre=float(input('Ingrese precio: '))
xcan = int(input('Ingrese cantidad: '))
if xcan >10:
   #hay dsct
   xdes= 0.05
    
else:
    #no hay dsct
    xdes=0
#calcular el importe a pagar
ximporte= xcan *xpre -xdes*xpre*xcan
#mostrar resultados
print('el descuento es: ', xdes*xpre*xcan)
print('total a pagar en soles: ', ximporte)
print('total a pagar en dolares: ', round(ximporte/xcambio,2))
print('*************C A J A******************')
xpago = float(input('Ingrese pago: '))
xmoneda =input('Moneda (S) o (D): ')
print('*******************************')

if (xmoneda.upper=='S'):
    print('El vuelto es : ', round(xpago-ximporte, 2))
else:
    sol = xpago/xcambio #convertir a soles  
    print('El vuelto es: ', round(xpago-ximporte, 2))  
print('*******************************')
print('comision del vendedor')
print('La comision es: ', 0.02*ximporte)
