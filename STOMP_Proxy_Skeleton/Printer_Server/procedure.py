#IL produttore deve ricevere le richieste di stampa e inserirle nella coda principale 
#Il consumatore deve prelevare le richieste di stampa dalla coda principale e smistarle nelle relative code STOMP

import multiprocessing as mp
import stomp

#PRODUTTORE
def produzione(server_queue, request):

    print("[PROCEDURE] Arrivo funzione produzione")
    #inseriamo la richiesta nella coda principale
    server_queue.put(request)

    #feedback
    print(f"[Produttore, funzione produzione] Richiesta ricevuta inviata alla coda principale del Server --> {request}")


#CONSUMATORE
def consumazione(server_queue):

    print("[PROCEDURE] Arrivo funzione consumazione")

    #connessione al broker STOMP 
    conn=stomp.Connection([('localhost', 61613)])
    conn.connect()

    while True:

        if not server_queue.empty():

            print("[PROCEDURE] CONSUMAZIONE -> inizio If")

            request=server_queue.get()
            tipo=request.split("-")[-1]

            if tipo=="bw" or tipo=="gs":
                queue_name="bw" 
            
            else:
                queue_name="color"

            #Invio della richiesta alla coda STOMP
            conn.send(destination=f"/queue/{queue_name}", body=request)

            #feedback
            print(f"[Consumatore, funzione consumazione] Richiesta ({request}) prelevata dalla coda del server e inviata alla coda {queue_name}")
