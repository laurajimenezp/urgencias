medical_treatment = {
    "Azul": ["Estabilización y monitoreo","Proceso curativo"], 
    "Urgente": ["Estabilizacion y monitoreo","examenes"],
    "Normal":["Examenes","Proceso curativo"],
    "Leve":["Pruebas diagnosticas","Proceso curativo"], 
}

def get_treatment(triage_code):
    return medical_treatment[triage_code]
