from ilogging import ILogging
from multiprocessing import Process
import socket as sk

BUFFER_SIZE=1024

class LoggingSkeleton(ILogging):

    def __init__(self, server_impl, port):
        self.server_impl=server_impl
        self.port=port


    def log(self, messaggioLog, tipo):
        # Delega al metodo log del server implementato
        return self.server_impl.log(messaggioLog, tipo)


    def run(self):
        #avvia il Logging Server per accettare richieste dal Client

        host='localhost'

        #definiamo il tipo di socket (TCP)
        s=sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.bind((host, int(self.port)))
        s.listen(5)

        print("[Skeleton] Logging Server in ascolto...")

        while True:
            conn, addr=s.accept()
            print(f"[Skeleton] Connessione accettata da {addr}")

            #avviamo il processo
            Process(target=self.handle_client, args=(conn,)).start()


    def handle_client(self, conn):
        #gestisce le richieste del client

        try:
            log=conn.recv(BUFFER_SIZE).decode() #riceve e decodifica la richiesta del client

            print(f"[Skeleton] Log ricevuto: {log}")

            messageLog, tipo = log.split("-")
            result=self.server_impl.log(messageLog, int(tipo))
            conn.send(result.encode())
        
        finally:
            conn.close()















