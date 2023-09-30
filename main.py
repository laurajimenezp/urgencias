from business.paciente import Patient
from business.triage import Triage

paciente1 = Patient('2929292929', "ana", "perez", 44, 78)
print(paciente1)

triage1 = Triage(paciente1)

triage1.add_symptom("Paro cardíaco"),
triage1.add_symptom("Paro respiratorio") 
triage1.add_symptom("Shock")
triage1.add_symptom("Convulsión")
triage1.add_symptom("Pérdida de un órgano")

print(triage1)

# triage1.assign_code()



