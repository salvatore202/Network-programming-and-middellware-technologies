from threading import Lock

QUEUE_MAX_SIZE=5

lock = Lock()

#PRODUTTORE
def produzione(laptop_queue, id):

    print("[PRODUZIONE] Arrivo")

    with lock:
        if len(laptop_queue)<QUEUE_MAX_SIZE:
            laptop_queue.append(id)
            print(f"[PRODUZIONE] Laptop con id : {id} inserito nella coda ")
            return True
        else:
            print(f"[PRODUZIONE] La coda è piena, impossibile inserire il laptop con id: {id}")
            return False
    
   

#CONSUMATORE
def consumazione(laptop_queue):

    print("[CONSUMAZIONE] Arrivo")

    with lock:
        if laptop_queue:
            id = laptop_queue.pop(0)
            print(f"[CONSUMAZIONE] Laptop con id : {id} Venduto ")
            return id
        else:
            return None

