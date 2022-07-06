class examen:
    def leer_archivo(self):
        archivo =open ("clientes.txt")
        for lis in archivo:
            lis =lis.rstrip()
            print (lis)
            lis=lis.replace(' ','')
            sr=lis.replace(',',' ')
            #print(sr)
            i=sr.rsplit()
            #print(linea3)
            print(i[0])
            print(i[1])
            print(i[2])
            print(i[3])
            print(i[4])
            print("\n")
        archivo.close()
Exam=examen()
Exam.leer_archivo()
            
