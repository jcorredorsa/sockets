import socket
import threading

def recibir_mensajes(socket_cliente):
    while True:
        try:
            datos = socket_cliente.recv(1024)
            if not datos:
                break
            mensaje = datos.decode("utf-8")
            print("\nServidor:", mensaje)
        except:
            break
    socket_cliente.close()

def iniciar_cliente():
    host = "192.168.0.10"   # Cambiar por la IP del servidor (mi computador en este caso, usar cmd ipconfig)
    puerto = 12345

    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        socket_cliente.connect((host, puerto))
        print("Conectado al servidor.")

        hilo_receptor = threading.Thread(target=recibir_mensajes, args=(socket_cliente,), daemon=True)
        hilo_receptor.start()

        while True:
            texto = input("Tú: ")
            if texto.lower() == "salir":
                socket_cliente.close()
                break
            socket_cliente.send(texto.encode("utf-8"))
    except:
        print("No fue posible conectar al servidor.")

    print("Cliente cerrado.")

if __name__ == "__main__":
    iniciar_cliente()
#python chat_client.py -- pegar eso 
