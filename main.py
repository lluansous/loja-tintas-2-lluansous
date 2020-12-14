"""Arquivo principal que será interpretado pelo interpretador."""
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    metros = float(input('Digite a quantidade de metros quadrados:'))
    folga = (metros/6) * 1.1
    
    #valor pra latas
    latas = math.ceil(folga/18)
    vlatas = latas*80
    
    
    #valor pra galões
    galao = math.ceil(folga/3.6)
    vgalao = galao*25
    
    
    #valor de ambos
    latasmin = math.floor(folga/18)
    vlatasmin = latasmin*80
    falta = folga - latasmin * 18
    galaomin = math.ceil(falta/3.6)
    vgalaomin = galaomin*25
    vtotal = vlatasmin + vgalaomin

    #print
    print(f'O valor gasto comprando apenas latas é de R$ {vlatas:.2f}.')
    print(f'Serão necessárias {latas} latas.')
    print(f'O valor gasto comprando apenas galões é de R$ {vgalao:.2f}.')
    print(f'Serão necessários {galao} galões.')
    print(f'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ {vtotal:.2f}.')
    print(f'Serão necessárias {latasmin} latas e {galaomin} galões.')

if __name__ == '__main__':
    main()
