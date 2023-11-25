def my_sort(lst):
    swaps = 0
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swaps += 1
                sorted = False
    
    return lst, swaps

sample_list = [34, 11, 90, 25, 12, 22, 64]
sorted_list, total_swaps = my_sort(sample_list)

print(f"Nombre total de coups nécessaires pour trier la liste : {total_swaps}")
print(f"Liste triée : {sorted_list}")
