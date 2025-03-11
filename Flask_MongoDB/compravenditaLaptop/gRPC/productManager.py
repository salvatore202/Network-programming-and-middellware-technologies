from concurrent import futures
import grpc
import productManager_pb2_grpc, productManager_pb2
import procedure
import requests

server_address = "http://127.0.0.1:5000"

class productManagerService(productManager_pb2_grpc.ProductManagerServicer):

    def __init__(self):
        self.laptop_queue = []


    def notifica_History_server(operation_name, id):

        #prepariamo il messaggio in formato json
        notifica = {
            "operation" : operation_name,
            "serial_number" : id
        }

        #prepariamo l'url che ci porterà all'endpoint desiderato
        resource_location = server_address + "/update_history"

        response = requests.post(resource_location, json=notifica)

        #gestiamo gli errori
        try:
            response.raise_for_status()
        except requests.HTTPError:
            print(f"[NOTIFICA HISTORY SERVER] Errore : {response.status_code} - {response.text}")
        else:
            print(f"[NOTIFICA HISTORY SERVER] Notifica inviata correttamente : {notifica}")


    def sell(self, request, context):

        print("[SERVER->SELL] Arrivo")

        result = procedure.produzione(self.laptop_queue, request.id)

        print("[SERVER->SELL] Produzione fatta")


        #invio notifica all'History Server
        self.notifica_History_server("sell", request.id)

        print("[SERVER->SELL] fine")

        return productManager_pb2.sellResponse(success=result)
            
        

    def buy(self, request, context):

        print("[SERVER->BUY] Arrivo")

        serial_number = procedure.consumazione(self.laptop_queue)

        print("[SERVER->BUY] Consumazione fatta")

        #invio notifica all'History Server
        self.notifica_History_server("buy", serial_number)

        print("[SERVER->BUY] Fine")

        return productManager_pb2.buyResponse(id=serial_number)
    

if __name__ == "__main__":

    # Assegno un'istanza del server gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),))

    # Collego le funzioni della classe al server
    productManager_pb2_grpc.add_ProductManagerServicer_to_server(productManagerService(), server)

    # Assegno dinamicamente una porta
    port = server.add_insecure_port('[::]:0')  # Porta dinamica
    print('Avvio Server Product Manager. In ascolto sulla porta: ' + str(port))

    server.start()

    server.wait_for_termination()