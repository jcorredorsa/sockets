# Proyecto: Chat con Sockets en Python

Este repositorio implementa un sistema de comunicación cliente-servidor utilizando **sockets en Python**. El objetivo es mostrar cómo establecer comunicación entre múltiples clientes y un servidor central, aplicando conceptos de **redes, concurrencia y arquitectura cliente-servidor**.

## Estructura del repositorio
```
sockets/
│── chat_servidor.py   # Lógica del servidor
│── chat_cliente.py    # Lógica del cliente
│── README.md          # Documentación del proyecto


## Ejecución

### 1. Iniciar el servidor
En una terminal:
```bash
python chat_servidor.py
```
El servidor quedará a la espera de conexiones en el puerto definido (por defecto `5000`).

### 2. Conectar clientes
En otra terminal (o en diferentes equipos de la red):
```bash
python chat_cliente.py
```
Cada cliente podrá enviar mensajes que serán recibidos por el servidor y reenviados a los demás.


## Ejemplo de uso
1. Ejecutar el servidor en la máquina principal.  
2. Abrir dos clientes en diferentes terminales.  
3. Enviar mensajes desde cada cliente y observar cómo se transmiten a todos los conectados.  


## Conceptos aplicados
- **Sockets TCP/IP**: comunicación confiable entre procesos.  
- **Concurrencia**: manejo de múltiples clientes simultáneamente.  
- **Arquitectura cliente-servidor**: separación clara de responsabilidades.  
- **Validaciones básicas**: control de conexiones y mensajes.  



Desarrollado por Juan Sebastián Corredor Sáenz 

