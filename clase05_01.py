def total_pagar(can_hijos, xsueldo):
    if can_hijos>=0 and xsueldo>=920:
        xboni=0
        if (can_hijos>=0):
            xpor=0.05 *xsueldo
            xboni = xpor * can_hijos
            total=xsueldo +xboni
            return total
    else:
        print('Verificar los datos de entrada')      
          
print('Empresa RHSOFTPERU')
xnom = input('Ingrese nombre: ')
can_hijos =int(input('Ingrese cantidad de hijos: '))
xsueldo = int(input('ingrese sueldo basico: '))
print('El neto a pagar es: ', total_pagar(can_hijos,xsueldo))