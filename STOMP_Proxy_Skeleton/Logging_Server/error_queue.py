import stomp

class ErrorChecker(stomp.ConnectionListener):

    def __init__(self, filtro):
        self.filtro=filtro

    
    def on_message(self, frame):
        #frame contiene il log ricevuto

        log=frame.body
        
        if self.filtro in log or log.split("-")[-1]==2:
            print(f"[ErrorChecker] Log di errore ricevuto")

            with open("error.txt", "a") as file:

                #scriviamo il Log sul file error.txt
                file.write(log+"\n")
            
            print(f"[ErrorChecker] Log salvato su error.txt")
    

def main(filtro):
        #funzione principale per avviare ErrorChecker

        #set della connesione al broker STOMP
        conn=stomp.Connection([("localhost", 61613)])

        #creiamo un'istanza di ErrorChecker
        listener=ErrorChecker(filtro)

        conn.set_listener("", listener)

        #connessione al broker STOMP
        conn.connect()

        #sottoscrizione alla coda errore
        conn.subscribe(destination="/queue/error", id=1, ack="auto")

        print(f"[ErrorChecker] In ascolto per tipo {filtro}")

        while True:
            pass

    
if __name__=="__main__":
        import sys
        filtro=sys.argv[1]
        main(filtro)
