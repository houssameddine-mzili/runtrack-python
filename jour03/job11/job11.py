def time_to_text(minutes):
    if not isinstance(minutes, int) or minutes < 0:
        return "Veuillez entrer un nombre entier positif de minutes."
    
    heures = minutes // 60
    minutes_restantes = minutes % 60

    return f"{heures} heures et {minutes_restantes} minutes"

exemple = time_to_text(160)

tests = [
    time_to_text(45),   
    time_to_text(120),   
    time_to_text(-10),   
    time_to_text(0),     
    time_to_text(1439)   
]

print(exemple)

