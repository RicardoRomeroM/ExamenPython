import requests
class examen:
    def leer_archivo(self):
        archivo =open ("clientes.txt")
        x=0
        for lis in archivo:
            lis =lis.rstrip()
            print (lis)
            lis=lis.replace(' ','')
            datos=lis.replace(',',' ')
            i=datos.rsplit()
            contador= x+1
            
            #Tabla employee
            payload = {'Id':"1", 'surname': i[1], 'firsname': i[0]}
            r = requests.post('http://localhost:8080/Prueba/crearemployee', json=payload)
            #Tabla Country
            payload = {'Id':"1", 'code':contador , 'name': i[2]}
            r = requests.post('http://localhost:8080/Prueba3/crearpais', json=payload)
            #tabla Airpot
            payload = {'Id':"1", 'name': i[4]}
            r = requests.post('http://localhost:8080/Prueba1/crearAirport', json=payload)
            #tabla Language
            payload = {'Id':"1", 'code':contador, 'name': i[3]}
            r = requests.post('http://localhost:8080/Lenguaje/crearlenguaje', json=payload)
        archivo.close()
Exam=examen()
Exam.leer_archivo()
            
