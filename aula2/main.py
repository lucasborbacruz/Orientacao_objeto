from aula2 import Produto as prod
from gestao_escola import Escola as scho

produto1 = prod('leite', 20.00, 40)
produto2 = prod('maca', 9.99, 30)
produto3 = prod('agua', 3.99, 20)

aluno1 = scho('Ze da manga', 25)
aluno2 = scho('Ze da cove', 30)
aluno3 = scho('Maria manga', 45)

listaP = [produto1, produto2, produto3]
listaS = [aluno1, aluno2, aluno3]

for i in range(3):
    listaP[i].apresentacao(), print('comprou'), listaS[i].apresentar(), print('apresentacao')
