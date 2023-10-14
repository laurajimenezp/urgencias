from business.paciente import Patient
from business.triage import Triage
from business.attention import Attention
from collections import deque 
import csv


codigos_azul = []
codigos_urgente = []
codigos_normal = []
codigos_leve = []


with open('/Users/laurajimenez/dev_study/urgencias/data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        paciente = Patient(row[0], row[1], row[2], row[3], row[4], row[5])
        triage = Triage(paciente)
        triage.add_symptom(row[5])
        triage.assign_code()
        atencion = Attention(paciente, triage.get_code())
        
        if triage.get_code()=="Azul":
            codigos_azul.append(atencion)
        
        if triage.get_code()=="Urgente":
            codigos_urgente.append(atencion)
            
        if triage.get_code()=="Normal":
            codigos_normal.append(atencion)
            
        if triage.get_code()=="Leve":
            codigos_leve.append(atencion)
         
""" for a in codigos_azul:
    print(a)
        
for b in codigos_urgente:
    print(b)
        
for c in codigos_normal:
    print(c)
        
for d in codigos_leve:
    print(d) """


""" q=deque()
[q.append(k) for k in codigos_azul] """

a = len(codigos_azul)
i=0
while i < a:
    print("\nPersonas atendidas de codigo azul:") 
    print(codigos_azul.pop()) 
    i+=1
    
           

b = len(codigos_urgente)
i=0
while i < b:
    print("\nPersonas atendidas de Urgencias:") 
    print(codigos_urgente.pop()) 
    i+=1


c = len(codigos_normal)
i=0
while i < c:
    print("\nPersonas atendidas de urgencias normales:") 
    print(codigos_normal.pop()) 
    i+=1

    
d = len(codigos_leve)
i=0
while i < d:
    print("\nPersonas atendidas de urgencias leves:") 
    print(codigos_leve.pop()) 
    i+=1

   
   
