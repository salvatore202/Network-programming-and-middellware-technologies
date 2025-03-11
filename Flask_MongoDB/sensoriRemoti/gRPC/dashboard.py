import sys
import grpc
import statistics_pb2, statistics_pb2_grpc

def run(port):

    #creaiamo il canale gRPC
    channel=grpc.insecure_channel('localhost:' + str(port))

    #ottengo lo stub
    stub=statistics_pb2_grpc.StatisticsManagerStub(channel)

    #recuperiamo i sensori disponibili
    print("[DASHBOARD] Invio richiesta per visualizzare i sensori disponibili...")
    
    #sensors_response=stub.getSensors(statistics_pb2.Empty())
    
    sensors_response=stub.getSensors(statistics_pb2.Empty())


    #creiamo una lista
    sensors=[]

    print("[DASHBOARD] Sensori disponibili:\n")
    for sensor in sensors_response:
        print(f"[DASHBOARD]  sensor_id: {sensor.sensor_id} - data_type: {sensor.data_type}")
        sensors.append(sensor)
                       
    #calcolo della media 
    for sensor in sensors:

        print(f'[DASHBOARD] Sending mean request:  sensor_id: {sensor.sensor_id} - data_type: {sensor.data_type}')

        response = stub.getMean(statistics_pb2.MeanRequest(sensor_id=sensor.sensor_id, data_type=sensor.data_type))

        print(f'[DASHBOARD]     Mean: {response.value}')



# Start client
if __name__ == "__main__":

    try:
        port = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg...")

    run(port)