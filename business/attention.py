from utils import treatment

class Attention:
   def __init__(self, pacient, triage_code):
      self.status = "admision"
      self.pacient = pacient
      self.triage_code = triage_code
      self.treatments = []
      self.assign_treatment()
        
   def assign_treatment(self):
      self.treatments = treatment.get_treatment(self.triage_code)
          
   def set_status(self, status):
      self.status = status
      
   def treatments_str(self):
          all_treatments = ""
          for s in self.treatments:
               all_treatments = all_treatments + " - " +  s 
          
          return all_treatments
     
   def __str__(self):
          return "Tratamientos >>> " + self.treatments_str() + "Estado : " + self.status
      
