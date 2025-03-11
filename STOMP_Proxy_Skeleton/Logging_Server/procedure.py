import multiprocessing as mp
import stomp

"PROD"
def produzione(queue, log):
    queue.put(log)
    print(f"[Produzione] Prodotto: {log}")


"CONS"
def consumazione(queue):
    
    conn=stomp.Connection([('localhost', 61613)])
    conn.connect()

    while True:
        if not queue.empty():
            log=queue.get()
            tipo=log.split("-")[-1]

            queue_name="error" if tipo=="2" else "info"

            conn.send(destination=f"/queue/{queue_name}", body=log)
            print(f"[Consumazione] Inviato a coda {queue_name}: {log}")