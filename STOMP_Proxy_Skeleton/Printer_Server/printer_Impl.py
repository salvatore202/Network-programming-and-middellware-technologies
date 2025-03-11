from iprinter import IPrinter
import procedure
from printer_Skeleton import PrinterSkeleton
from multiprocessing import Queue, Process

class PrinterService(IPrinter):

    def __init__(self):
        self.queue=Queue()

    def print(self, pathFile, tipo):

        #debug
        print("\n[SERVER] Arrivo funzione print")

        request = f"{pathFile}-{tipo}"
        procedure.produzione(self.queue, request)

        #debug
        print("[SERVER] Fine funzione print")

        return (f"[SERVER] Richiesta {request} inserita in coda")
    
    def start(self, port):

        skeleton = PrinterSkeleton(self, port)
        
        #avviamo il processo consumatore
        Process(target=procedure.consumazione, args=(self.queue,)).start()

        #avviamo il server con lo skeleton
        skeleton.run()

if __name__=="__main__":

    server = PrinterService()

    server.start(5000)



        
