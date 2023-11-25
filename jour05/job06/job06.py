def distance_to_toilet(steps, height_per_step):
    
    trips_per_day = 5 * 2
    
    height_per_step_in_meters = height_per_step / 100
   
    distance_per_step = 2 * steps * height_per_step_in_meters
    
    total_distance_per_week = distance_per_step * trips_per_day * 7
    
    return f"Pour {steps} marches de {height_per_step} cm, le gardien parcourt {total_distance_per_week:.2f} m par semaine."

print(distance_to_toilet(100, 15))
