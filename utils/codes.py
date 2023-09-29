triage_codes = {
    "Blue": ["Cardiac arrest", "Respiratory arrest", "Shock", "Seizure", "Loss of an organ", "Loss of a limb"],
    "Urgent": ["Tachycardia", "High blood pressure with headaches", "Loss of balance", "Severe choking", "Bleeding", "Extreme pain", "Intoxication"],
    "Normal": ["Chest pain", "Palpitations", "High blood pressure", "Mild choking", "Nasal trauma"],
    "Mild": ["Tonsillitis", "Pharyngitis", "Diarrhea without dehydration", "Uncontrolled high blood pressure"]
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
        
            

    