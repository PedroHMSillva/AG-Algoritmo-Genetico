
from alg_gen import alg_gen

saida = [
    {'item': 'Lapis', 'peso': 1, 'valor': 10},
    {'item': 'Borracha', 'peso': 2, 'valor': 20},
    {'item': 'Caderno', 'peso': 3, 'valor': 30},
    {'item': 'Apostila', 'peso': 4, 'valor': 40},
    {'item': 'Caneta', 'peso': 5, 'valor': 50},
    {'item': 'Cálculadora', 'peso': 6, 'valor': 60},
]

def funFitness(genes, saida):
    peso = 0
    valor = 0
    for i in range(len(genes)):
        #Adiciona os itens na bolsa
        if (genes[i]==1):
            peso += saida[i]['peso']
            valor += saida[i]['valor']
            
    
    if (peso > 10):
        return 0
    return valor

ag = alg_gen(saida, funcaoFitness=funFitness )
ag.executa()

print(ag.populacao)




        
            
