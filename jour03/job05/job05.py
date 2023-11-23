def calcule(num1, operator, num2):
    try:
        return eval(f"{num1}{operator}{num2}")
    except ZeroDivisionError:
        return "Erreur : division par zéro"
    except Exception:
        return "Opérateur inconnu ou erreur de calcul"

print(calcule(10,'+', 5))  
print(calcule(15,'-', 5))  
print(calcule(3,'*', 4)) 
print(calcule(20,'/', 5))  
print(calcule(20,'/', 0))  
print(calcule(20,'%', 3))  
print(calcule(5,'^', 2))   
