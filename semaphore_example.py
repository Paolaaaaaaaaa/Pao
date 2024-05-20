import threading
import time

#Crear un semaforo con un contador inicial de 2
semaphore = threading.Semaphore(2)

def tarea(id):
    print(f"Tarea {id} intentando acceder al recurso")
    with semaphore:
         print(f"Tarea {id } ha adquirido el semaforo")
         time.sleep(2)
         print(f"Tarea {id} ha liberado el semaforo")
         
#Crear multiplea hilos que ejecute la funcion "tarea".
threads = []
for i in range(5):
    thread = threading.Thread(target=tarea,args=(i,))
    threads.append(thread)
    thread.start()    
#Esperar todos los hilos
for thread in threads:
    thread.join()


  

