import queue
from utils import codes

class Triage:
     def __init__(self, pacient):
          self.pacient = pacient
          self.symptoms = []
          self.code = ""
     
     def add_symptom(self, symptom):
          self.symptoms.append(symptom)
     
     def assign_code(self):
          self.code = codes.get_code(self.symptoms)
          
     def get_code(self):
          return self.code
          
     def symptoms_str(self):
          all_symtoms = ""
          for s in self.symptoms:
               all_symtoms = all_symtoms + " - " +  s 
          
          return all_symtoms
     
          
     def __str__(self):
          return "Sintomas >>> " + self.symptoms_str() + "Codigo: " + self.code
     
    