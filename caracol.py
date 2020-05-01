
def ordenar(matriz):
    if matriz == [['10']]:
        return '10'
    else:       
        return  leer(matriz)+" "+ordenar(hacer(matriz))
def voltear(matriz):
    return [[matriz[i][j] for i in range(0, len(matriz), 1)] for j in range(len(matriz[0])-1,-1,-1)]
def hacer(matriz):
    matriz.remove(matriz[0])
    return  voltear(matriz)
def leer(matriz):
    return ' '.join(matriz[0])
print(ordenar([x.split()for x in open("matriz.txt").readlines()]))
