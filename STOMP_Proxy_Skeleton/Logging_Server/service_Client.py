import time, random
from logging_proxy import LoggingProxy


N_ENTRY=10

def main():

    proxy=LoggingProxy('localhost', 5000)

    for _ in range(N_ENTRY):

        tipo=random.randint(0,2)

        if tipo==0 or tipo==1:
            messaggioLog=random.choice(["success","checking"])            
            proxy.log(messaggioLog, tipo)

        
        elif tipo==2:
            messaggioLog=random.choice(["fatal","exception"])            
            proxy.log(messaggioLog, tipo)

        #proxy.log(messaggioLog, tipo)

        
        time.sleep(1)


if __name__=="__main__":
    main()
