# Importamos los módulos necesarios
from modules import module1
from modules import module2
import threading

# Definimos la lógica principal de la aplicación
def main():
    #ESCALAR VERTICALMENTE
    thread1 = threading.Thread(target=module1.funcion1)
    thread2 = threading.Thread(target=module2.funcion2)

    # Iniciamos los threads
    thread1.start()
    thread2.start()

    # Esperamos a que los threads terminen
    thread1.join()
    thread2.join()

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
