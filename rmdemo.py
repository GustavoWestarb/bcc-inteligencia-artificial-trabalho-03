from collections import namedtuple
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import demo

class CorrelacaoRegressaoLinearMultipla:
    def __init__(self):
        dados = self. ler_dados()

        variaveis = self.definir_variaveis(dados)

        # Matriz_x
        # 0 - Primeira coluna é sempre um
        # 1 - Segunda coluna é tamanho da casa
        # 2 - Terceira coluna é o número de quartos
        matriz_x = variaveis.matri_x
        vetor_y = variaveis.vetor_y

        correlacao_tamanho_casa = self.correlacao_por_variavel(1, matriz_x, vetor_y)
        correlacao_numero_quartos = self.correlacao_por_variavel(2, matriz_x, vetor_y)


    def reg_multipla(self):
        pass


    def correlacao_por_variavel(self, variavel, matriz_x , vetor_y):

        matriz_np = np.array(matriz_x)
        vetor_x = matriz_np[:, variavel]

        return self.correlacao(vetor_x, vetor_y)


    def definir_variaveis(self, dados):
        
        matriz_aux = []
        vetor_y_aux = []

        for i, array in enumerate(dados.values):
            matriz_aux.append([1, array[0], array[1]])
            vetor_y_aux.append(array[2])
        
        _retorno = namedtuple("retorno", ["matri_x", "vetor_y"])

        return _retorno(matriz_aux, vetor_y_aux)

    def correlacao(self, vetor_x, vetor_y):
    
        quantidade_elementos_x = len(vetor_x)
        quantidade_elementos_y = len(vetor_y)

        soma_x = self.somar_valores(vetor_x, quantidade_elementos_x)
        media_x = soma_x / quantidade_elementos_x

        soma_y = self.somar_valores(vetor_y, quantidade_elementos_y)
        media_y = soma_y / quantidade_elementos_y

        soma_parte_baixo_1 = 0.0
        soma_parte_baixo_2 = 0.0
        soma_parte_cima = 0.0
        
        for i in range(quantidade_elementos_x):
            x = float(vetor_x[i])
            y = float(vetor_y[i])

            parte_cima_1 = x - media_x
            parte_cima_2 = y - media_y
            soma_parte_cima = soma_parte_cima + (parte_cima_1 * parte_cima_2)

            parte_baixo_1 = math.pow((x - media_x), 2)
            soma_parte_baixo_1 = soma_parte_baixo_1 + parte_baixo_1

            parte_baixo_2 = math.pow((y - media_y), 2)
            soma_parte_baixo_2 = soma_parte_baixo_2 + parte_baixo_2

        parte_baixo = soma_parte_baixo_1 * soma_parte_baixo_2
        parte_baixo = math.sqrt(parte_baixo)

        coefiente_correlacao = soma_parte_cima / parte_baixo

        return coefiente_correlacao


    def somar_valores(self, vetor, quantidade_elementos):
        soma = 0.0
        for i in range(quantidade_elementos):
            soma = soma + vetor[i]
        return soma


    def ler_dados(self):
        return pd.read_csv('.\/assets\/Dados\/data.csv')


if __name__ == "__main__":
    c = CorrelacaoRegressaoLinearMultipla()
