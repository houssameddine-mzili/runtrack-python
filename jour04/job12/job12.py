def tri_bulles(L):
    n = 0  
    for i in L:
        n += 1

    
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L


L = [64, 34, 25, 12, 22, 11, 90]
L_triee = tri_bulles(L)
print(L_triee)
