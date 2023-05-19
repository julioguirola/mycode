#recurso
rep = 0
li = []
xx = 0
#introducir mensaje
mens = input("Introduzca el mensaje: ")
#medir el mensaje para saber si es par o impar
if len(mens) % 2 != 0:
    mens = mens + " "
#convertir el mensaje en una lista
while len(mens) > rep:
    li.append(mens[rep])
    rep = rep + 1
rep = 0   
#encriptar
#intercambiar las posiciones en la lista
while len(mens) > rep:
    saved = li[rep]
    li.insert(rep,li[rep + 1])
    del li[rep + 1]
    li.insert(rep + 1,saved)
    del li[rep + 2]
    rep = rep + 2
#convertir caracteres en numeros
rep = 0 
while len(li) > rep:
    li.insert(rep,(ord(li[rep])+ 99)**2 )
    del li[rep + 1]
    rep = rep + 1
cryp = str(li)
cryp = cryp.replace(',','')
cryp = cryp.replace(' ','')
cryp = cryp.replace('[','')
cryp = cryp.replace(']','')


#mostrar mensaje encriptado
print(cryp)



###desencriptar###
try :
    xx = int(input("introduzca el mensaje encriptado: "))
except :
    print("solo numeros porfavor")
xx = str(xx)
length = len(xx) / 5
rep = 0
repli = 0
repmens = 0
mensaje = ''
mens = ''
while rep < length :
    sli = chr(int((float((xx[repli:repli+5])))**(1/2)-99))
    rep = rep + 1
    repli = repli + 5
    mensaje = mensaje + sli
li = list(mensaje)
rep = 0
while len(li) > rep:
    saved = li[rep]
    li.insert(rep,li[rep + 1])
    del li[rep + 1]
    li.insert(rep + 1,saved)
    del li[rep + 2]
    rep = rep + 2
for a in li :
    mens = mens + a
print(mens)



