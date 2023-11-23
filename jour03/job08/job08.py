def farm(type,saison):
    if type == "fruits" and saison== "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison== "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison== "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison== "ete":
        print("artichaut, aubergine,navet")
    else:
        print("Type ou saison non spécifié ou non reconnu")


farm("fruits", "hiver")
farm("fruits", "ete")
farm("legume", "hiver")
farm("legume", "ete")