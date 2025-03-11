from iprinter import IPrinter
from multiprocessing import Process
import socket as sk

BUFSIZE = 1024

class PrinterSkeleton(IPrinter):

    def __init__(self, server_impl, port):
        self.server_impl=server_impl
        self.port=port

    #metodo dell'interfaccia
    def print(self, pathFile, tipo):

        #delega
        return self.server_impl.print(pathFile, tipo)
    

    def run(self):

        host = 'localhost'

        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

        s.bind((host, self.port))

        s.listen(5)

        #debug message 
        print("[SKELETON] Server in ascolto...")

        while True:
            
            conn, addr = s.accept()

            print(f"[SKELETON] Connessione accettata da {addr}")   

            #definiamo il processo
            Process(target=self.proc_func, args=(conn,)).start()

    #DA COMPLETARE POST IMPLEMENTAZIONE 
    def proc_func(self, conn):

        try:
            print("[PROCESSO] Avviato -> invio messaggio")
            request = conn.recv(BUFSIZE).decode()
            print(f"[SKELETON] Messaggio {request} ricevuto")

            pathFile, tipo = request.split("-")
            result = self.print(pathFile, tipo)
            conn.send(result.encode())
        finally:
            print("[SKELETON] Connessione chiusa ")
            conn.close()


                     

