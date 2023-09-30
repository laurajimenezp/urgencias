from utils import treatment

class Attention:
   def __init__(self ):
      self.status = "admision"
      self.treatments = []
        
   def assign_treatment(self):
      self.treatments = treatment.get_treatment(self.code)
          
   def set_status(self, status):
      self.status = status
      
