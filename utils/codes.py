triage_codes = {
    "Azul": ["Paro cardíaco", "Paro respiratorio", "Shock", "Convulsión", "Pérdida de un órgano", "Pérdida de una extremidad"],
    "Urgente": ["Taquicardia", "Presión arterial alta con dolores de cabeza", "Pérdida de equilibrio", "Asfixia grave", "Sangrado", "Dolor extremo", "Intoxicación"],
    "Normal": ["Dolor en el pecho", "Palpitaciones", "Presión arterial alta", "Asfixia leve", "Trauma nasal"],
    "Leve": ["Amigdalitis", "Faringitis", "Diarrea sin deshidratación", "Presión arterial alta no controlada"]
}

def match_sympthom(code_sympthoms, pacient_sympthoms):
    match = False
    for s in pacient_sympthoms:
        print('sintoma paciente > ', s)
        if s in code_sympthoms:
            match= True
            break
    
    print(match)    
    return match

def get_code(pacient_sympthoms):
    assigned_code = "Normal"
    for code in triage_codes:
        print('Busqueando en Codigo : ', code )
        print(' sintomas sistema: ', triage_codes[code])
        if match_sympthom(triage_codes[code], pacient_sympthoms):
            assigned_code = code
            break
            
    return assigned_code
        
            

    