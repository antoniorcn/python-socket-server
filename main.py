import jpysocket
import socket
import time
# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522

class DeviceServer:

    def __init__(self, port):
        # self.reader = SimpleMFRC522()
        self.host = 'localhost'  # Host Name
        self.port = port

    def read_rfid(self):
        try:
            id, text = self.reader.read()
            print(id)
            print(text)
            return id, text
        finally:
            pass
            # GPIO.cleanup()

    def run(self):
        s = socket.socket()  # Create Socket
        s.bind((self.host, self.port))  # Bind Port And Host
        s.listen(5)  # Socket is Listening
        print("Socket Is Listening....")
        connection, address = s.accept()  # Accept the Connection
        print("Connected To ", address)
        msgsend = jpysocket.jpyencode("Connected to RaspBerry Moonsoft Device")  # Encript The Msg
        connection.send(msgsend)  # Send Msg
        msgsend = jpysocket.jpyencode("Wait for commands")  # Encript The Msg
        connection.send(msgsend)  # Send Msg
        while True:
            cmdrecv = connection.recv(1024)  # Recieve msg
            print("Lido :", cmdrecv)
            cmdstr = jpysocket.jpydecode(cmdrecv)  # Decript msg
            print("Command received:", cmdstr)
            if cmdstr == "READ-RFID":
                print("Executando leitura do RFID")
                msgsend = jpysocket.jpyencode("Dados do RFID: 123456")  # Encript The Msg
                connection.send(msgsend)  # Send Msg
            elif cmdstr == "OPEN-DOOR":
                print("Abrindo a porta")
                msgsend = jpysocket.jpyencode("Porta Aberta")  # Encript The Msg
                connection.send(msgsend)  # Send Msg
            elif cmdstr == "RETRIEVE-CAMERA":
                print("Enviando imagem da camera")
                msgsend = jpysocket.jpyencode("Dados da camera: B1F4C2")  # Encript The Msg
                connection.send(msgsend)  # Send Msg
            elif cmdstr == "QUIT":
                print("Encerrando")
                break
            time.sleep(1)

        s.close()  # Close connection
        print("Connection Closed.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    device = DeviceServer(8080)
    device.run()

