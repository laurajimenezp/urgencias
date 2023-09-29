class Patient:
    def __init__(self, id, first_name, last_name, age, weight, health_conditions=None, medical_care_history=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.health_conditions = health_conditions if health_conditions else []
         
    def __str__(self):
     return f"ID del paciente: {self.id}, Nombre: {self.first_name} {self.last_name}, Edad: {self.age}, Grupo de triage: {self.triage_group}, Proceso de alta: {self.discharge_status}"