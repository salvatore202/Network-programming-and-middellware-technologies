import grpc
import statistics_pb2
import statistics_pb2_grpc
from pymongo import MongoClient

from concurrent import futures

#funzione di collegamento al database MongoDB 
def get_database():

    client=MongoClient("127.0.0.1", 27017)
    
    return client['sensors_data']

class StatisticsServicer(statistics_pb2_grpc.StatisticsManagerServicer):

    def __init__(self, db):
        self.db=db

    
    #Funzione per ricavare i dati dei sensori registrati nel DB
    def getSensors(self, request, context):

        print("[GET SENSORS] Acquisendo i sensori dal DB")

        #recuperiamo la collection MongoDB con i sensori
        sensor_collection=self.db['sensors']


        #recuperiamo i dati dala collection
        results=sensor_collection.find()

        #stampiamo i risultati
        for result in results:

            print("[GET SENSORS] Get sensor: " + str(result))

            #gestiamo il caso di campi non presenti
            try:
                sensor_id=result['_id']
                data_type=result['data_type']
            except Exception as e:
                print("[GET SENSORS] Failed retrieving one of the required field...skipping the data")
                print("[GET SENSORS] Obtaianed - " + str(result))
                continue

            yield statistics_pb2.Sensor(sensor_id=sensor_id, data_type=data_type)


    #Prevede in input un MeanRequest(statistics_pb2.pyi) e ritorna uno StringMessage
    def getMean(self, request, context):

        #estraiamo i dati del sensore da Meanrequest (request)
        sensor_id=request.sensor_id
        data_type=request.data_type

        print(f"[GET MEAN] Richiesta ricevuta per sensor_id: {sensor_id} - data_type: {data_type} ")

        #inizializziamo la collection
        collection=None

        #assegniamo un valore alla collection 
        if data_type=="temp":
            collection=self.db['temp_data']  #collection delle misurazioni temp
        elif data_type=="press":
            collection=self.db['press_data']  #collection delle misurazioni press
        else:
            return statistics_pb2.StringMessage(value='-1')


        results=collection.find({'sensor_id':sensor_id})
    
        #media
        mean=0

        #numero di elementi
        elem=0

        for result in results:
            try:
                mean = mean + result['data']
                elem = elem + 1
            except Exception as e:
                print("[GET MEAN] Failed retrieving one of the required field...skipping the data")
                print("[GET MEAN] Obtaianed - " + str(result))
                continue

        #calcolo della media
        mean = mean/elem

        #stampa
        print("[GET MEAN] Media = " + str(mean))

        return statistics_pb2.StringMessage(value=str(mean))


if __name__=="__main__":

    #prendiamo il database
    db=get_database()

    #assegniamo a server un istanza del server gRPC, specificando la configurazione
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),))

    #colleghiamo l'implementazione delle funzioni della classe al server
    statistics_pb2_grpc.add_StatisticsManagerServicer_to_server(StatisticsServicer(db), server)

    #inizializziamo la porta
    port = 0

    port = server.add_insecure_port('[::]:' + str(port))
    print("Avvio Server. IN ascolto sulla porta " + str(port))

    server.start()

    server.wait_for_termination()

    


















