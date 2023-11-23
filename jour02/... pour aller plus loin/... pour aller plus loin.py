# Program to determine if a triangle can be formed from given lengths and its type

def can_form_triangle(a, b, c):
    """Check if three lengths can form a triangle."""
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    """Determine the type of the triangle."""
    if a == b and b == c:
        return "Équilatéral"
    elif a == b or b == c or a == c:
        isosceles = True
    else:
        isosceles = False

    # Check for right triangle using Pythagoras theorem
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        if isosceles:
            return "Rectangle isocèle"
        return "Rectangle"
    
    if isosceles:
        return "Isocèle"
    
    return "Quelconque"

# Input from user
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Determine if it's possible to form a triangle
if can_form_triangle(a, b, c):
    print(f"Un triangle peut être formé, et il est de type : {triangle_type(a, b, c)}")
else:
    print("Il n'est pas possible de former un triangle avec ces longueurs.")

