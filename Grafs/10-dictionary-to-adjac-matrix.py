g = {
    '0': ['0', '1', '2'], 
    '1': ['0', '2', '4'], 
    '2': ['0', '1', '3'],
    '3': ['2','4'],
    '4': ['1','3']
}

def DictToMatrix(Dict):
    keys = sorted(Dict.keys())
    size = len(keys)
    M = [[0]*size for i in range(size)]
    for a,b in [(keys.index(a), keys.index(b)) for a, row in g.items() for b in row]:
        M[a][b] = 2 if (a==b) else 1
        
    return M
    
print(DictToMatrix(g))
