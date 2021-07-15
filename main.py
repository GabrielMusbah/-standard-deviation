import numpy  # biblioteca usada para fazer a media dos valores presentes na lista
import math  # biblioteca de funcoes matematicas, usado para fazer a raiz


def lerListaNumero():
    print("Digite os valores a serem analizados em apenas uma linha: ")
    listaNumero = input().split()

    return listaNumero


def converterLista(listaNumero):
    listaNumero = list(map(int, listaNumero))  # converter uma lista strings em inteiros

    return listaNumero


def quantidadeNumero(listaNumero):
    quantidadeNumero = len(listaNumero)

    return quantidadeNumero


def mediaLista(listaNumero):
    mediaLista = numpy.mean(listaNumero)

    return mediaLista


def listaComMedia(mediaLista, quantidadeNumero):
    listaComMedia = []

    while quantidadeNumero > 0:
        listaComMedia.append(mediaLista)
        quantidadeNumero = quantidadeNumero - 1

    return listaComMedia


def listaNumeroMenosMedia(listaNumero, listaComMedia):  # fazer a lista numero menos a lista de media
    listaNumeroMenosMedia = []

    listaNumeroMenosMedia = [(a - b) for a, b in zip(listaNumero, listaComMedia)]

    return listaNumeroMenosMedia


def listaNumeroMenosMediaAoQuadrado(listaNumeroMenosMedia):
    listaNumeroMenosMediaAoQuadrado = []

    listaNumeroMenosMediaAoQuadrado = [(a * b) for a, b in zip(listaNumeroMenosMedia, listaNumeroMenosMedia)]

    return listaNumeroMenosMediaAoQuadrado


def somaLista(listaNumeroMenosMediaAoQuadrado):
    somaLista = sum(listaNumeroMenosMediaAoQuadrado)

    return somaLista


def dividirSomaPorQuantidadeNumero(somaLista, quantidadeNumero):
    dividirSomaPorQuantidadeNumero = somaLista / (quantidadeNumero - 1)

    return dividirSomaPorQuantidadeNumero


def desvioPadrao(dividirSomaPorQuantidadeNumero):
    desvioPadrao = math.pow(dividirSomaPorQuantidadeNumero, 1 / 2)

    return desvioPadrao


listaNumero = lerListaNumero()

listaNumero = converterLista(listaNumero)

quantidadeNumero = quantidadeNumero(listaNumero)

mediaLista = mediaLista(listaNumero)

listaComMedia = listaComMedia(mediaLista, quantidadeNumero)

listaNumeroMenosMedia = listaNumeroMenosMedia(listaNumero, listaComMedia)

listaNumeroMenosMediaAoQuadrado = listaNumeroMenosMediaAoQuadrado(listaNumeroMenosMedia)

somaLista = somaLista(listaNumeroMenosMediaAoQuadrado)

dividirSomaPorQuantidadeNumero = dividirSomaPorQuantidadeNumero(somaLista, quantidadeNumero)

desvioPadrao = desvioPadrao(dividirSomaPorQuantidadeNumero)

print("desvio padrao: %0.5f" % desvioPadrao)