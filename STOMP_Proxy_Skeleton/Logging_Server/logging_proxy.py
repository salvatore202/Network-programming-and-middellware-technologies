from ilogging import ILogging
import socket as sk

class LoggingProxy(ILogging):

    def __init__(self, host, port):
        self.host=host
        self.port=port

    def log(self, messageLog, tipo):
        #invia il messaggio di log al server che provvederà a smistarlo nella rispettiva coda 

        #definiamo la socket
        s=sk.socket(sk.AF_INET, sk.SOCK_STREAM)

        #colleghiamo la socket al Server 
        s.connect((self.host, int(self.port)))
        
        log=f"{messageLog}-{tipo}"

        #inviamo il log codificato
        s.sendall(log.encode())
        print(f"[Proxy] Log inviato: {log}")

        response = s.recv(1024).decode()
        print(f"[Proxy] Risposta ricevuta: {response}")

        return response 