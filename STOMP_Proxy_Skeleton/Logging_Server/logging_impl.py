from logging_Skeleton import LoggingSkeleton
from ilogging import ILogging
from procedure import produzione, consumazione
from multiprocessing import Queue, Process

class LoggingServer(ILogging):

    def __init__(self):
        self.queue=Queue()


    def log(self, messaggioLog, tipo):
        #inserisce un log nella coda principale del LoggingServer

        log=f"{messaggioLog}-{tipo}"
        produzione(self.queue, log)

        return "[LoggingServer] Log ricevuto "
    
    
    def start(self, port):
        #avvia il server utilizzando lo Skeleton

        skeleton=LoggingSkeleton(self, port)
        Process(target=consumazione, args=(self.queue,)).start()
        skeleton.run()


if __name__=="__main__":
    server=LoggingServer()
    server.start(5000)