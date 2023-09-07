import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
def connetction (ip):                                           #Перевел в метод 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 55555))
    return s
# client.connect(('127.0.0.1', 55555))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('utf-8')     #Изменил на UTF-8
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

def write():
    while True:

        message = input()               
        if message == 'exit':           # Выход из чата
            client.close()                      
        else:        
            message = f'{nickname}: {message}'  #Изменил на f строку
            client.send(message.encode('utf-8'))


client = connetction('127.0.0.1')

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
