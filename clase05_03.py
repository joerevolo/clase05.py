def contar_vocal(frase,vocal):
    xc =0 #inicializar la variable
    can_caracteres =len(frase)#cantidad de caracteres 
    for i in range (0, can_caracteres):
        if frase [i]== vocal:
            xc =xc+1
    return xc

xfrase =input('ingrese frase: ')
xvocal = input('ingrese vocal: ')
print('La cantidad de la vocal: ', xvocal ,'es ' , contar_vocal(xfrase,xvocal))
