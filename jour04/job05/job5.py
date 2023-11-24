def replace_third_with_sum(L):
    if len(L) > 4:  
        L[3] = L[2] + L[4]
    return L

L = [1, 2, 3, 4, 5]

second_value = L[1]

modified_list = replace_third_with_sum(L)

last_value = L[-1]

print(second_value,"\n",modified_list,"\n",last_value)
