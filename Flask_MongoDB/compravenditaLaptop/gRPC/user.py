import sys
import grpc
import threading as mt
import random
import productManager_pb2_grpc
import productManager_pb2

operations=["sell", "buy"]

#funzione associata ad ogni thread
def thread_func(stub):


    operation = operations[random.randint(0,1)]
    
    try:

        if operation=="sell":

            id = random.randint(1, 100)
            result = stub.sell(productManager_pb2.sellRequest(id=id))

            print(f"[USER] Operazione : {operation}-{id} non andata a buon fine" if result==False else None)
    
        else:

            id = stub.buy(productManager_pb2.Empty())
            print(f"[USER] Operazione : {operation}-{id} eseguita")

    except grpc.RpcError as e:
            print(f"[USER] Operazione : {operation} fallita con errore: {e.details()}")



if __name__=="__main__":

    
    #chiediamo la porta da terminale
    try:
        port = sys.argv[1]
    except IndexError:
        print("Please. specify PORT arg...")

    #creiamo il canale gRPC
    channel = grpc.insecure_channel('localhost:' + str(port))
        
    stub = productManager_pb2_grpc.ProductManagerStub(channel)
        
    #creiamo una lista di thread
    threads=[]

    #avviamo 10 thread
    for i in range(1,11):

        #definiamo il thread
        thd = mt.Thread(target=thread_func, args=(stub,))

        #avviamo il thread
        thd.start()

        #aggiungiamo il thread alla coda 
        threads.append(thd)

    for thread in threads:
        thread.join()