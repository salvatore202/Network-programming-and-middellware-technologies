import requests, random 
import threading as mt


supported_types=['temp', 'press']
server_address="http://127.0.0.1:5000"

N_REQ=5

#funzione di ogni thread
def thread_func(sensor_id):
    
    #selezioniamo in maniera casuale il tipo di sensore da aggiungere
    data_type=supported_types[random.randint(0,1)]

    #strutturiamo la richiesta json per la registrazione del sensore 
    sensor_spec={
        '_id' : sensor_id,
        'data_type' : data_type
    }

    #prepariamo l'url per la richiesta che ci porterà all'endpoint [CONTROLLER->add_sensor]
    resource_location=server_address+"/sensor"

    #inviamo la richiesta 
    response=requests.post(resource_location, json=sensor_spec)

    #gestiamo eventuali errori
    try:
        response.raise_for_status()
    except requests.exception.HTTPError:
        print(f"[SENSOR-{sensor_id}] Errore : {response.status_code} - {response.text}")
    else:
    #non ci sono errori
        print(f"[SENSOR-{sensor_id}] Sensore registrato corretamente con : {sensor_spec}")

    
    #Una volta registrato il sensore, inviamo al controller delle ipotetiche misurazioni del sensore appena registrato

    #Richieste multiple
    for i in range(N_REQ):

        #generiamo dati casuali e prepariamo il json da inviare 
        data={
            'sensor_id' : sensor_id,
            'data' : random.randint(1,50)
        }

        #prepariamo l'url per la richiesta che ci porterà all'endpoint CONTROLLER->store_data
        resourse_location=server_address+"/data/"+data_type

        #inviamo la richiesta
        response=requests.post(resourse_location, json=data)

        #gestiamo eventuali errori
        try:
            response.raise_for_status()
        except requests.exception.HTTPError:
            print(f"[SENSOR-{sensor_id}] Errore : {response.status_code} - {response.text}")
        else:
        #non ci sono errori
            print(f"[SENSOR-{sensor_id}] Dato {data_type} aggiunto : {data}")
            


if __name__=="__main__":

    #creiamo una lista di thread
    threads=[]

    #avvio i thread
    for i in range(1,6):
        
        #definiamo il thread
        thd=mt.Thread(target=thread_func, args=(i,))

        #avviamo
        thd.start()

        #aggiungiamo alla coda
        threads.append(thd)

    for thread in threads:
        thread.join()
































