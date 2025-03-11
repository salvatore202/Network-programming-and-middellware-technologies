import stomp

class ColorPrinter(stomp.ConnectionListener):

    def __init__(self):
        pass

    def on_message(self, frame):
        
        request = frame.body

        print(f"[Color Printer] Richiesta di stampa ricevuta : {request}")

        with open("color.txt", "a") as file:

            file.write(request + "\n")

        print("[Color Printer] richiesta salvata su color.txt")

def main():

    #definizmo la connessione 
    conn = stomp.Connection([('localhost', 61613)])

    #set del listener
    listener = ColorPrinter()
    conn.set_listener("", listener)

    #ci colleghiamo 
    conn.connect()

    #sottoscrizione alla coda
    conn.subscribe(destination="/queue/color", id=1, ack="auto")

    #debug
    print("[Color Printer] IN ascolto per tipo color")


    #ciclo infinito che ci permette di restare in ascolto 
    while True:
        pass

if __name__=="__main__":

    main()

