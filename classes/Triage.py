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
          
     
          