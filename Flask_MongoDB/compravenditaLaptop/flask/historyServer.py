from flask import Flask, request

app = Flask(__name__)

#ENDPOINT PER REGISTRARE LE OPERAZIONI 
@app.post('/update_history')
def update_history():

    operation = request.get_json()

    with open("history", "a") as file:

        #scriviasmo l'operazione sul file
        file.write(operation + "\n")
    
    print(f"[HISTORY SERVER] Operazione {operation} inserita nello storico opeazioni")


if __name__=="__main__":
    app.run(debug=True)