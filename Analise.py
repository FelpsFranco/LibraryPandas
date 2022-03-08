import pandas as pd
import matplotlib.pyplot as plt

def abre_arquivo():
    arquivo = pd.read_excel('ProjetandoValores.xlsx', engine='openpyxl')
    return arquivo

def calcula_lucro(arquivos):
    arquivos.loc[arquivos['Tipo']=='Cookie', 'Lucro Liquído'] = arquivos['Preço de Venda'] * arquivos['Quantidade Vendida'] - arquivos['Preço Custo'] * arquivos['Quantidade Vendida']
    arquivos.loc[arquivos['Tipo'] == 'Caixa', 'Lucro Liquído'] = arquivos['Preço de Venda'] * arquivos['Quantidade Vendida'] - arquivos['Preço Custo'] * arquivos['Quantidade Vendida']

def gera_excel(arquivos):
    arquivos.to_excel('ValoresAtualizados.xlsx', index=False)

def grafico(arquivos):
    plt.pie(arquivos['Lucro Liquído'], labels=arquivos['Produtos'], autopct='%1.0f%%')
    plt.show()

def inicia():
    arquivo = abre_arquivo()
    print(arquivo)
    print('\n\n\n')
    calcula_lucro(arquivo)
    print(arquivo)
    gera_excel(arquivo)
    grafico(arquivo)

inicia()



