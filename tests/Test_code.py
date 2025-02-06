coleur = [[0,2,4],[0,3,1]]
valeur = [[11,5,6],[7,3,1]]
pair = tuple((i,j) for i in range(len(coleur)) for j in range(len(coleur[0])))
print(pair)
def cost(pair):
    (i1,j1),(i2,j2) = pair
    coleur = [[0,2,4],[0,3,1]]
    valeur = [[11,5,6],[7,3,1]]

    if abs((i1-i2)) + abs(j1-j2) == 1:
        return abs(valeur[i1][j1] - valeur[i2][j2])
    return None
pair = (0, 1),(1, 1)
print(cost(pair))
 

    # for i in range(len(pair)):
    #     for j in range(pair[len(pair)][-1]):
    #         if pair[i] == pair[i-1] and abs(pair[j-1]-pair[j]) == 1:
    #             return abs(valeur[i][j]-valeur[i][j-1])
    #         elif pair[j] == pair[j-1] and abs(pair[i-1]-pair[i]) == 1:
    #             return abs(valeur[i][j]-valeur[i-1][j])