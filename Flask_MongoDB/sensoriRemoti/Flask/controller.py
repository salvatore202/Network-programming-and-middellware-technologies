from flask import Flask, request
from pymongo import MongoClient

app=Flask(__name__)

#funzione per connettersi  al MongoDB
def get_database():

    client=MongoClient("127.0.0.1", 27017)

    return client['sensors_data']


#ENDPOINT PER INSERIRE MISURAZIONI
@app.post('/data/<data_type>')
def store_data(data_type):

    #prendiamo la richiesta arrivata a questo endpoint
    body=request.get_json()

    #ci colleghiamo al database
    db=get_database()

    #selezioniamo la collection in base al data_type
    if data_type=="temp":
        data_collection=db['temp_data']
    elif data_type=="press":
        data_collection=db['press_data']
    else:
        #errore->tipo di dato non supportato
        return {'result':'Unsupported data type'}, 400

    #inseriamo il dato nel MongoDB e gestiamo le eccezioni
    try:
        data_collection.insert_one(body)
    except Exception as e:
        print("[CONTROLLER->stored_data] Operazione Fallita")
        return {'result': 'failed - '+str(e)}, 500
    else:
    #se l'operazione è andata a buon fine 
        print(f"[CONTROLLER->stored_data] Operazione Eseguita con Successo - {data_type} salvato sul DB")
        return {'result': 'success'}


#ENDPOINT PER INSERIRE SENSORI
@app.post('/sensor')
def add_sensor():

    #prendiamo la richiesta arrivata a questo endpoint
    body=request.get_json()

    #ci colleghiamo al database
    db=get_database()

    #specifichiamo la collection di dati del MongoDB
    sensor_collection=db['sensors']

    #inseriamo il sensore nel MongoDB e gestiamo le eccezioni 
    try:
        sensor_collection.insert_one(body)
    except Exception as e:
        print("[CONTROLLER->add_sensor] Operazione Fallita")
        return {'result': 'failed - '+str(e)}, 500
    else:
    #se l'operazione è andata a buon fine 
        print("[CONTROLLER->add_sensor] Operazione Eseguita con Successo - Nuovo sensore registrato sul DB")
        return {'result': 'success'}


if __name__  == "__main__":

    app.run(debug=True)












































    