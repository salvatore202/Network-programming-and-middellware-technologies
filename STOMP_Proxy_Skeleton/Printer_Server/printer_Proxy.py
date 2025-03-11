from iprinter import IPrinter
import socket as sk

BUFFSIZE=1024

class PrinterProxy(IPrinter):

    def __init__(self, host, port):
        self.host=host
        self.port=port

    def print(self, pathFile, tipo):

        #debug
        print("[PROXY] Arrivo funzione print")

        #definiamo e colleghiamo la socket
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.connect((self.host, int(self.port)))

        request = f"{pathFile}-{tipo}"

        s.sendall(request.encode())
        print(f"[PROXY] richiesta di stampa inviata: {request}")

        response = s.recv(BUFFSIZE).decode()

        return response



        