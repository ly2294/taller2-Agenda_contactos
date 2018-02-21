
# coding: utf-8

# In[ ]:


#Natalia Isabel Hernandez 
#Leidy Yuliana Quintero
#Jhon Sanchez Buritica
#Inteligencia Artificial


import time  
import os
import getpass

def agenda():
    password = "123456"
    contactos = {}
    salir=True
    while(salir):
        print('\nBienvenido al Menu de  Mi Agenda de Contactos\n')
        print(' 1.) Agregar Contacto\n 2.) Ver Contactos\n 3.) Buscar Contacto\n 4.) Modificar Contacto\n 5.) Eliminar Contacto\n 6.) Salir\n')
        op=input('Digite la opcion que desea ver: ')
        os.system('cls')
        if op == '1': # Agregar contactos
            nombre=input('Nombre: ')
            if nombre in contactos:
                print('Error el contacto ya existe')
                time.sleep(1)
                os.system('cls')
                continue

            try:
                num=int(input('Numero: '))
                if num>9999999999:
                    print('El numero es demaciado largo')
                    time.sleep(1)
                    os.system('clear')
                    continue
                elif num<1000000000:
                    print('El numero es demaciado corto\nDeben de ser 10 digitos')
                    time.sleep(1)
                    os.system('clear')
                    continue
            except:
                print('Valor no valido')
                time.sleep(1)
                os.system('cls')
            contactos[(nombre)] = num
            print('Contacto agregado')
            print(contactos)
            time.sleep(1)
            os.system('cls')
            with open('contactos.txt', 'a') as file:#Agregar contenido al archivo
                file.write("\n")
                file.write("Nombre: "+str(nombre)+" Numero: " + str(num))
                file.close#Cerrar archivo

        elif op == '2': # Ver contactos
            archivo = open('contactos.txt','r')#Abrir archivo para leer el contenido
            for contacto in contactos:
                for num in contactos:
                    print('Contacto / Numero')
                    print( num,contactos[contacto])
            time.sleep(1)
            os.system('cls')
            print(archivo.read())#imprimir lectura
         
        elif op == '3': # Buscar contactos
            buscar=input('Contacto a Buscar: ')
            print (contactos[buscar])
            time.sleep(1)
            os.system('cls')
            if buscar not in contactos:
                print('El contacto no existe., agreguelo desde el menu')
                continue
        elif op == '4': # Modificar contactos
            archivo=open('contactos.txt')
            aux = getpass.getpass("ingrese la contraseña del contacto")
            if aux == password:
                os.system('cls')
                contacto = input('Contacto a modificar: ')
                if contacto not in contactos:
                    print ('El contacto no existe, agreguelo desde el menu')
                    continue
                try:
                    nuevo=int(input('Nuevo Numero: '))
                    contactos[contacto]=nuevo
                    if num>9999999999:
                        print('El numero es de maciado largo')
                        time.sleep(1)
                        os.system('cls')
                        continue
                    elif num<1000000000:
                        print('El numero es muy corto\nDeben de ser 10 digitos')
                    print('Contacto modificado con exito')
                    time.sleep(1)
                    os.system('cls')
                    continue
                except:
                    print('¡Dato no valido!')
                    time.sleep(1)
                    os.system('cls')
                    continue
                    
            else:
                print("contraseña incorrecta")
                os.system('cls')
        elif op == '5': # Eliminar contactos
            aux = getpass.getpass("ingrese la contraseña del contacto")
            if aux == password:
                os.system('cls')
                eliminar=input('Contacto a eliminar: ')
                archivo=open('contactos.txt','r')
                if eliminar not in contactos:
                    print ("El contacto no existe")
                    continue
                del(contactos[eliminar])
                print('Contacto',eliminar,'eliminado con exito')
                time.sleep(1)
                os.system('cls')
                continue
            else:
                print("contraseña incorrecta")
                os.system('cls') 
                linea=archivo.readline()
                print(linea)
        elif op == '6': # Regresar al menu principal
            exit()
        else:
            print('Opcion no valida,\nElija una opcion del 1 al 6')
            time.sleep(1)
            os.system('cls')
            

agenda()

