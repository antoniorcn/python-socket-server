import socket

class SocketServer:

    def __init__(self, port):
        self.port = port
        self.host = ''

    def run(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (self.host, self.port)
        tcp.bind(orig)
        tcp.listen(1)
        print("Servidor iniciado aguardando conexão do cliente")
        while True:
            con, cliente = tcp.accept()
            print('Concetado por', cliente)
            while True:
                msg = con.recv(128)
                if not msg: break
                print(cliente, str(msg))
                cmd = msg[2:].decode('utf-8')
                print("Converted Message =>", cmd)
            print('Finalizando conexao do cliente', cliente)
            con.close()


if __name__ == "__main__":
    srv = SocketServer(8080)
    srv.run()