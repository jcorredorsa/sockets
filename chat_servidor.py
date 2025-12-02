import socket
import threading

def recibir_mensajes(conexion):
    while True:
        try:
            datos = conexion.recv(1024)
            if not datos:
                break
            mensaje = datos.decode("utf-8")
            print("\nCliente:", mensaje)
        except:
            break
    conexion.close()

def iniciar_servidor():
    host = "0.0.0.0"
    puerto = 12345

    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((host, puerto))
    socket_servididor.listen(1)

    print("Servidor iniciado. Esperando conexión...")
    conexion, direccion = socket_servidor.accept()
    print("Conexión establecida con:", direccion)

    hilo_receptor = threading.Thread(target=recibir_mensajes, args=(conexion,), daemon=True)
    hilo_receptor.start()

    try:
        while True:
            texto = input("Tú: ")
            if texto.lower() == "salir":
                conexion.close()
                break
            conexion.send(texto.encode("utf-8"))
    except:
        pass

    socket_servidor.close()
    print("Servidor cerrado.")

if __name__ == "__main__":
    iniciar_servidor()
#python chat_server.py -- pegar eso
