import subprocess

def ejecutar(comando):
    subprocess.run(comando, shell=True)
option="1"

while option!=6:
    
    print("Menu:")
    print("1. Crear archivo 'misnotas.txt'")
    print("2. Crear carpeta 'calificaciones'")
    print("3. Crear subcarpeta 'primerparcial'")
    print("4. Mover archivo 'misnotas.txt' a la carpeta de 'calificaciones'")
    print("5. Mover programa ćalculadora.py' a la subcarpeta 'primerparcial'")
    print("6. Salir")


    option = input("Selecciona una opcion: ")

    if option == "1":
        ejecutar("touch misnotas.txt") 
    elif option == "2":
        ejecutar("mkdir calificaciones")
    elif option == "3":
        ejecutar("mkdir calificaciones/primerparcial")
    elif option == "4":
        ejecutar("mv misnotas.txt calificaciones/")
    elif option == "5":
        ejecutar("mv Desktop/Calculadora.py calificaciones/primerparcial/")
    elif option == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida. Por favor selecciona una opcion del menu.")
            
    
