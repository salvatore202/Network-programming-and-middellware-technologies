import stomp, time

class InfoFilter(stomp.ConnectionListener):

    def on_message(self, frame):
        # frame contiene il log ricevuto
        log = frame.body
        tipo = int(log.split("-")[-1])

        # Controlliamo se il log contiene il valore "1"
        if tipo==1:
            print(f"[InfoFilter] Log ricevuto con valore 1: {log}")
            
            # Scriviamo il log nel file info.txt
            with open("info.txt", "a") as file:
                file.write(log + "\n")
            
            print(f"[InfoFilter] Log salvato su info.txt")

    
def main():
        # Funzione principale per avviare InfoFilter

        # Impostiamo la connessione al broker STOMP
        conn = stomp.Connection([("localhost", 61613)])

        # Creiamo un'istanza di InfoFilter
        listener = InfoFilter()

        # Impostiamo il listener per la connessione
        conn.set_listener("", listener)

        # Connessione al broker STOMP
        conn.connect()

        # Sottoscrizione alla coda "info"
        conn.subscribe(destination="/queue/info", id=1, ack="auto")

        print(f"[InfoFilter] In ascolto sulla coda 'info' ")

        # Loop infinito per mantenere la connessione attiva
        while True:
            time.sleep(1)

if __name__ == "__main__":
    main()
