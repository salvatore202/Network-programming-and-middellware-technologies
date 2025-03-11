from printer_Proxy import PrinterProxy
import random, time

tipi = ["bw", "gs", "color"]
estensioni = ["doc", "txt"]
N_REQUEST = 10

def main():

    #debug
    print("\n[USER] Inizio funzione main")

    for _ in range(N_REQUEST):

        tipo = tipi[random.randint(0,2)]
        estensione = estensioni[random.randint(0,1)]

        NUM = random.randint(0,100)

        pathFile = f"/user/file_{NUM}.{estensione}"

        print(f"\n[USER] Invio al proxy richiesta {_}: {pathFile}-{tipo}")

        #richiesta di stampa
        proxy = PrinterProxy('localhost', 5000)
        response = proxy.print(pathFile, str(tipo))
        
        print(f"[PROXY] Risposta del server: {response}")

        time.sleep(1)




if __name__=="__main__":
    main()