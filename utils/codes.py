triage_codes = {
    
"Azul": ["Paro cardíaco", "Paro respiratorio", "Shock", "Convulsión", "Pérdida de un órgano", "Pérdida de una extremidad"],
"Urgente": ["Taquicardia", "Presión arterial alta con dolores de cabeza", "Pérdida de equilibrio", "Asfixia grave", "Sangrado", "Dolor extremo", "Intoxicación"],
"Normal": ["Dolor en el pecho", "Palpitaciones", "Presión arterial alta", "Asfixia leve", "Trauma nasal"],
"Leve": ["Amigdalitis", "Faringitis", "Diarrea sin deshidratación", "Presión arterial alta no controlada"]

}

def match_sympthom(code_sympthoms, pacient_sympthoms):
    for s in pacient_sympthoms:
        if s in code_sympthoms:
            return True

def get_code(sympthoms):
    for code in triage_codes:
        if match_sympthom(triage_codes[code], sympthoms):
            return code
        return "Normal"
        
            

    