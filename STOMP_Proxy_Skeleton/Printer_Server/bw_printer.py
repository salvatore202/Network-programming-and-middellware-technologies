import stomp


class BWPrinter(stomp.ConnectionListener):

    def __init__(self):
        pass

    def on_message(self, frame):
        
        request = frame.body

        #debug
        print(f"[BW Printer] Richiesta di stampa ricevuta : {request}")

        with open("bw.txt", "a") as file:

            file.write(request + "\n")

        print("[BW Printer] richiesta salvata su bw.txt")


def main():

    #connessione al broker stomp
    conn = stomp.Connection([('localhost', 61613)])

    #impostiamo il listener
    listener = BWPrinter()
    conn.set_listener("", listener)

    conn.connect()

    conn.subscribe(destination="/queue/bw", id=1, ack="auto")

    print("[BW Printer] IN ascolto per tipo bw oppure gs")

    while True:
        pass

if __name__=="__main__":
    main()